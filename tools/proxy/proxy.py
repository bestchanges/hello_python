from flask import Flask, request, Response
import requests
from flask_cors import CORS
from requests.auth import HTTPBasicAuth

import logging
import argparse

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1

parser = argparse.ArgumentParser(
    description="This proxy is for development purposes. It was developed to use with local installation of Jira, "
                + "but can serve other web services. "
                + "It passes CORS policy so can be used in AJAX requests from browser.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("--target", help="Target web service. WITH TRAILING SLASH!", default='http://localhost:2990/jira/')
parser.add_argument("--basic-auth", required=False, help="Basic auth in the form user:password")
parser.add_argument("--port", help="Port which proxy will listen", default="8080")
parser.add_argument("--debug", help="Print extended debugging information for each request", default="8080")
parser.add_argument("--cache", type=bool, help="If set to True then cache all GET responses until restart", default=True)
args = parser.parse_args()

logging.info(f"Using parameters: {args}")

SITE_NAME = args.target
BASIC_AUTH = args.basic_auth.split(":") if args.basic_auth else ()
PORT = args.port
DO_CACHE = args.cache

cache = dict()

def _proxy(*args, **kwargs):
    url = request.url
    method = request.method
    if DO_CACHE and method == 'GET' and url in cache:
        logging.info(f"Return cached response for {url}")
        return cache[url]
    resp = requests.request(
        method=method,
        url=request.url.replace(request.host_url, SITE_NAME),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        auth=HTTPBasicAuth(*BASIC_AUTH) if BASIC_AUTH else None
    )

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    if DO_CACHE and method == 'GET':
        logging.info(f"Keep to cache response for {url}")
        cache[url] = response
    return response


app = Flask('__main__')
CORS(app, supports_credentials=True)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    return _proxy()

app.run(host='0.0.0.0', port=PORT)

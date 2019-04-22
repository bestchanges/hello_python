#!/usr/bin/env bash
# my branch
curl 'https://api.github.com/search/repositories?sort=stars&q=stars:>500&page=1&per_page=100' > r1.json


# one-liner with unix pipes
# curl 'https://api.github.com/search/repositories?sort=stars&per_page=500&q=stars:>500' | jq .items[].language | sort | uniq -c | sort -nr
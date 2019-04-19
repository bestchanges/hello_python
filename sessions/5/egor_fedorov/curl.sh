#!/usr/bin/env bash
curl 'https://api.github.com/search/repositories?sort=stars&q=stars:>500&page=1&per_page=100' > r1.json

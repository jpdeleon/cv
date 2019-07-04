#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import requests

headers = {
    "Authorization": "Bearer {0}".format(os.environ["GITHUB_API_KEY"])}

query = """
{
  user(login: "dfm") {
    pinnedItems(first: 6, types: [REPOSITORY]) {
      totalCount
      edges {
        node {
          ... on Repository {
            name
            description
            url,
            homepageUrl
            forkCount
            stargazers {
              totalCount
            }
            watchers {
              totalCount
            }
          }
        }
      }
    }
  }
}
"""

r = requests.post("https://api.github.com/graphql",
                  json={"query": query}, headers=headers)
r.raise_for_status()
result = r.json()
with open("repos.json", "w") as f:
    json.dump(result, f, indent=2)

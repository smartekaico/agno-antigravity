# Skill: Apify Actor Runner

## Trigger

- Auto: Enrichment steps in lead generation pipeline.
- Manual: `/apify run {actor_id} {input_json}`

## Description

Executes Apify Actors to scrape data from various platforms (Instagram, LinkedIn, Google Maps).

## Inputs

| Param     | Type   | Required | Description                                          |
| :-------- | :----- | :------- | :--------------------------------------------------- |
| actor_id  | string | Yes      | The Apify Actor ID (e.g., `apify/instagram-scraper`) |
| run_input | object | Yes      | JSON input specific to the actor                     |
| memory    | int    | No       | Memory in MB (default: 4096)                         |

## Outputs

| Field  | Type   | Description             |
| :----- | :----- | :---------------------- |
| status | string | "SUCCEEDED" or "FAILED" |
| data   | array  | List of items scraped   |
| log    | string | URL to run log          |

## Configuration

Required Environment Variable: `APIFY_TOKEN`

## Implementation (Python)

```python
from apify_client import ApifyClient
import os
import json

def run_actor(actor_id, run_input):
    api_token = os.getenv('APIFY_TOKEN')
    if not api_token:
        raise ValueError("APIFY_TOKEN env var not found")

    client = ApifyClient(api_token)

    # Start the actor and wait for it to finish
    run = client.actor(actor_id).call(run_input=run_input)

    # Fetch results
    dataset_items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
    return dataset_items
```

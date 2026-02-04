# Skill: Olostep Scraper

## Trigger

- Auto: Lead enrichment or general web scraping when `crawl4ai` or `serper` is insufficient or when explicit "Olostep" usage is requested.
- Manual: `/olostep scrape {url} {prompt}`

## Description

Executes Olostep API calls to scrape or crawl web pages. Olostep is capable of handling complex interactions and returning structured data.

## Inputs

| Param  | Type   | Required | Description                                      |
| :----- | :----- | :------- | :----------------------------------------------- |
| url    | string | Yes      | The URL to scrape or crawl.                      |
| prompt | string | No       | Specific extraction prompt (e.g., "Find emails") |

## Outputs

| Field  | Type   | Description             |
| :----- | :----- | :---------------------- |
| status | string | "SUCCEEDED" or "FAILED" |
| data   | object | Scraped data content    |

## Configuration

Required Environment Variable: `OLOSTEP_API_KEY`

## Implementation (Python)

```python
import requests
import os
import time

def run_olostep_scrape(url, prompt=None):
    api_key = os.getenv('OLOSTEP_API_KEY')
    if not api_key:
        raise ValueError("OLOSTEP_API_KEY env var not found")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Use the /v1/scrapes endpoint for single page extraction
    endpoint = "https://api.olostep.com/v1/scrapes"

    payload = {
        "url": url,
    }

    if prompt:
        payload["prompt"] = prompt

    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Olostep API Error: {e.response.text}")
        return None
```

---
description: Run the multi-strategy lead generation pipeline.
---

# Workflow: Lead Generation

## Description

Executes the lead search pipeline based on the selected strategy (`LOCAL` or `B2B`).

## Usage

```bash
# For Local Businesses (Instagram focus)
python -m src.lead_gen --strategy LOCAL --niche "Coffee" --location "Austin, TX"

# For B2B (LinkedIn focus)
python -m src.lead_gen --strategy B2B --role "CTO" --niche "SaaS" --location "London"
```

## Steps

1.  **Load Configuration**
    - Read `APIFY_TOKEN` and `SERPER_API_KEY`.
    - Parse arguments (strategy, niche, location).

2.  **Discovery Phase (Serper)**
    - If `LOCAL`: Call Google Places API for `"{niche} in {location}"`.
    - If `B2B`: Call Google Search API for `"site:linkedin.com/in/ {role} {niche} {location}"`.

3.  **Qualification Phase**
    - If `LOCAL`: Visit website (Crawl4AI) to find IG link. Fallback to Google Search.
    - If `B2B`: Filter results by title match (if possible via snippet).

4.  **Enrichment Phase (Apify)**
    - If `LOCAL`: Run `apify/instagram-scraper` on found handles.
    - If `B2B`: Run `apify/linkedin-scraper` (or equivalent) on found profile URLs.

5.  **Save Results**
    - Append validated leads to `Leads_Master` Google Sheet (or CSV for now).

## Prerequisites

- `pip install apify-client crawl4ai google-search-results pandas`

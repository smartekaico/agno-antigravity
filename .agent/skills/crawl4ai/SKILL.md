# Skill: Web Scraper (Crawl4AI)

## Trigger

- Auto: Enrichment phase for new leads.
- Manual: `/scrape {url}`

## Inputs

| Param             | Type   | Required | Default |
| ----------------- | ------ | -------- | ------- |
| url               | string | Yes      | -       |
| extraction_prompt | string | No       | -       |
| timeout           | int    | No       | 30000   |

## Outputs

| Field    | Type   | Description              |
| -------- | ------ | ------------------------ |
| markdown | string | Cleaned page content     |
| metadata | object | Title, description, etc. |

## Cost

Compute only (runs locally/hosted).

# Directive: Lead Enrichment

## Goal

Enrich "new" leads with deep company and profile data using Crawl4AI scraping and LLM-based content analysis to enable hyper-personalized outreach.

## Inputs

| Input       | Source             | Required | Validation    |
| ----------- | ------------------ | -------- | ------------- |
| Lead ID     | Leads_Master Sheet | Yes      | UUID          |
| Website URL | Leads_Master Sheet | Yes      | Valid URL     |
| Status      | Leads_Master Sheet | Yes      | Must be "new" |

## Skills

| Skill              | Purpose                                    | Trigger           |
| ------------------ | ------------------------------------------ | ----------------- |
| `crawl4ai-scraper` | Scrape company website (About, Team, News) | Per lead URL      |
| `llm-analyzer`     | Extract structured data & hooks            | After scraping    |
| `sheet-reader`     | Get leads to enrich                        | Start of workflow |
| `sheet-writer`     | Update enrichment data                     | After analysis    |

## Outputs

| Output         | Format              | Destination                     |
| -------------- | ------------------- | ------------------------------- |
| Company Data   | Text/JSON           | Google Sheet: `Enrichment_Data` |
| Personal Hooks | List[String]        | Google Sheet: `Enrichment_Data` |
| Lead Status    | String ("enriched") | Google Sheet: `Leads_Master`    |

## Edge Cases

| Scenario            | Handling                                     |
| ------------------- | -------------------------------------------- |
| Website 404/Offline | Mark valid=false, skip enrichment, log error |
| Scraping blocked    | Retry with different user-agent or skip      |
| Content too short   | Fallback to basic info, flag low quality     |
| LLM Analysis Fail   | Retry once, then log error                   |

## Success Criteria

- [ ] Successfully scrape valid websites (Homepage, About, Team)
- [ ] LLM extracts: Description, Pain Points, Recent News
- [ ] 3 distinct personalization hooks identified per lead
- [ ] Data written to Enrichment_Data sheet
- [ ] Lead status updated to "enriched"

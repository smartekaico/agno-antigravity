# Directive: Lead Search

## Goal

Automate the discovery and enrichment of leads using specific pipelines based on the target niche.

## Search Strategies

### 1. Local Business (Retail, Gyms, Restaurants)

- **Focus:** Instagram presence & physical location.
- **Pipeline:**
  1.  **Discovery**: Google Maps (Serper) -> Business Name, Address, Website.
  2.  **Qualification**: Check Website for IG link OR Google Search `site:instagram.com`.
  3.  **Enrichment**: Apify Instagram Scraper -> Followers, Bio, Email.
  4.  **Edge Case**: If "No IG", mark as low priority.

### 2. B2B / Professional (IT, Healthcare, Consultants)

- **Focus:** LinkedIn profiles & decision makers.
- **Pipeline:**
  1.  **Discovery**: Google X-Ray Search (Serper) -> `site:linkedin.com/in/ "{Role}" "{Industry}"`
  2.  **Qualification**: Filter by "Current Role" match.
  3.  **Enrichment**: Apify LinkedIn Scraper (or Visit Profile) -> Company, full bio.
  4.  **Extension**: Find Company Website -> Look for corporate email.

## Inputs

| Input          | Source        | Required | Description                            |
| :------------- | :------------ | :------- | :------------------------------------- |
| **Strategy**   | System_Config | Yes      | `LOCAL` or `B2B`                       |
| Niche/Industry | System_Config | Yes      | e.g., "Coffee Shop" or "Cybersecurity" |
| Role           | System_Config | No       | e.g., "Owner" or "CTO" (B2B only)      |
| Location       | System_Config | Yes      | Target city/region                     |

## Skills & Tools

| Skill         | Purpose                                            | Configuration    |
| :------------ | :------------------------------------------------- | :--------------- |
| `serper-tool` | Discovery (Maps for Local, Google Search for B2B). | `SERPER_API_KEY` |
| `crawl4ai`    | Qualification (Web scraping).                      | Local Skill      |
| `apify`       | Enrichment (IG or LinkedIn scraping).              | `APIFY_TOKEN`    |

## Outputs

| Output | Destination          | Fields                                                                       |
| :----- | :------------------- | :--------------------------------------------------------------------------- |
| Leads  | `Leads_Master` Sheet | Name, Role, Company, Website, Social URL, Email, Phone, **Type** (Local/B2B) |

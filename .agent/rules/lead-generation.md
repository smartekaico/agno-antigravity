# Rule: Lead Generation & Data Handling

P3 Priority (Domain)

## MUST

- **Rate Limiting**:
  - Serper: Max 100/day (Free Tier).
  - MailRelay: Max 2,500/day.
  - Crawl4AI: 2-second delay between sites.
- **Compliance**:
  - Include physical address in all emails.
  - Honor unsubscribes within 48 hours.
  - Only collect publicly available data.
- **Data Integrity**:
  - Validated inputs for all API calls.
  - Deduplicate leads before adding to Master list.

## SHOULD

- Cache search results for 7 days.
- Cache scraped content for 30 days.
- Verify emails before sending to reduce bounce rate.

## MUST NOT

- Email leads with score < 50.
- Send emails to "Do Not Contact" domains.
- Scrape sites with explicit `robots.txt` Disallow for our User-Agent.

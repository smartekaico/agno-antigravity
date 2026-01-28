# Directive: Lead Search

## Goal

Automate the discovery of potential leads using Serper.dev based on defined criteria (Industry, Position, Location) and populate the "Leads_Master" sheet.

## Inputs

| Input          | Source                        | Required | Validation                |
| -------------- | ----------------------------- | -------- | ------------------------- |
| Industry       | Google Sheets (System_Config) | Yes      | Non-empty string          |
| Position       | Google Sheets (System_Config) | Yes      | Non-empty string          |
| Location       | Google Sheets (System_Config) | Yes      | Non-empty string          |
| Exclusion List | Google Sheets (System_Config) | No       | List of domains/companies |

## Skills

| Skill             | Purpose                      | Trigger                  |
| ----------------- | ---------------------------- | ------------------------ |
| `serper-tool`     | Execute search queries       | Per criteria combination |
| `sheet-reader`    | Read config parameters       | Start of workflow        |
| `sheet-writer`    | Store new leads              | After deduplication      |
| `email-extractor` | Extract emails from snippets | Post-search              |

## Outputs

| Output     | Format    | Destination                  |
| ---------- | --------- | ---------------------------- |
| New Leads  | Row Data  | Google Sheet: `Leads_Master` |
| Search Log | Log Entry | Google Sheet: `System_Logs`  |

## Edge Cases

| Scenario         | Handling                                               |
| ---------------- | ------------------------------------------------------ |
| No results found | Log warning, proceed to next criteria                  |
| API Rate Limit   | Pause execution, retry after backoff                   |
| Duplicate Lead   | Check `email` OR (`name` + `company`). Skip if exists. |
| Invalid API Key  | Alert user, halt execution                             |

## Success Criteria

- [ ] Search parameters correctly read from System_Config
- [ ] Serper.dev API successfully queried
- [ ] Results parsed and deduplicated against existing leads
- [ ] New leads written to Leads_Master with status "new"
- [ ] 0 Duplicates added

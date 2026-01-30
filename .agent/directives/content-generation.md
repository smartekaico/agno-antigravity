# Directive: Content Generation

## Goal

Generate hyper-personalized email content (icebreakers, subject lines, full emails) for enriched leads using LLM-powered content analysis and templates.

## Inputs

| Input           | Source                | Required | Validation                    |
| --------------- | --------------------- | -------- | ----------------------------- |
| Lead ID         | Leads_Master Sheet    | Yes      | UUID, status="enriched"       |
| Enrichment Data | Enrichment_Data Sheet | Yes      | Non-empty hooks & description |
| Templates       | Email_Templates Sheet | Yes      | Active templates available    |
| Campaign Config | System_Config Sheet   | Yes      | Campaign goals defined        |

## Skills

| Skill               | Purpose                           | Trigger               |
| ------------------- | --------------------------------- | --------------------- |
| `template-selector` | Select best template for lead     | Per lead              |
| `icebreaker-gen`    | Generate personalized icebreakers | After template select |
| `subject-gen`       | Create subject line variations    | After icebreaker      |
| `email-composer`    | Combine elements into full email  | Final step            |
| `quality-checker`   | Validate output quality           | Before storage        |
| `sheet-writer`      | Store generated content           | After quality check   |

## Outputs

| Output          | Format          | Destination                       |
| --------------- | --------------- | --------------------------------- |
| Icebreaker Text | String          | Google Sheet: `Outreach_Tracking` |
| Subject Line    | String          | Google Sheet: `Outreach_Tracking` |
| Full Email Body | HTML/Text       | Google Sheet: `Outreach_Tracking` |
| Content Status  | "ready_to_send" | Google Sheet: `Outreach_Tracking` |

## Edge Cases

| Scenario                 | Handling                                               |
| ------------------------ | ------------------------------------------------------ |
| No personalization hooks | Use generic industry-based hook, flag low quality      |
| Template missing tokens  | Log error, skip to next template                       |
| LLM generation fails     | Retry once, fallback to template-only (no icebreaker)  |
| Content too long         | Truncate and flag for review                           |
| Spam score high          | Regenerate with safer language, alert if persistent    |
| Duplicate content        | Check against recent generations, regenerate if needed |

## Success Criteria

- [ ] Icebreaker references specific lead/company details (not generic)
- [ ] Subject line under 50 characters, no spam trigger words
- [ ] Full email under 150 words with single clear CTA
- [ ] All template tokens properly replaced
- [ ] Quality check passes (readability, relevance, tone)
- [ ] Content marked "ready_to_send" in Outreach_Tracking
- [ ] 2 variations generated for A/B testing (optional)

# Directive: Email Outreach

## Goal

Generate personalized emails for enriched leads, manage the sending queue via MailRelay, and track engagement (Opens, Clicks, Replies) to handle follow-ups.

## Inputs

| Input       | Source                         | Required | Validation        |
| ----------- | ------------------------------ | -------- | ----------------- |
| Lead Data   | Leads_Master & Enrichment_Data | Yes      | Status="enriched" |
| Templates   | Email_Templates Sheet          | Yes      | Active templates  |
| Daily Limit | Config                         | Yes      | < Daily Cap       |

## Skills

| Skill                | Purpose                     | Trigger          |
| -------------------- | --------------------------- | ---------------- |
| `content-generator`  | Generate Icebreakers & Body | Per lead         |
| `mailrelay-sender`   | Send emails via API         | Scheduled Window |
| `engagement-tracker` | Check opens/replies         | Hourly/Webhook   |
| `sheet-manager`      | Read/Write queue status     | Continuous       |

## Outputs

| Output          | Format               | Destination                       |
| --------------- | -------------------- | --------------------------------- |
| Sent Email      | JSON Log             | Google Sheet: `Outreach_Tracking` |
| Follow-up Tasks | Queue Entry          | Google Sheet: `Follow_Up_Queue`   |
| Lead Status     | String ("contacted") | Google Sheet: `Leads_Master`      |

## Edge Cases

| Scenario        | Handling                            |
| --------------- | ----------------------------------- |
| Bounce detected | Mark invalid, cancel follow-ups     |
| Unsubscribe     | Add to suppression list immediately |
| Daily limit hit | Paused queue until next window      |
| API Failure     | Retry 3 times, then alert admin     |

## Success Criteria

- [ ] Personalized icebreakers generated using hooks
- [ ] Emails sent successfully via MailRelay
- [ ] Tracking IDs logged in Outreach_Tracking
- [ ] Follow-ups scheduled automatically
- [ ] Bounces/Unsubscribes processed correctly

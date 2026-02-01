# Directive: Response Handling

## Goal

Detect, classify, and process email responses using AI to automate actions (cancel follow-ups, alert humans, update lead status) based on response intent.

## Inputs

| Input                 | Source                  | Required | Validation              |
| --------------------- | ----------------------- | -------- | ----------------------- |
| Response Email        | MailRelay/IMAP Inbox    | Yes      | Valid email format      |
| Original Outreach     | Outreach_Tracking Sheet | Yes      | Match by thread/email   |
| Lead Data             | Leads_Master Sheet      | Yes      | Lead exists in system   |
| Classification Config | System_Config Sheet     | No       | Custom categories/rules |

## Skills

| Skill                 | Purpose                             | Trigger              |
| --------------------- | ----------------------------------- | -------------------- |
| `inbox-monitor`       | Poll for new responses              | Every 15 minutes     |
| `response-matcher`    | Match reply to original outreach    | New email detected   |
| `llm-classifier`      | Classify response intent            | After matching       |
| `sentiment-analyzer`  | Determine positive/neutral/negative | Post-classification  |
| `action-executor`     | Execute automated actions           | After classification |
| `notification-sender` | Alert humans for hot leads          | Real-time            |
| `sheet-updater`       | Update Responses & Leads sheets     | After processing     |

## Response Classifications

| Category        | Definition                              | Automated Action                           |
| --------------- | --------------------------------------- | ------------------------------------------ |
| INTERESTED      | Wants to learn more or schedule meeting | Cancel follow-ups, alert human, mark "hot" |
| MEETING_REQUEST | Explicitly asks for call/meeting        | Cancel follow-ups, alert human, mark "hot" |
| MORE_INFO       | Requests additional information         | Cancel auto follow-ups, queue human reply  |
| NOT_NOW         | Interested but bad timing               | Cancel follow-ups, schedule re-engagement  |
| NOT_INTERESTED  | Clear rejection                         | Cancel all, mark "closed_lost"             |
| OUT_OF_OFFICE   | Auto-reply/vacation                     | Extract return date, reschedule follow-up  |
| UNSUBSCRIBE     | Wants to stop receiving emails          | Cancel all, suppress, mark "unsubscribed"  |
| UNCLEAR         | Cannot determine intent                 | Flag for human review                      |

## Outputs

| Output             | Format         | Destination                        |
| ------------------ | -------------- | ---------------------------------- |
| Classification Log | JSON           | Google Sheet: `Responses`          |
| Lead Status Update | String         | Google Sheet: `Leads_Master`       |
| Follow-Up Cancels  | Status Updates | Google Sheet: `Follow_Up_Queue`    |
| Human Alerts       | Notification   | Configured channels (email/Slack)  |
| Analytics Update   | Metrics        | Google Sheet: `Campaign_Analytics` |

## Edge Cases

| Scenario                | Handling                                           |
| ----------------------- | -------------------------------------------------- |
| Cannot match to lead    | Log to orphan responses, attempt fuzzy matching    |
| Classification unclear  | Flag for human review, cancel automated follow-ups |
| Multiple responses      | Process latest, archive others as "superseded"     |
| Auto-reply loop         | Detect and suppress after 2 exchanges              |
| Malicious/spam response | Mark as spam, do not process, block sender         |
| Empty response          | Log as "acknowledgment", continue follow-ups       |
| Attachment only         | Request clarification, queue for human             |

## Success Criteria

- [ ] Responses detected within 15 minutes of receipt
- [ ] 95%+ of responses correctly matched to original outreach
- [ ] Classification accuracy >90% (human-verified sample)
- [ ] Hot leads (INTERESTED/MEETING_REQUEST) alerted within 5 minutes
- [ ] Follow-ups cancelled automatically on any response
- [ ] Unsubscribes processed and suppressed immediately
- [ ] All responses logged in Responses sheet with full metadata
- [ ] Human review queue < 5% of total responses

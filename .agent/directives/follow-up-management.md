# Directive: Follow-Up Management

## Goal

Manage automated follow-up sequences by scheduling, queueing, and sending follow-up emails based on engagement patterns and response status.

## Inputs

| Input             | Source                  | Required | Validation                 |
| ----------------- | ----------------------- | -------- | -------------------------- |
| Original Outreach | Outreach_Tracking Sheet | Yes      | status="sent"              |
| Lead Status       | Leads_Master Sheet      | Yes      | Not responded/unsubscribed |
| Engagement Data   | Outreach_Tracking Sheet | Yes      | Open/click tracking        |
| Schedule Config   | System_Config Sheet     | Yes      | Follow-up intervals set    |

## Skills

| Skill                 | Purpose                    | Trigger               |
| --------------------- | -------------------------- | --------------------- |
| `queue-processor`     | Process pending follow-ups | Daily at 8AM          |
| `response-checker`    | Check if lead replied      | Before each follow-up |
| `engagement-analyzer` | Check opens/clicks         | Queue processing      |
| `follow-up-gen`       | Generate follow-up content | If proceeding         |
| `mailrelay-sender`    | Send follow-up emails      | Approved sends        |
| `queue-scheduler`     | Schedule next follow-ups   | After send            |
| `sheet-manager`       | Update queue and tracking  | Continuous            |

## Outputs

| Output          | Format                | Destination                       |
| --------------- | --------------------- | --------------------------------- |
| Follow-Up Queue | Queue Entries         | Google Sheet: `Follow_Up_Queue`   |
| Sent Follow-Ups | Log Entries           | Google Sheet: `Outreach_Tracking` |
| Cancelled Queue | Status Updates        | Google Sheet: `Follow_Up_Queue`   |
| Lead Status     | "nurture"/"contacted" | Google Sheet: `Leads_Master`      |

## Follow-Up Sequence

| Follow-Up | Timing            | Strategy          | Tone                 |
| --------- | ----------------- | ----------------- | -------------------- |
| #1        | +3 business days  | "Checking in"     | Helpful, add value   |
| #2        | +7 business days  | "Different angle" | New hook, case study |
| #3        | +14 business days | "Breakup email"   | Urgency, last chance |

## Edge Cases

| Scenario             | Handling                                         |
| -------------------- | ------------------------------------------------ |
| Lead replies         | Cancel all pending follow-ups immediately        |
| Lead unsubscribes    | Cancel all, add to suppression list              |
| Email bounced        | Cancel follow-ups, mark lead invalid             |
| No opens on previous | Delay follow-up by 2 days (possible spam folder) |
| Queue limit reached  | Prioritize by lead score, defer lower scores     |
| Follow-up 3 complete | Mark as "nurture", schedule re-engagement in 90d |
| Out of office reply  | Extract return date, reschedule after return     |

## Success Criteria

- [ ] Follow-ups scheduled automatically after initial send
- [ ] Queue processed daily for due follow-ups
- [ ] Responses detected and cancel follow-ups within 1 hour
- [ ] Follow-up 1, 2, 3 sent at correct intervals
- [ ] No emails sent to unsubscribed/bounced leads
- [ ] Leads moved to "nurture" after follow-up 3 (no response)
- [ ] Out-of-office leads rescheduled appropriately

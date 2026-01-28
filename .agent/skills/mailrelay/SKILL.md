# Skill: Email Sender (MailRelay)

## Trigger

- Auto: Outreach workflow (approved leads).
- Manual: `/send-mail {to} {template}`

## Inputs

| Param     | Type    | Required | Default |
| --------- | ------- | -------- | ------- |
| to_email  | string  | Yes      | -       |
| subject   | string  | Yes      | -       |
| html_body | string  | Yes      | -       |
| tracking  | boolean | No       | true    |

## Outputs

| Field      | Type   | Description        |
| ---------- | ------ | ------------------ |
| message_id | string | ID for tracking    |
| status     | string | sent/queued/failed |

## Cost

Free tier: 75,000 emails/month.

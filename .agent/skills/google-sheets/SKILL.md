# Skill: Data Management (Google Sheets)

## Trigger

- Auto: Data pipeline (storage/retrieval).
- Manual: `/sheet-read`, `/sheet-write`

## Inputs

| Param     | Type   | Required | Default           |
| --------- | ------ | -------- | ----------------- |
| operation | enum   | Yes      | read/write/append |
| range     | string | Yes      | -                 |
| data      | array  | No       | -                 |

## Outputs

| Field         | Type  | Description      |
| ------------- | ----- | ---------------- |
| data          | array | Rows returned    |
| updated_cells | int   | Count of changes |

## Cost

Free (API quotas apply).

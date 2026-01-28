# Skill: Search (Serper)

## Trigger

- Auto: User requests new leads or market research.
- Manual: `/search {query}`

## Inputs

| Param       | Type   | Required | Default |
| ----------- | ------ | -------- | ------- |
| query       | string | Yes      | -       |
| location    | string | No       | -       |
| num_results | int    | No       | 10      |

## Outputs

| Field        | Type  | Description                                   |
| ------------ | ----- | --------------------------------------------- |
| results      | array | List of search results (title, link, snippet) |
| credits_used | int   | Cost calculation                              |

## Cost

1 credit per search. Free tier: 100/day.

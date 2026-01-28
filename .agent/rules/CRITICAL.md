# Rule: Critical Security & Compliance

P1 Priority - Never Override

## MUST

- Never commit secrets (API keys, tokens, passwords) to git.
- Validate all inputs using strict schemas.
- Sanitize all outputs to prevent XSS/Injection.
- Follow the Principle of Least Privilege.

## MUST NOT

- Bypass authentication or authorization checks.
- Log sensitive data (PII, secrets, payment info).

## EXCEPTIONS

- None.

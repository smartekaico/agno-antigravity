# Rule: Version Control & Branching

P2 Priority

## MUST

- Use **Phase-Based Branching** to mirror SOP execution.
  - `main`: Validated, stable code.
  - `feat/phase-{n}-{name}`: Active development.
- **Atomic Commits**: Each commit should represent a single logical change.
- **Merge Criteria**:
  - All tests must pass.
  - Verification checklist complete.
  - No linting errors.

## SHOULD

- Use descriptive commit messages (e.g., "feat: implement serper client").
- Delete feature branches after merging.

## MUST NOT

- Commit directly to `main` without verification.
- Force push to shared branches.

# Security Policy

## Reporting

Email `Petar.Radanliev@newcastle.ac.uk` with steps to reproduce. Do not open public issues for sensitive flaws.

## Scope

Lab code under `src/`, `run_LangChain/`, `week-*`, and homework templates. All prompts and fixtures are synthetic.

## Safety by Design

- **Isolated, offline only**: no live network access, no real credentials, no private data. Demos use local fixtures (`data/adversarial_prompts.json`).
- Assume any AI-generated code is untrusted until verified.
- Do not use these labs against external systems.

## Disclosure

Acknowledgement within 48h, fix coordinated case-by-case.

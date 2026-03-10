Task 4 — Hardening & Governance Playbook (deliverable)

Minimum required controls (students must implement or describe):
1. Input validation examples: showcase Great Expectations checks for ingestion schema
2. Access control: RBAC policies (minimal example for Airflow + Feature Store)
3. Versioning: how to use content-addressed artifact naming or signed feature snapshots
4. Monitoring: propose telemetry rules (feature drift thresholds, sudden class distribution change)
5. Recovery: recommended containment and retraining thresholds; rollback mechanism

Deliverable:
- `hardening_playbook.md` with concrete commands/config snippets and at least one small demo script (`hardening_demo.py`) that runs a Great Expectations check on `poisoned_stream.jsonl`.

Task 3 — Red Team: DAG hijack & API fuzzing demo

Objective:
- Provide a minimal demonstration showing how an attacker could hijack an Airflow DAG or spoof a Kafka/HTTP ingestion source.
- Provide a short redteam_report.md describing the exploit vector, proof-of-concept commands, and recommended mitigations.

Contents:
- `spoof_ingest.py` — script that simulates a malicious upstream source sending corrupted events.
- `dag_hijack.md` — step-by-step on how a misconfigured DAG with permissive connections could be abused.

Safety:
- All demos must be run in an isolated environment. Do not run against production systems.

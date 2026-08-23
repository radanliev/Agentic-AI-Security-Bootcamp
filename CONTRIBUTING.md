# Contributing to Agentic AI Security Demos (Bootcamp)

## Setup

```bash
git clone https://github.com/radanliev/Agentic-AI-Security-Demos.git
cd Agentic-AI-Security-Demos
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
# optional UI: streamlit run app.py
```

Labs are offline; no external API keys required for core exercises.

## How to Contribute

- Fix lab instructions, starter code, or fixtures.
- Improve adversarial prompt sets or observability notebooks.
- Add homework solutions as examples (keep student TODOs intact).

## Workflow

1. Fork → branch.
2. Run affected lab checks locally (`pytest` or `streamlit` dry-run).
3. Keep synthetic-only guarantee; no added network calls.
4. Submit PR with description and tested steps.

## Style

- Python 3.10+, clear exercise objectives, 200–500 word write-ups.
- Keep `src/agent.py`, `src/memory.py` interfaces stable across weeks.

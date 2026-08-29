# Codeforces Journey

This repository tracks a personal Codeforces learning journey.

## Goals
- Track problem-solving progress
- Monitor contest participation
- Keep a running log of solved problems and rating growth
- Automate updates from Codeforces data

## Structure
- `scripts/update_journey.py` updates the journey data
- `.github/workflows/sync.yml` runs the sync automatically

## Local usage

```bash
python scripts/update_journey.py
```

This script can be adapted to fetch your Codeforces profile and update a progress summary or markdown report.

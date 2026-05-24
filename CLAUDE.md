# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A personal CV/portfolio website built with Python Dash (Plotly), deployed to Azure Web App via GitHub Actions and Docker. Live at https://yscv.azurewebsites.net.

## Commands

```bash
# Install dependencies
poetry install

# Run locally (debug mode)
poetry run python app/app.py

# Run with explicit config
RUN_LOCATION=Local APP_HOST_LOCAL=127.0.0.1 APP_PORT=8050 poetry run python app/app.py

# Docker
docker build -t dashcv .
docker run -p 8047:8047 dashcv

# Tests (pytest configured, tests/ dir currently empty)
poetry run pytest
```

## Required Environment Variables

| Variable | Purpose |
|---|---|
| `DB_USERNAME`, `DB_PWD`, `DB_SERVER`, `DB_DATABASE` | Azure SQL Server credentials |
| `OPENAI_API_KEY` | OpenAI API key for CV assistant |
| `ASSISTANT_ID` | OpenAI Assistants API ID |
| `RUN_LOCATION` | `"Local"` or `"Docker"` (controls host/port and debug mode) |
| `APP_HOST_LOCAL`, `APP_HOST_DOCKER`, `APP_PORT` | Server binding config |

Use a `.env` file locally (already in `.gitignore`).

## Architecture

### Multi-page Dash Application

- **`app/app.py`**: Entry point. Initializes Dash with Bootstrap theming, global navbar, and footer. Registers multi-page routing via `dash.register_page()`.
- **`app/pages/`**: Each file is a self-contained page that calls `dash.register_page()` at import:
  - `home.py` — Bio and project overview
  - `cv.py` — Interactive Plotly timeline + ag-grid CV table
  - `skills.py` — Skills visualization with category filtering
  - `assistant.py` — OpenAI Assistants API chatbot for Q&A on CV content
- **`app/components/`**: Reusable UI components shared across pages
- **`app/utils/DbData.py`**: Connects to Azure SQL Server at startup via pymssql, loads `Cv.Cv` and `Cv.Skills` tables into pandas DataFrames used across pages
- **`app/assets/`**: Static files served automatically by Dash (CSS, images)

### Data Flow

Database → `DbData.py` (loaded once at startup) → pandas DataFrames → page-level Dash callbacks → Plotly figures / ag-grid tables

### Deployment

Push to `master` → GitHub Actions builds Docker image → pushes to ghcr.io → deploys to Azure Web App "yscv". Secrets: `GHCR_USERNAME`, `GHCR_TOKEN`, `AZURE_WEBAPP_PUBLISH_PROFILE`.

### Ports

- Local dev: `8050`
- Docker: `8047`

### Key Dependencies

- `dash`, `dash-bootstrap-components` — UI framework
- `plotly`, `pandas` — data visualization and processing
- `pymssql` — Azure SQL Server connection
- `openai` — CV assistant chatbot
- `py-plot-ge` — custom plotting library (installed from personal GitHub)

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

A centralised CRUD application to capture the global PyData community landscape: which meetup groups exist, where they are, and who organises them. The eventual vision includes provisioning resources per meetup (Google Groups, subdomains under pydata.org). Authentication/self-service is important for GDPR compliance so organisers can update or remove their own data.

The project is in its earliest stage — `main.py` is a placeholder and the architecture is not yet established.

## Package Manager

This project uses `uv`. Do not use `pip` directly.

```bash
uv add <package>          # add a dependency
uv add --dev <package>    # add a dev dependency
uv run <command>          # run a command in the managed environment
uv sync                   # install all dependencies
```

## Commands

```bash
uv run pytest             # run all tests
uv run pytest tests/path/to/test_file.py::test_name  # run a single test
uv run python main.py     # run the app
```

## Stack

- **Python 3.13**
- **FastAPI** — the chosen web framework for the CRUD API
- **pytest** + **hypothesis** — testing (hypothesis for property-based tests)

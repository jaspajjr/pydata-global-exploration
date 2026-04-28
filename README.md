# pydata-global-exploration

A centralised registry of PyData meetup groups, their locations, and the people who organise them.

## Vision

The PyData community lacks a single source of truth for who is running meetups, where, and under which organisations. This project builds the infrastructure to capture and organise that information — starting with a simple CRUD application, and eventually using it to provision resources for each group automatically (Google Groups, subdomain pages, and more).

## Planned scope

The initial application will support:

- Creating and managing meetup group records (name, location, organisation)
- Creating and managing organiser records linked to those groups
- Self-service authentication so organisers can update or remove their own data
- Downstream resource provisioning per group:
  - A Google Group for each meetup
  - A subdomain page (e.g. `manchester.pydata.org`, `new-york.pydata.org`)

## Data ownership

Because the app stores personal data about organisers, GDPR compliance is a first-class concern. Self-service authentication — where organisers log in and manage their own records — is the chosen approach to minimise administrative overhead and give individuals control over their data.

## Status

Early exploration. The shape of the application is still being defined.

## Setup

Requires Python 3.13 and [`uv`](https://docs.astral.sh/uv/).

```bash
uv sync             # install dependencies
uv run python main.py  # run the app
uv run pytest       # run tests
```

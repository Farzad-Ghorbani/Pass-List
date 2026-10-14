# Pass-List — image-based deployment

This repository is the image/Compose distribution for Pass-List. Installation does **not** build application code on the target server and does **not** require an installation script.

## Images

The GitHub Actions workflow publishes these private GHCR images:

- `ghcr.io/farzad-ghorbani/pass-list-web:v1.13.1-final`
- `ghcr.io/farzad-ghorbani/pass-list-cert-ops:v1.13.1-final`
- `ghcr.io/farzad-ghorbani/pass-list-nginx:v1.13.1-final`
- `ghcr.io/farzad-ghorbani/pass-list-init:v1.13.1-final`
- `ghcr.io/farzad-ghorbani/pass-list-postgres:16-alpine`

`pass-list-init` only prepares persistent paths and creates a temporary self-signed certificate when no certificate exists. It exits before the application starts. No Docker socket is mounted into the application.

## First installation

Copy `compose.yaml` and `.env.example` to the target server, then create `.env` from the example and replace every `CHANGE_ME` value.

Before the first start, set `PASSLIST_INITIAL_HOSTNAME` and `DJANGO_ALLOWED_HOSTS` to the real IP/hostname(s) that will be used to reach the panel.

Useful local commands for generating secrets (these commands are not installation scripts):

```bash
python3 -c 'import secrets; print(secrets.token_urlsafe(64))'   # DJANGO_SECRET_KEY
python3 -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())'  # PASSLIST_ENCRYPTION_KEY
python3 -c 'import secrets; print(secrets.token_urlsafe(48))'   # PASSLIST_OPS_TOKEN
python3 -c 'import secrets; print(secrets.token_urlsafe(32))'   # POSTGRES_PASSWORD
```

For a private GHCR package, authenticate Docker once on a connected machine/server:

```bash
docker login ghcr.io
```

Then installation is only:

```bash
docker compose up -d
```

The Compose stack automatically creates/prepares persistent directories under `PASSLIST_BASE_PATH` (default `/opt/pass-list`) through the `pass-list-init` image. It also creates a temporary self-signed certificate if `certs/pass-list.crt` and `certs/pass-list.key` do not already exist.

After the first successful login, change the Super Admin password. You may then clear `SUPERADMIN_PASSWORD` in `.env`; existing Super Admin data is never re-seeded or reset by container startup.

## Persistent data

Default persistent base path:

```text
/opt/pass-list
```

Important paths include PostgreSQL data, certificates, certificate backups, media/static files, audit/app logs, Nginx logs/runtime maps, and certificate staging.

### Critical recovery material

Back up the full persistent path **and** the deployment `.env`. In particular, `PASSLIST_ENCRYPTION_KEY` is required to decrypt secrets already stored in PostgreSQL. Losing the database encryption key makes encrypted secret values unrecoverable.

Never commit the real `.env`, TLS private keys, database backups, or exported production secrets to GitHub.

## TLS and hostnames

The first boot can use the temporary self-signed certificate. A Super Admin can later upload a PEM/KEY or PFX/P12 certificate from the TLS management page and manage active/primary hostnames from the Hostname & Domain Settings page.

`cert-ops` retains the production hardening fixes used by the tested deployment:

- certificate staging files are group-readable (`0640`) so the restricted helper can consume them;
- all Linux capabilities are dropped except `CHOWN`, which is required for `nginx -t` with the Nginx temporary directories;
- no Docker socket is exposed.

## Offline zones

The running application itself does not require Internet access. For a fully isolated zone, pull the GHCR images on a connected staging host, export them with `docker save`, transfer them to the isolated zone, and load them with `docker load`. Once the images exist locally, the same `compose.yaml` starts the stack without Internet access.

## Build source

The exact build source is stored under `source/parts/` as Base64 archive parts. GitHub Actions reconstructs `pass-list-v1.13.1-final-source.zip`, verifies it against `source/BUILD-SHA256.txt`, and only then builds the images.

The application code includes the production-tested Controller Value search filtering, Controller-scoped result columns, sticky/search-result table improvements, UI refinements, hostname management, blocked-access landing page, TLS management, and migrations through `core.0008`.


## Code knowledge graph (Graphify)

Graphify **0.9.90** is installed at project scope for Codex. The checked-in
`graphify-out/` snapshot maps the verified application source and supports code
queries. See [setup and rebuild instructions](tools/graphify/README.md).
The **Graphify code graph** GitHub Actions workflow publishes a refreshed HTML,
JSON and Markdown report artifact after relevant changes.

# Graphify for Pass-List

Graphify 0.9.90 (official PyPI package `graphifyy`) is the latest stable release
verified on 2026-10-14. This is a development tool; it is not a runtime service.
Upstream: https://github.com/Graphify-Labs/graphify/releases/tag/v0.9.90

## Install and rebuild

Use Python 3.12 and an isolated environment from the repository root:

```bash
python3 -m venv .venv-graphify
source .venv-graphify/bin/activate
python -m pip install -r tools/graphify/requirements.txt
graphify install --project --platform codex
bash tools/graphify/build.sh
graphify query "SecretRecord permissions"
```

The official Codex skill and reference files are checked into `.codex/skills/graphify/`.
The CLI must still be installed in each development environment. Codex invokes the
skill as `$graphify`. No global Codex configuration is changed by this project.

`prepare_source.py` reconstructs the source archive from `source/parts/`, verifies
`source/BUILD-SHA256.txt`, and replaces the disposable `graphify-source/` directory.
Never make permanent edits there: the source archive remains authoritative.
Graph source paths such as `app/core/models.py` are relative to `graphify-source/`.

The build uses local AST extraction only. It does not call an LLM or need API keys.
HTML templates, prose, CSS and other unsupported files are not semantically analyzed.
The extractor can omit files that it classifies as sensitive.

Outputs are `graphify-out/graph.json`, `graph.html`, `GRAPH_REPORT.md`, and
`SOURCE.json` (source checksum and tool version). The committed outputs are a
snapshot; compare SOURCE.json with source/BUILD-SHA256.txt before relying on them.
GitHub Actions rebuilds after relevant source/tool changes and uploads fresh
outputs as an artifact; it does not commit them back automatically.
After intentional source updates, rebuild and commit these four output files.

## Upgrade later

Check the official release and PyPI version, update `tools/graphify/requirements.txt`
to the new exact version, install that requirements file, then run:

```bash
graphify install --project --platform codex
bash tools/graphify/build.sh
```

Review and commit the refreshed skill, references, graph outputs and version pin.
The project-specific instructions at the top of AGENTS.md must be retained.

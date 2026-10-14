# Pass-List source layout

This repository distributes an archive-backed application. For this project,
rebuild the graph with `bash tools/graphify/build.sh` instead of `graphify update .`:
the helper verifies and reconstructs the source before indexing it. Graph node
paths are relative to `graphify-source/`, not the repository root. Do not edit
that disposable extracted directory as the permanent source of truth.

Install the CLI with `tools/graphify/requirements.txt` in an isolated environment.
Before using a committed graph, compare `graphify-out/SOURCE.json` source_sha256
with `source/BUILD-SHA256.txt`; rebuild if they differ. Use the local code-only
build by default. See `tools/graphify/README.md` for setup and upgrade commands.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- When graphify-out/graph.json exists, run `graphify query "<question>"` before your first grep, search or source-file read for a codebase question, and put this rule in every subagent prompt that explores code. Read raw files only for lines the graph or an earlier read already located. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
- A committed graphify-out/graph.json is rewritten whole on every build, so a large diff to it in a pull request is expected. Do not flag it as churn or suggest skipping the graph rebuild or its hooks.

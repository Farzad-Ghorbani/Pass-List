#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
python3 tools/graphify/prepare_source.py
graphify extract graphify-source --code-only --no-gitignore --max-workers 2 --out .
graphify cluster-only . --no-label
python3 - <<'PY'
import json
from pathlib import Path
root = Path('.')
graph = json.loads((root / 'graphify-out/graph.json').read_text())
if not graph['nodes'] or not graph['links']:
    raise SystemExit('Graph is empty')
provenance = {
    'graphify_version': graph['graph']['graphify_version'],
    'source_sha256': (root / 'source/BUILD-SHA256.txt').read_text().strip(),
    'source_root': 'graphify-source/',
    'mode': 'code-only; local AST; no LLM',
    'nodes': len(graph['nodes']),
    'edges': len(graph['links']),
}
(root / 'graphify-out/SOURCE.json').write_text(json.dumps(provenance, indent=2) + '\n')
print(json.dumps(provenance, indent=2))
PY

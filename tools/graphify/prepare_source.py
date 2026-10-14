"""Reconstruct the checksum-verified release source for local code analysis."""
import base64
import hashlib
import io
from pathlib import Path, PurePosixPath
import shutil
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "graphify-source"

def main():
    parts = sorted((ROOT / "source/parts").glob("part-*.b64"))
    if not parts:
        raise SystemExit("No source archive parts found")
    encoded = b"".join(p.read_bytes() for p in parts)
    data = base64.b64decode(b"".join(encoded.split()), validate=True)
    digest = hashlib.sha256(data).hexdigest()
    expected = (ROOT / "source/BUILD-SHA256.txt").read_text().strip()
    if digest != expected:
        raise SystemExit("Source SHA256 mismatch; refusing to extract")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = archive.infolist()
        roots = set()
        for member in members:
            path = PurePosixPath(member.filename)
            if path.is_absolute() or ".." in path.parts or "\\" in member.filename:
                raise SystemExit("Unsafe archive path")
            if stat.S_ISLNK(member.external_attr >> 16):
                raise SystemExit("Archive symlinks are not supported")
            roots.add(path.parts[0])
        if len(roots) != 1:
            raise SystemExit("Expected one release source directory")
        if DEST.is_symlink():
            raise SystemExit("Extraction destination must not be a symlink")
        if DEST.exists():
            shutil.rmtree(DEST)
        DEST.mkdir()
        for member in members:
            relative = PurePosixPath(member.filename).parts[1:]
            if not relative:
                continue
            target = DEST.joinpath(*relative)
            if member.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(archive.read(member))
    print(f"Verified source SHA256: {digest}")
    print("Source ready in graphify-source/")

if __name__ == "__main__":
    main()

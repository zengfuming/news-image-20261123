"""Write 23 November 2026's world news as one image to /output/entry.png.

The entry image is bundled in this repository as entry.png (a 1024x1024
newspaper front page). This program copies it to the output path, verifies
the copy byte-for-byte with SHA-256, and does nothing else: no network, no
randomness, so two runs write identical bytes.

Run: python3 main.py  (MAKEFUN_OUTPUT_DIR defaults to /output)
"""

import hashlib
import os
import shutil
import sys

CHUNK_SIZE = 65536
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(CHUNK_SIZE)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.png")

    shutil.copyfile(SOURCE, output_path)

    source_hash = sha256_of(SOURCE)
    output_hash = sha256_of(output_path)
    if source_hash != output_hash:
        print("copy verification failed: hashes differ", file=sys.stderr)
        return 1

    print("wrote {} (sha256 {})".format(output_path, output_hash))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

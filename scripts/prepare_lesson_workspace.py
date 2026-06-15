#!/usr/bin/env python3
"""Create a standard lesson-to-audio workspace."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "lesson.md": "# Lesson\n\nPaste the original lesson plan here.\n",
    "pages.md": "",
    "narration.md": "",
    "full.txt": "",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Create standard lesson workflow files.")
    parser.add_argument("directory", help="Target lesson directory")
    args = parser.parse_args()

    target = Path(args.directory).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    for name, content in FILES.items():
        path = target / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            print(f"created {path}")
        else:
            print(f"exists  {path}")

    print("\nExpected generated audio files:")
    print(target / "audio.wav")
    print(target / "voice.mp3")


if __name__ == "__main__":
    main()

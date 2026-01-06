#!/usr/bin/env python3

import argparse
import json
import os
from pathlib import Path
import sys

DEFAULT_STRUCTURE = {
    "000-Inbox": [],
    "100-Work": [
        "101-Calendar",
        "102-Projects",
        "103-Operation"
    ],
    "200-Learning": [
        "201-Reading",
        "202-Computer",
        "203-Language"
    ],
    "300-Life": [
        "301-Travel",
        "302-Finance",
        "303-Hobbies"
    ],
    "900-Resources": [
        "901-Templates",
        "902-Images",
        "903-Plugins"
    ]
}


def load_structure_from_file(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            else:
                print(f"Config file {path} must contain a JSON object at top level.")
                sys.exit(1)
    except Exception as e:
        print(f"Failed to load config file {path}: {e}")
        sys.exit(1)


def create_folders(base: Path, structure, gitkeep: bool = False):
    """Recursively create folders described by `structure` under `base`.
    `structure` is expected to be a dict where keys are folder names and values
    are lists of either string names or nested dicts for deeper nesting.
    """
    if not isinstance(structure, dict):
        raise TypeError("structure must be a dict")

    for name, children in structure.items():
        folder_path = base / name
        folder_path.mkdir(parents=True, exist_ok=True)
        if gitkeep:
            (folder_path / ".gitkeep").write_text("", encoding="utf-8")
        # children can be a list of strings or dicts
        if isinstance(children, list):
            for child in children:
                if isinstance(child, str):
                    (folder_path / child).mkdir(parents=True, exist_ok=True)
                    if gitkeep:
                        (folder_path / child / ".gitkeep").write_text("", encoding="utf-8")
                elif isinstance(child, dict):
                    create_folders(folder_path, child, gitkeep=gitkeep)
                else:
                    print(f"Ignored unsupported child type: {type(child)} in {name}")
        elif isinstance(children, dict):
            create_folders(folder_path, children, gitkeep=gitkeep)
        else:
            # if children is empty or None, continue
            continue


def main():
    parser = argparse.ArgumentParser(description="Create a standardized folder structure for an Obsidian vault.")
    parser.add_argument("--path", "-p", default=".", help="Target path for the Obsidian vault (default: current directory)")
    parser.add_argument("--config", "-c", help="Path to a JSON configuration file describing the folder structure")
    parser.add_argument("--gitkeep", action="store_true", help="Create a .gitkeep file inside each folder so Git can track empty dirs")
    args = parser.parse_args()

    base = Path(args.path).expanduser().resolve()
    if not base.exists():
        base.mkdir(parents=True, exist_ok=True)

    if args.config:
        config_path = Path(args.config)
        if not config_path.exists():
            print(f"Config file {config_path} does not exist.")
            sys.exit(1)
        structure = load_structure_from_file(config_path)
    else:
        # try to load default_structure.json next to the script if present
        script_dir = Path(__file__).resolve().parent
        default_cfg = script_dir / "default_structure.json"
        if default_cfg.exists():
            structure = load_structure_from_file(default_cfg)
        else:
            structure = DEFAULT_STRUCTURE

    create_folders(base, structure, gitkeep=args.gitkeep)

    print(f"Folder structure created at: {base}")


if __name__ == "__main__":
    main()

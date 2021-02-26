"""Create apt packages from a file list"""
import shutil
from pathlib import Path
from typing import List

from dvdp.utils import system


def parse_log_for_paths(log_file: str):
    if system.is_windows():
        raise Exception('Cannot parse log on a windows system.')
    paths = []
    with open(log_file, 'r') as file:
        for line in file:
            splitted = line.split('/', maxsplit=1)
            if len(splitted) == 2:
                path_candidate = Path('/' + splitted[1])
                if path_candidate.exists():
                    paths.append(path_candidate)
    return paths


def create_package_tree(destination: Path, paths: List[Path]):
    destination.mkdir(parents=True, exist_ok=True)
    for path in paths:
        dest_sub = destination / path
        dest_sub.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, dest_sub)


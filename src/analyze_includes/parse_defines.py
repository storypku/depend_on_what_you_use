import json
from pathlib import Path
from typing import List

from src.analyze_includes.parse_source import IgnoredIncludes
from src.analyze_includes.std_header import STD_HEADER

DEFINES_KEY = "defines"


def parse_defines(headers_info_file: Path) -> List[str]:
    with open(headers_info_file, encoding="utf-8") as fin:
        loaded = json.load(fin)
        return loaded["self"][DEFINES_KEY]

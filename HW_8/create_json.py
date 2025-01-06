from pathlib import Path

from pathlib import Path
from typing import TextIO
import json


def create_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f_2:
        json.dump(file_data, f_2, ensure_ascii=False, indent=2)
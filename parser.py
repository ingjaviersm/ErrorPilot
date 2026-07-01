import re
from pathlib import Path
from typing import List

from models import LogEntry
from normalizer import LogNormalizer


class LogParser:
    """
    Parser para logs de PHP.
    Primera versión: procesa eventos de una sola línea.
    """

    LOG_PATTERN = re.compile(
        r'^\[(?P<timestamp>.*?)\]\s+PHP\s+(?P<level>Warning|Notice|Fatal error|Parse error|Deprecated|Error):\s+'
        r'(?P<message>.*?)\s+in\s+(?P<file>.*?)\s+on\s+line\s+(?P<line>\d+)$'
    )

    def __init__(self):
        self.normalizer = LogNormalizer()

    def parse_file(self, log_file: str) -> List[LogEntry]:
        entries: List[LogEntry] = []

        path = Path(log_file)

        with path.open("r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                entry = self.parse_line(line.rstrip())

                if entry is not None:
                    entries.append(entry)

        return entries

    def parse_line(self, line: str):

        match = self.LOG_PATTERN.match(line)

        if not match:
            return None

        file_path = match.group("file")
        message = match.group("message")

        return LogEntry(
            timestamp=match.group("timestamp"),
            level=match.group("level"),
            message=message,
            normalized_message=self.normalizer.normalize(message),
            file_path=file_path,
            file_name=Path(file_path).name,
            line=int(match.group("line")),
            raw=line
        )
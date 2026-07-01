from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LogEntry:
    timestamp: Optional[str]
    level: str
    message: str
    normalized_message: str
    file_path: Optional[str]
    file_name: Optional[str]
    line: Optional[int]
    raw: str
    stacktrace: List[str] = field(default_factory=list)
from dataclasses import dataclass, field
from typing import Dict, List

from models import LogEntry


@dataclass
class Summary:
    total_events: int = 0
    first_event: str = ""
    last_event: str = ""

    levels: Dict[str, int] = field(default_factory=dict)
    priorities: Dict[str, int] = field(default_factory=dict)


@dataclass
class ProblemSummary:
    message: str
    priority: str
    count: int


@dataclass
class SpecificError:
    message: str
    file_name: str
    line: int
    count: int


@dataclass
class FileSummary:
    file_name: str
    total_events: int
    score: int
    problems: Dict[str, int]


@dataclass
class AnalysisResult:
    summary: Summary

    normalized_problems: List[ProblemSummary] = field(default_factory=list)

    specific_errors: List[SpecificError] = field(default_factory=list)

    files: List[FileSummary] = field(default_factory=list)

    entries: List[LogEntry] = field(default_factory=list)
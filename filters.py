from typing import List, Optional

from models import LogEntry


class LogFilters:

    def apply(
        self,
        entries: List[LogEntry],
        level: Optional[str] = None,
        file: Optional[str] = None,
        contains: Optional[str] = None
    ) -> List[LogEntry]:

        filtered_entries = entries

        if level is not None:
            filtered_entries = [
                entry for entry in filtered_entries
                if entry.level.lower() == level.lower()
            ]

        if file is not None:
            file_filter = file.lower()

            filtered_entries = [
                entry for entry in filtered_entries
                if (
                    entry.file_name is not None
                    and file_filter in entry.file_name.lower()
                ) or (
                    entry.file_path is not None
                    and file_filter in entry.file_path.lower()
                )
            ]

        if contains is not None:
            contains_filter = contains.lower()

            filtered_entries = [
                entry for entry in filtered_entries
                if contains_filter in entry.message.lower()
                or contains_filter in entry.normalized_message.lower()
            ]

        return filtered_entries
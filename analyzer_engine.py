from collections import Counter, defaultdict
from typing import List

from analysis_models import (
    AnalysisResult,
    Summary,
    ProblemSummary,
    SpecificError,
    FileSummary
)
from models import LogEntry
from priority import ErrorPriority


class AnalyzerEngine:

    def analyze(self, entries: List[LogEntry]) -> AnalysisResult:

        priority = ErrorPriority()

        summary = Summary()

        summary.total_events = len(entries)

        if entries:
            summary.first_event = entries[0].timestamp
            summary.last_event = entries[-1].timestamp

        level_counter = Counter()
        priority_counter = Counter()

        normalized_counter = Counter()
        specific_counter = Counter()

        file_counter = Counter()
        file_problem_counter = defaultdict(Counter)
        file_priority_counter = defaultdict(Counter)

        priority_weight = {
            "CRITICO": 100,
            "ALTO": 20,
            "MEDIO": 5,
            "BAJO": 1
        }

        for entry in entries:

            entry_priority = priority.get_priority(
                entry.level,
                entry.normalized_message
            )

            level_counter[entry.level] += 1

            priority_counter[entry_priority] += 1

            normalized_counter[
                (
                    entry.normalized_message,
                    entry_priority
                )
            ] += 1

            specific_counter[
                (
                    entry.message,
                    entry.file_name,
                    entry.line
                )
            ] += 1

            file_counter[entry.file_name] += 1

            file_problem_counter[
                entry.file_name
            ][entry.normalized_message] += 1

            file_priority_counter[
                entry.file_name
            ][entry_priority] += 1

        summary.levels = dict(level_counter)
        summary.priorities = dict(priority_counter)

        result = AnalysisResult(
            summary=summary,
            entries=entries
        )

        #
        # Problemas normalizados
        #

        for (
            message,
            priority_name
        ), count in normalized_counter.most_common():

            result.normalized_problems.append(

                ProblemSummary(

                    message=message,

                    priority=priority_name,

                    count=count
                )

            )

        #
        # Errores específicos
        #

        for (
            message,
            file_name,
            line
        ), count in specific_counter.most_common():

            result.specific_errors.append(

                SpecificError(

                    message=message,

                    file_name=file_name,

                    line=line,

                    count=count

                )

            )

        #
        # Archivos
        #

        for file_name, total in file_counter.items():

            score = 0

            for (
                priority_name,
                quantity
            ) in file_priority_counter[file_name].items():

                score += quantity * priority_weight.get(priority_name, 1)

            score += len(file_problem_counter[file_name]) * 50

            result.files.append(

                FileSummary(

                    file_name=file_name,

                    total_events=total,

                    score=score,

                    problems=dict(file_problem_counter[file_name])

                )

            )

        result.files.sort(
            key=lambda x: x.score,
            reverse=True
        )

        return result
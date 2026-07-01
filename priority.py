class ErrorPriority:
    """
    Calcula prioridad de corrección según severidad y tipo de error.
    """

    PRIORITY_CRITICAL = "CRITICO"
    PRIORITY_HIGH = "ALTO"
    PRIORITY_MEDIUM = "MEDIO"
    PRIORITY_LOW = "BAJO"

    def get_priority(self, level: str, normalized_message: str) -> str:

        if level == "Fatal error":
            return self.PRIORITY_CRITICAL

        if normalized_message in [
            "Allowed memory size of 134217728 bytes exhausted",
        ]:
            return self.PRIORITY_CRITICAL

        if normalized_message in [
            "Attempt to read property on null",
            "Call to a member function on null",
        ]:
            return self.PRIORITY_HIGH

        if normalized_message in [
            "Undefined array key",
            "Undefined property",
            "Undefined variable",
            "Trying to access array offset on value of type bool",
            "Trying to access array offset on value of type null",
            "foreach() argument must be of type array|object, null given",
        ]:
            return self.PRIORITY_MEDIUM

        return self.PRIORITY_LOW
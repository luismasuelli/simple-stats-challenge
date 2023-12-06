from .stats import Stats


class Capture:
    """
    Captures numbers between 0 and 999. Other numbers will NOT be
    allowed in this version.
    """

    MAX_VALUE = 1000

    def __init__(self):
        self._collected = [0] * self.MAX_VALUE

    def add(self, value: int):
        """
        Collects a new value (it must be in the valid range).
        :param value: The value to add.
        """

        if not isinstance(value, int) or value not in range(self.MAX_VALUE):
            raise ValueError("Invalid value")
        self._collected[value] += 1

    def build_stats(self):
        """
        Builds a new stats object, passing the collected statistics.
        :return: The stats object.
        """

        return Stats(self._collected)

from typing import List


class Stats:
    """
    The stats object. It takes a histogram and lets the users
    make queries over the ranges of values.
    """

    @staticmethod
    def _make_cumulative_histogram(histogram: List[int]) -> List[int]:
        """
        Builds the cumulative histogram CH, where CH[i] == sum(histogram[:i+1]).

        Notice how this method does NOT have a complexity on the number of
        underlying related elements but, instead, on the range of allowed
        values (which is constant: the size of the histogram).

        :param histogram: The flat histogram to build the cumulative one from.
        :return: The cumulative histogram.
        """

        # Ok, the faster solution would be to use numpy's cumsum.
        # But it is against the rules to use those pre-implemented
        # tools, so let's go with the slower, but fully developed,
        # algorithm.

        total_count = 0
        cumulative_histogram = []
        for value in histogram:
            total_count += value
            cumulative_histogram.append(total_count)
        return cumulative_histogram

    def __init__(self, histogram: List[int]):
        """
        Builds the instance from the histogram (constant size) instead of
        building it from the collected elements.
        :param histogram: The histogram to build the stats from.
        """

        self._cummulative_histogram = Stats._make_cumulative_histogram(histogram)
        self._histogram_size = len(histogram)
        self._max_value = self._histogram_size - 1

    def less(self, value: int) -> int:
        """
        Returns the number of elements that are lower than the provided value.
        :param value: The value to test against.
        :return: The count of lower values.
        """

        if value <= 0:
            return 0
        elif value > self._histogram_size:
            return self._cummulative_histogram[-1]
        else:
            return self._cummulative_histogram[value - 1]

    def greater(self, value: int) -> int:
        """
        Returns the number of elements that are greater than the provided value.
        :param value: The value to test against.
        :return: The count of greater values.
        """

        all_elements = self._cummulative_histogram[-1]
        if value < 0:
            return all_elements
        elif value >= self._max_value:
            return 0
        else:
            return all_elements - self._cummulative_histogram[value]

    def between(self, start: int, end: int) -> int:
        """
        Returns the number of elements that are between
        :param start: The minimum element in the range (inclusive).
        :param end: The maximum element in the range (inclusive).
        :return: The count of values in the range.
        """

        # First, check the boundaries' validity and also
        # check the trivial boundaries.
        if start > end:
            raise ValueError("The start index must not be greater than the end index")
        elif start > self._max_value:
            return 0
        elif end < 0:
            return 0

        end = min(end, self._max_value)
        if start <= 0:
            return self._cummulative_histogram[end]
        else:
            return self._cummulative_histogram[end] - self._cummulative_histogram[start - 1]

from .capture import Capture


def _add_elements(capture: Capture, *elements):
    """
    Adds a set of elements to the capture object.
    :param capture: The capture object.
    :param elements: The elements to add.
    """

    for element in elements:
        capture.add(element)

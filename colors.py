from enum import Enum

END = '\033[0m'

class Colors(Enum):
    """
    Utility class for styling terminal text with ANSI escape codes.
    """
    LOSS = '\033[31m'
    WIN = '\033[32m'
    DRAW = '\033[33m'
    WARNING = '\033[91m'
    INFO = '\033[34m'


def style(string: str, theme: Colors) -> str:
    """
    Apply a given style to a string.
    Args:
        string (str): The text to style.
        theme (Colors): The name of the style.
    Returns:
        str: The styled text.
    """
    try:
        return f"{theme.value}{string}{END}"
    except:
        return f"Style '{style}' is not defined. Available styles: {', '.join(Colors._member_names_)}"
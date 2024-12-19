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

    @staticmethod
    def style(string: str, style: str) -> str:
        """
        Apply a given style to a string.
        Args:
            string (str): The text to style.
            style (str): The name of the style (LOSS, WIN, DRAW, WARNING, INFO).
        Returns:
            str: The styled text.
        """
        try:
            return f"{Colors[style.upper()].value}{string}{END}"
        except:
            return f"Style '{style}' is not defined. Available styles: {', '.join(Colors._member_names_)}"
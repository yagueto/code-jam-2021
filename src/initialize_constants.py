class Constants:
    """Class for managing constants required in the application."""

    def __init__(self, stdscr: 'curses.windows') -> None:  # noqa: F821
        """Initialized constants to be used in the application"""
        self.MAX_Y, self.MAX_X = stdscr.getmaxyx()
        self.CENTER_Y, self.CENTER_X = self.MAX_Y // 2, self.MAX_X // 2

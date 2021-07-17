from typing import List


class Menu:
    """For handling menus in the application"""

    def __init__(self, options: List[str], default: int = 0,
                 padding: int = 1, align: bool = False) -> None:

        if align:
            max_ = max([len(x) for x in options])
            self.options = [x.center(max_) for x in options]

        self.options = [x.center(len(x) + 2 * padding) for x in self.options]
        self.current = default

    def dec(self) -> None:
        """Moves the current selection one step down"""
        if (self.current == len(self.options)-1):
            self.current = 0
        else:
            self.current += 1

    def inc(self) -> None:
        """Moves the current selection one step up"""
        if (self.current == 0):
            self.current = len(self.options)-1
        else:
            self.current -= 1

    def current_elem(self) -> str:
        """Returns the currently selected item `str`"""
        return self.options[self.current]


def draw_box(stdscr: 'curses.window', y: int, x: int, text: str, padding: int = 1) -> None:  # noqa: F821
    """Draws a box around the given text in stdscr"""
    text = [f"┌{'─'*(len(text)+2*padding)}┐", f"│{' '*padding}{text}{' '*padding}│", f"└{'─'*(len(text)+2*padding)}┘"]
    for index, text in enumerate(text):
        stdscr.insstr(y + index, x, text)


def center_multiline_str(string: str, x_max: int) -> str:
    """Centers a multiline string according to the given x_max value"""
    split = string.splitlines()
    return "\n".join([x.center(x_max) for x in split])

# if __name__ == "__main__":
#     print(center_multiline_str("hello\nhow are you\nthis is", 10))

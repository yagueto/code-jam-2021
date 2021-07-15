import curses

from utils.utils import draw_box


def difficulty_level(stdscr: 'curses.window', CONSTANTS: 'CONSTANTS') -> None:  # noqa: F821
    """Function which runs when `difficulty` option is selected.

    Modify this function for chaning `difficulty` option screen.
    """
    stdscr.clear()

    text = "This is the difficulty menu!"
    draw_box(stdscr, CONSTANTS.CENTER_Y, CONSTANTS.CENTER_X - len(text) // 2, text, padding=2)

    stdscr.insstr(CONSTANTS.MAX_Y - 5, CONSTANTS.MAX_X - 20, " Back ", curses.A_REVERSE)

    while True:
        key = stdscr.getch()
        if key in [10, 13]:
            break

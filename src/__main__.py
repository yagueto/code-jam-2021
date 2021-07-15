import curses
from curses import textpad

from initialize_constants import Constants
from Screens import difficulty_level
from utils.utils import Menu


def main_menu(stdscr: curses.window, default: int = 0) -> None:
    """Main menu screen of the app."""
    stdscr.clear()
    stdscr.nodelay(1)
    curses.mousemask(0)
    stdscr.timeout(1)

    menu = Menu(options=["Play", "Difficulty", "Exit"], default=default)
    box_dim = [[2, 3], [CONSTANTS.MAX_Y-2, CONSTANTS.MAX_X-3]]

    while True:

        for index, text in enumerate(menu.options):
            if index == menu.current:
                stdscr.insstr(CONSTANTS.CENTER_Y + index, CONSTANTS.CENTER_X, text, curses.A_REVERSE)
                continue
            stdscr.insstr(CONSTANTS.CENTER_Y + index, CONSTANTS.CENTER_X, text)

        textpad.rectangle(stdscr, box_dim[0][0], box_dim[0][1], box_dim[1][0], box_dim[1][1])

        stdscr.refresh()
        key = stdscr.getch()

        if (key == curses.KEY_UP):
            menu.inc()
        elif (key == curses.KEY_DOWN):
            menu.dec()

        if key in [10, 13]:
            if menu.current == 2:
                return
            elif menu.current == 1:
                difficulty_level(stdscr, CONSTANTS)

        stdscr.clear()


def main(stdscr: curses.window) -> None:
    """Starts the application and initializes the global constants"""
    global CONSTANTS
    CONSTANTS = Constants(stdscr)
    curses.curs_set(0)

    main_menu(stdscr)


if __name__ == "__main__":
    exit(curses.wrapper(main))

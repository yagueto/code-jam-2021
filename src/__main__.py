import curses

from initialize_constants import Constants
from Screens import main_menu


def main(stdscr: curses.window) -> None:
    """Starts the application and initializes the global constants"""
    global CONSTANTS
    CONSTANTS = Constants(stdscr)
    curses.curs_set(0)

    main_menu(stdscr, CONSTANTS=CONSTANTS)


if __name__ == "__main__":
    exit(curses.wrapper(main))

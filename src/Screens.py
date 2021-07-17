import curses
from curses import textpad

from utils.utils import Menu, draw_box


def difficulty_level(stdscr: curses.window, CONSTANTS: 'CONSTANTS') -> str:  # noqa: F821
    """Function which runs when `difficulty` option is selected.

    Modify this function for chaning `difficulty` option screen.
    """
    menu = Menu(options=["Easy", "Medium", "Hard"], default=1, align=True)

    box_dim = [[4, 3], [CONSTANTS.MAX_Y-2, CONSTANTS.MAX_X-3]]

    stdscr.clear()

    while True:

        msg = "Choose the difficulty level, harder the level, lesser the time you get to guess!"
        msg = msg.center(CONSTANTS.MAX_X-9)

        draw_box(stdscr, 1, 3, msg)

        for index, difficulty in enumerate(menu.options):
            if index == menu.current:
                stdscr.insstr(CONSTANTS.CENTER_Y + index, CONSTANTS.CENTER_X, difficulty, curses.A_REVERSE)
                continue
            stdscr.insstr(CONSTANTS.CENTER_Y + index, CONSTANTS.CENTER_X, difficulty)

        textpad.rectangle(stdscr, box_dim[0][0], box_dim[0][1], box_dim[1][0], box_dim[1][1])

        stdscr.refresh()
        key = stdscr.getch()

        if (key == curses.KEY_UP):
            menu.inc()
        elif (key == curses.KEY_DOWN):
            menu.dec()

        if key in [10, 13]:
            break

        stdscr.clear()

    return menu.options[menu.current].strip()


def play(stdscr: curses.window, CONSTANTS: 'CONSTANTS', game_mode: str) -> None:  # noqa: F821
    """Screen shown when play option is selected"""
    msg = f"Haven't implemented the play screen yet! You have selected the {game_mode} mode"
    stdscr.clear()

    while True:
        draw_box(stdscr, CONSTANTS.CENTER_Y, CONSTANTS.CENTER_X - len(msg)//2, msg)
        key = stdscr.getch()
        if key in [10, 13]:
            return


def main_menu(stdscr: curses.window, CONSTANTS: 'CONSTANTS', default: int = 0,  # noqa: F821
              mode: str = "Easy") -> None:
    """Main menu screen of the app."""
    stdscr.clear()

    menu = Menu(options=["Play", "Difficulty", "Exit"], default=default, align=True)
    box_dim = [[4, 3], [CONSTANTS.MAX_Y-2, CONSTANTS.MAX_X-3]]

    while True:

        msg = f"Current Mode : {mode}"
        draw_box(stdscr, 1, CONSTANTS.CENTER_X - len(msg) // 2, msg)

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
            if menu.current == 0:
                play(stdscr, CONSTANTS, game_mode=mode)

            elif menu.current == 1:
                mode = difficulty_level(stdscr, CONSTANTS)

            elif menu.current == 2:
                return

        stdscr.clear()

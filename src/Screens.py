import curses
import os
from curses import textpad

from utils.image_to_ascii import get_ascii
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


def intro(stdscr: curses.window, CONSTANTS: 'CONSTANTS', game_mode: str) -> None:  # noqa: F821
    """Screen which serves as an intro for the game. Displays a box and a short intro message

    Parameters
    ----------
    stdscr: curses.window
        Curses window
    CONSTANTS: 'CONSTANTS'
        Constants (screen size, etc.)
    game_mode: str
        Difficulty level (Easy/Medium/Hard)
    """
    intro_msg = "Look! A box! I bet it contains something interesting..."
    start_question = "Should we take a look inside?"

    stdscr.clear()

    filename = os.path.join(os.path.dirname(__file__), 'assets', 'box.png')

    box_size = min(CONSTANTS.MAX_Y, CONSTANTS.MAX_X - 20)

    box = get_ascii(filename, (box_size + 20, box_size - 3))
    stdscr.addstr(0, 0, box)

    draw_box(stdscr, CONSTANTS.MAX_Y - 3, CONSTANTS.CENTER_X - len(intro_msg) // 2, intro_msg)

    while True:
        key = stdscr.getch()
        if key:
            key = None
            break

    stdscr.clear()
    stdscr.addstr(0, 0, box)
    draw_box(stdscr, CONSTANTS.MAX_Y - 3, CONSTANTS.CENTER_X - len(start_question) // 2, start_question)

    while True:
        key = stdscr.getch()
        if key:
            play(stdscr, CONSTANTS, game_mode=game_mode)
            return


def play(stdscr: curses.window, CONSTANTS: 'CONSTANTS', game_mode: str) -> None:  # noqa: F821
    """Main play screen

    Parameters
    ----------
    stdscr: curses.window
        Curses window
    CONSTANTS: 'CONSTANTS'
        Constants (screen size, etc.)
    game_mode: str
        Difficulty level (Easy/Medium/Hard)
    """
    stdscr.clear()
    solution_screen(stdscr, CONSTANTS, "http://example.com", has_won=True)
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
                intro(stdscr, CONSTANTS, game_mode=mode)

            elif menu.current == 1:
                mode = difficulty_level(stdscr, CONSTANTS)

            elif menu.current == 2:
                return

        stdscr.clear()


def solution_screen(stdscr: curses.window, CONSTANTS: 'CONSTANTS', image_url: str, default: int = 0,  # noqa: F821
                    has_won: bool = False) -> None:
    """Screen to show the user what the image was if he gives up and to congrat him otherwise

    Parameters
    ----------
    stdscr: curses.window
        Curses window
    CONSTANTS: 'CONSTANTS'
        Constants (screen size, etc.)
    has_won: bool
        Whether thhe user has made a correct guess
    image_url: str
        Pixabay URL of the image
    """
    stdscr.clear()
    win_msg = "Congratulations! You've guessed correctly!"
    lose_msg = "Oh no! You've lost :("

    if has_won:
        draw_box(stdscr, CONSTANTS.CENTER_Y - 3, CONSTANTS.CENTER_X - len(win_msg) // 2, win_msg)
    else:
        draw_box(stdscr, CONSTANTS.CENTER_Y - 3, CONSTANTS.CENTER_X - len(lose_msg) // 2, lose_msg)

    stdscr.addstr(CONSTANTS.CENTER_Y + 1, CONSTANTS.CENTER_X - len(image_url) // 2, image_url)
    while True:
        key = stdscr.getch()
        if key:
            return

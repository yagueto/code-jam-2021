from typing import List

from fuzzywuzzy import fuzz
from PyDictionary import PyDictionary


def validate(guess: str, synonyms: List[str], threshold: int = 95) -> bool:
    """Validate a user guess against list of synonyms

    Parameters
    ----------
    guess : str
        Guess user provided
    synonyms : List[str]
        List of synonyms of actual solution
    threshold : int, optional
        Distance the string can be from any of the synonyms (typos etc), by default 95

    Returns
    -------
    bool
        Whether the guess was correct or not
    """
    guess = guess.lower()
    match = False

    for synonym in synonyms:
        if fuzz.partial_ratio(guess, synonym) >= threshold:
            match = True
            break

    return match


def get_synonyms(solution: str) -> List[str]:
    """Retrieve synonyms for correct solution

    Parameters
    ----------
    solution : str
        Correct guess for puzzle

    Returns
    -------
    List[str]
        List containing valid synonyms to solution
    """
    synonyms = PyDictionary().synonym(solution)
    return synonyms + [solution]

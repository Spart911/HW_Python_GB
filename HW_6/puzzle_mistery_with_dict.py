import puzzle_mystery

__all__ = ['new_puzzle', 'save_statistic', 'show_statistic']

_ANSWERS = dict()


def new_puzzle(puzles: dict, limit: int):
    for key, value in puzles.items():
        puzzle_mystery.puzzle(key, value, limit)


def save_statistic(puzzle: str, count_right: int):
    _ANSWERS[puzzle] = count_right


def show_statistic():
    print(*(f'{key} - {value}\n' for key, value in _ANSWERS.items()))
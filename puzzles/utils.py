from pathlib import Path

from functional import seq


def get_input_seq(day: int) -> seq:
    """Return a seq with the contents of the day's input file, one line per
    element, as strings, with trimmed whitespace.
    """
    fname = f"day_{day:02}_input.txt"
    fpath = Path(__file__).parent.parent / "inputs" / fname
    return seq.open(fpath).map(str.strip)


if __name__ == "__main__":
    get_input_seq(day=1).for_each(print)

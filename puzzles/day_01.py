from functional import seq

from puzzles.utils import get_input_seq


def larger_than_previous_count(int_seq: seq) -> int:
    # Create offset sequence by dropping first element
    offset_seq = int_seq.drop(1)

    # Zip original with offset to get consecutive pairs
    pairs_seq = int_seq.zip(offset_seq)

    # Map pairs to func: is the latter earlier than the former?
    larger = pairs_seq.starmap(lambda a, b: 1 if a < b else 0)

    return larger.sum()


def get_window_sums(int_seq: seq, window_size: int) -> int:
    # Get consecutive sequences of seq[1:]
    tails = int_seq.tails()

    # Take 3 elements from each
    windows = tails.map(lambda sq: sq.take(window_size))

    # Use only windows with size 3 (end of seq may have less)
    windows = windows.filter(lambda sq: sq.size() == window_size)

    # The relevant number is the sum of elements in the window
    window_sums = windows.map(sum)

    return window_sums


def day_1_part_1() -> int:
    """
    --- Day 1: Sonar Sweep ---

    You're minding your own business on a ship at sea when the overboard alarm
    goes off! You rush to see if you can help. Apparently, one of the Elves
    tripped and accidentally sent the sleigh keys flying into the ocean!

    Before you know it, you're inside a submarine the Elves keep ready for
    situations like this. It's covered in Christmas lights (because of course
    it is), and it even has an experimental antenna that should be able to
    track the keys if you can boost its signal strength high enough; there's
    a little meter that indicates the antenna's signal strength by displaying
    0-50 stars.

    Your instincts tell you that in order to save Christmas, you'll need to get
    all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each
    day in the Advent calendar; the second puzzle is unlocked when you complete
    the first. Each puzzle grants one star. Good luck!

    As the submarine drops below the surface of the ocean, it automatically
    performs a sonar sweep of the nearby sea floor. On a small screen,
    the sonar sweep report (your puzzle input) appears: each line is a
    measurement of the sea floor depth as the sweep looks further and further
    away from the submarine.

    For example, suppose you had the following report:

    199
    200
    208
    210
    200
    207
    240
    269
    260
    263

    This report indicates that, scanning outward from the submarine, the sonar
    sweep found depths of 199, 200, 208, 210, and so on.

    The first order of business is to figure out how quickly the depth
    increases, just so you know what you're dealing with - you never know if
    the keys will get carried into deeper water by an ocean current or a fish
    or something.

    To do this, count the number of times a depth measurement increases from
    the previous measurement. (There is no measurement before the first
    measurement.) In the example above, the changes are as follows:

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)

    In this example, there are 7 measurements that are larger than the previous
    measurement.

    How many measurements are larger than the previous measurement?
    """
    input_seq = get_input_seq(day=1).map(int)
    result = larger_than_previous_count(input_seq)
    print(f"Result for day 1, part 1: {result}")
    assert result == 1527
    return result


def day_1_part_2() -> int:
    """
    --- Part Two ---

    Considering every single measurement isn't as useful as you expected:
    there's just too much noise in the data.

    Instead, consider sums of a three-measurement sliding window. Again
    considering the above example:

    199  A
    200  A B
    208  A B C
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G
    269    F G H
    260      G H
    263        H

    Start by comparing the first and second three-measurement windows. The
    measurements in the first window are marked A (199, 200, 208); their sum
    is 199 + 200 + 208 = 607. The second window is marked B (200, 208,
    210); its sum is 618. The sum of measurements in the second window is
    larger than the sum of the first, so this first comparison increased.

    Your goal now is to count the number of times the sum of measurements in
    this sliding window increases from the previous sum. So, compare A with
    B, then compare B with C, then C with D, and so on. Stop when there
    aren't enough measurements left to create a new three-measurement sum.

    In the above example, the sum of each three-measurement window is as
    follows:

    A: 607 (N/A - no previous sum)
    B: 618 (increased)
    C: 618 (no change)
    D: 617 (decreased)
    E: 647 (increased)
    F: 716 (increased)
    G: 769 (increased)
    H: 792 (increased)

    In this example, there are 5 sums that are larger than the previous sum.

    Consider sums of a three-measurement sliding window. How many sums are
    larger than the previous sum?
    """
    input_seq = get_input_seq(day=1).map(int)
    window_sums = get_window_sums(input_seq, window_size=3)
    result = larger_than_previous_count(window_sums)
    print(f"Result for day 1, part 2: {result}")
    assert result == 1575
    return result


if __name__ == "__main__":
    day_1_part_1()
    day_1_part_2()

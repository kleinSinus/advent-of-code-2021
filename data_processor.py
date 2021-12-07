import scripts.day01
import scripts.day02
import scripts.day03
import scripts.day04
import scripts.day05
import scripts.day06
import scripts.day07
import scripts.day08
import scripts.day09
import scripts.day10
import scripts.day11
import scripts.day12
import scripts.day13
import scripts.day14
import scripts.day15
import scripts.day16
import scripts.day17
import scripts.day18
import scripts.day19
import scripts.day20
import scripts.day21
import scripts.day22
import scripts.day23
import scripts.day24
import scripts.day25

dates = {
    1:  scripts.day01.do_stuff,
    2:  scripts.day02.do_stuff,
    3:  scripts.day03.do_stuff,
    4:  scripts.day04.do_stuff,
    5:  scripts.day05.do_stuff,
    6:  scripts.day06.do_stuff,
    7:  scripts.day07.do_stuff,
    8:  scripts.day08.do_stuff,
    9:  scripts.day09.do_stuff,
    10: scripts.day10.do_stuff,
    11: scripts.day11.do_stuff,
    12: scripts.day12.do_stuff,
    13: scripts.day13.do_stuff,
    14: scripts.day14.do_stuff,
    15: scripts.day15.do_stuff,
    16: scripts.day16.do_stuff,
    17: scripts.day17.do_stuff,
    18: scripts.day18.do_stuff,
    19: scripts.day19.do_stuff,
    20: scripts.day20.do_stuff,
    21: scripts.day21.do_stuff,
    22: scripts.day22.do_stuff,
    23: scripts.day23.do_stuff,
    24: scripts.day24.do_stuff,
    25: scripts.day25.do_stuff
}

def invalid(input_data, test_mode):
    return "Not a valid input date"

# runs the script for a specific day of the AoC challenge and generates the output if file is found
def gen_output(input_data, date, test_mode):
    stuff = dates.get(date, invalid)
    output = stuff(input_data, test_mode)
    return output

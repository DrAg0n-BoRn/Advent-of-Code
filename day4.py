'''
 _______  _        _______  _______  _                 _______    _______  _______  ______   _        _______  _______  _______ 
(  ____ \( \      (  ____ \(  ___  )( (    /||\     /|(  ____ )  (       )(  ___  )(  __  \ ( (    /|(  ____ \(  ____ \(  ____ \
| (    \/| (      | (    \/| (   ) ||  \  ( || )   ( || (    )|  | () () || (   ) || (  \  )|  \  ( || (    \/| (    \/| (    \/
| |      | |      | (__    | (___) ||   \ | || |   | || (____)|  | || || || (___) || |   ) ||   \ | || (__    | (_____ | (_____ 
| |      | |      |  __)   |  ___  || (\ \) || |   | ||  _____)  | |(_)| ||  ___  || |   | || (\ \) ||  __)   (_____  )(_____  )
| |      | |      | (      | (   ) || | \   || |   | || (        | |   | || (   ) || |   ) || | \   || (            ) |      ) |
| (____/\| (____/\| (____/\| )   ( || )  \  || (___) || )        | )   ( || )   ( || (__/  )| )  \  || (____/\/\____) |/\____) |
(_______/(_______/(_______/|/     \||/    )_)(_______)|/         |/     \||/     \|(______/ |/    )_)(_______/\_______)\_______)
'''

# --- Preprocessing --- 
with open("./inputs/input4.txt", "r") as file:
    data_raw = file.readlines()
data = [line.strip() for line in data_raw]

def get_tuple(raw: str) -> list[tuple[int, int]]:
    step1 = [raw.split(sep=",")[0], raw.split(sep=",")[1]]
    step2 = [[step1[0].split(sep="-")[0], step1[0].split(sep="-")[1]], [step1[1].split(sep="-")[0], step1[1].split(sep="-")[1]]]
    step3 = [(int(step2[0][0]), int(step2[0][1])), (int(step2[1][0]), int(step2[1][1]))]
    return step3


#  --- PART I ---
def is_contained(elven: list[tuple[int, int]]) -> bool:
    elf1_lower, elf1_upper = elven[0][0], elven[0][1]
    elf2_lower, elf2_upper = elven[1][0], elven[1][1]
    # Define conditions
    if elf1_lower <= elf2_lower and elf1_upper >= elf2_upper:
        return True
    elif elf2_lower <= elf1_lower and elf2_upper >= elf1_upper:
        return True
    else:
        return False

def part_one():
    total_value = 0
    for line in data: 
        elf_tuple = get_tuple(line)
        if is_contained(elf_tuple):
            total_value += 1
    print(total_value)


# --- PART II ---
def is_overlap(elven: list[tuple[int, int]]) -> bool:
    elf1_lower, elf1_upper = elven[0][0], elven[0][1]
    elf2_lower, elf2_upper = elven[1][0], elven[1][1]
    # Define ranges
    range1 = list(range(elf1_lower, elf1_upper+1))
    range2 = list(range(elf2_lower, elf2_upper+1))
    # Define conditions
    for number in range1:
        if number in range2:
            return True
    else:
        return False

def part_two():
    total_value = 0
    for line in data:
        elf_tuple = get_tuple(line)
        if is_overlap(elf_tuple):
            total_value += 1
    print(total_value)

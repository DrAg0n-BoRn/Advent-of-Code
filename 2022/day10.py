'''
 .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |   ______     | || | _____  _____ | | | | ____    ____ | || |      __      | || |  ________    | || | ____  _____  | || |  _________   | || |    _______   | || |    _______   | |
| |   .' ___  |  | || |  |_   __ \   | || ||_   _||_   _|| | | ||_   \  /   _|| || |     /  \     | || | |_   ___ `.  | || ||_   \|_   _| | || | |_   ___  |  | || |   /  ___  |  | || |   /  ___  |  | |
| |  / .'   \_|  | || |    | |__) |  | || |  | |    | |  | | | |  |   \/   |  | || |    / /\ \    | || |   | |   `. \ | || |  |   \ | |   | || |   | |_  \_|  | || |  |  (__ \_|  | || |  |  (__ \_|  | |
| |  | |         | || |    |  ___/   | || |  | '    ' |  | | | |  | |\  /| |  | || |   / ____ \   | || |   | |    | | | || |  | |\ \| |   | || |   |  _|  _   | || |   '.___`-.   | || |   '.___`-.   | |
| |  \ `.___.'\  | || |   _| |_      | || |   \ `--' /   | | | | _| |_\/_| |_ | || | _/ /    \ \_ | || |  _| |___.' / | || | _| |_\   |_  | || |  _| |___/ |  | || |  |`\____) |  | || |  |`\____) |  | |
| |   `._____.'  | || |  |_____|     | || |    `.__.'    | | | ||_____||_____|| || ||____|  |____|| || | |________.'  | || ||_____|\____| | || | |_________|  | || |  |_______.'  | || |  |_______.'  | |
| |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''
# --- Preprocessing ---
def preprocess():
    with open("./inputs/input10.txt", "r") as file:
        data_raw = [line.strip() for line in file.readlines()]
    # Assembly to Python
    data = [1]
    for command in data_raw:
        if "noop" in command:
            data.append(0)
        else:
            data.append(0)
            data.append(int(command[5:]))
    return data


# --- PART I ---
def signal_strength(dict_: dict, cycles: list[int]=[20, 60, 100, 140, 180, 220]):
    suma = 0
    for cycle in cycles:
        result = dict_.get(cycle) * cycle
        suma += result
    return suma

def part_one():
    commands = preprocess()
    temp_ = []
    x = 0
    for command in commands:
        x += command
        temp_.append(x)
    signal = dict(enumerate(temp_, start=1))
    print(signal_strength(signal))
    
    
# --- PART II ---
def part_two():
    commands = preprocess()
    temp_ = []
    x = 0
    screen = ""
    for command in commands:
        x += command
        temp_.append(x)
    for CRT, sprite in enumerate(temp_, start=0):
        if CRT % 40 in [sprite-1, sprite, sprite+1]:
            screen += "#"
        else:
            screen += "."
    for pixel in range(0, 240, 40):
        print(screen[pixel:pixel+40])
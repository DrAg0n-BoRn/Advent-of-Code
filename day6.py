'''
 _______  __   __  __    _  ___   __    _  _______    __   __  _______  ______   __    _  _______  _______  _______ 
|       ||  | |  ||  |  | ||   | |  |  | ||       |  |  |_|  ||   _   ||      | |  |  | ||       ||       ||       |
|_     _||  | |  ||   |_| ||   | |   |_| ||    ___|  |       ||  |_|  ||  _    ||   |_| ||    ___||  _____||  _____|
  |   |  |  |_|  ||       ||   | |       ||   | __   |       ||       || | |   ||       ||   |___ | |_____ | |_____ 
  |   |  |       ||  _    ||   | |  _    ||   ||  |  |       ||       || |_|   ||  _    ||    ___||_____  ||_____  |
  |   |  |       || | |   ||   | | | |   ||   |_| |  | ||_|| ||   _   ||       || | |   ||   |___  _____| | _____| |
  |___|  |_______||_|  |__||___| |_|  |__||_______|  |_|   |_||__| |__||______| |_|  |__||_______||_______||_______|
'''

# --- Preprocessing ---
def preprocess() -> str:
    with open(file="./inputs/input6.txt", mode="r") as file:
        data = file.readline().strip()
    return data

def search(length: int) -> int:
    signal = preprocess()
    for i in range(len(signal) - length):
        packet = set(signal[i:i+length])
        if len(packet) == length:
            position = i + length
            break
    return position

# --- PART I ---
def part_one():
    print(search(length=4))
    
# --- PART II ---
def part_two():
    print(search(length=14))

'''
 (`-').->            _  (`-') _  (`-')                        <-. (`-')   (`-')  _ _(`-')   <-. (`-')_  (`-')  _ (`-').-> (`-').-> 
 ( OO)_       .->    \-.(OO ) \-.(OO )   <-.        .->          \(OO )_  (OO ).-/( (OO ).->   \( OO) ) ( OO).-/ ( OO)_   ( OO)_   
(_)--\_) ,--.(,--.   _.'    \ _.'    \ ,--. )   ,--.'  ,-.    ,--./  ,-.) / ,---.  \    .'_ ,--./ ,--/ (,------.(_)--\_) (_)--\_)  
/    _ / |  | |(`-')(_...--''(_...--'' |  (`-')(`-')'.'  /    |   `.'   | | \ /`.\ '`'-..__)|   \ |  |  |  .---'/    _ / /    _ /  
\_..`--. |  | |(OO )|  |_.' ||  |_.' | |  |OO )(OO \    /     |  |'.'|  | '-'|_.' ||  |  ' ||  . '|  |)(|  '--. \_..`--. \_..`--.  
.-._)   \|  | | |  \|  .___.'|  .___.'(|  '__ | |  /   /)     |  |   |  |(|  .-.  ||  |  / :|  |\    |  |  .--' .-._)   \.-._)   \ 
\       /\  '-'(_ .'|  |     |  |      |     |' `-/   /`      |  |   |  | |  | |  ||  '-'  /|  | \   |  |  `---.\       /\       / 
 `-----'  `-----'   `--'     `--'      `-----'    `--'        `--'   `--' `--' `--'`------' `--'  `--'  `------' `-----'  `-----'  
'''

# --- Preprocessing ---
def preprocess() -> tuple[dict[int, list[str]], list[tuple[int, int, int]]]:
    with open("./inputs/input5.txt", "r") as file:
        crate_lines = []
        for _ in range(8):
            crate_lines.append(file.readline())    
        crate_index = file.readline()
        _ = file.readline()
        instructions = file.readlines()

    # organize crates in lists... somehow
    crates = {int(key):[] for key in crate_index if not key.isspace()}
    for line in crate_lines:
        temp_ = []
        for i in range(0, 4*len(crates), 4):
            temp_.append(line[i:i+4].strip())
        for j in range(len(temp_)):
            if len(temp_[j]) > 0:
                crates[j+1].append(temp_[j][1])
    # Rearrange crate order
    for key, list_ in crates.items():
        crates[key] = list_[::-1]

    # Decipher instructions... somehow
    range_from_to = []
    for instruction in instructions:
        instruction = instruction.strip()
        parts = instruction.split(" ")
        range_from_to.append((int(parts[1]), int(parts[3]), int(parts[5])))
        
    return (crates, range_from_to)


# --- PART I ---
def part_one():
    crates, instructions = preprocess()[0], preprocess()[1]
    
    for range_, from_, to_ in instructions:
        for _ in range(range_):
            crates[to_].append(crates[from_].pop(-1))
        
    result = ""    
    for i in range(1, len(crates) + 1):
        result = result + crates[i][-1]
        
    print(result)


# --- PART II ---
def part_two():
    crates, instructions = preprocess()[0], preprocess()[1]
    
    for range_, from_, to_ in instructions:
        for i in range(-range_, 0, 1):
            crates[to_].append(crates[from_].pop(i))

    result = ""    
    for i in range(1, len(crates) + 1):
        result = result + crates[i][-1]
        
    print(result)

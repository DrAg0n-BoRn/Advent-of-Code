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
with open("./inputs/input5.txt", "r") as file:
    crate_lines = []
    for _ in range(8):
        crate_lines.append(file.readline())    
    crate_index = file.readline()
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
for instruction in instructions:
    instruction.split(" ")


# --- PART I ---

'''
_____  ____  ____  __  __                          
| () )/ () \/ (__`|  |/  /                          
|_|\_\\____/\____)|__|\__\                          
_____  ____  _____  ____ _____                      
| ()_)/ () \ | ()_)| ===|| () )                     
|_|  /__/\__\|_|   |____||_|\_\                     
  ____  ____  _   ____   ____  ____ _____   ____    
 (_ (_`/ (__`| | (_ (_` (_ (_`/ () \| () ) (_ (_`   
.__)__)\____)|_|.__)__).__)__)\____/|_|\_\.__)__)   
 __  __   ____   ____  __  _  ____   ____   ____    
|  \/  | / () \ | _) \|  \| || ===| (_ (_` (_ (_`   
|_|\/|_|/__/\__\|____/|_|\__||____|.__)__).__)__)                                               
'''

lose = 0
draw = 3
win = 6


def convert(choice: str) -> int:
    match choice:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3


def get_score(elf: str, player: str) -> int:
    player: int = convert(player)
    elf: int = convert(elf)
    
    if player == elf:
        return player + draw
    elif player == 1 and elf == 3:
        return player + win
    elif elf == 1 and player == 3:
        return player + lose
    elif player > elf:
        return player + win
    elif player < elf:
        return player + lose


score = 0
with open("./inputs/input2.txt", "r") as file:
    for ronda in file:
        list_ = ronda.strip().split(sep=" ")
        score += get_score(elf=list_[0], player=list_[1])
        
print(score)

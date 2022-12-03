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

rock = 1
paper = 2
scissors = 3

score = 0

# --- PART I --- 
# def convert(choice: str) -> int:
#     match choice:
#         case "X":
#             return rock
#         case "Y":
#             return paper
#         case "Z":
#             return scissors
#         case "A":
#             return rock
#         case "B":
#             return paper
#         case "C":
#             return scissors


# def get_score(elf: str, player: str) -> int:
#     player: int = convert(player)
#     elf: int = convert(elf)

#     if player == elf:
#         return player + draw
#     elif player == 1 and elf == 3:
#         return player + win
#     elif elf == 1 and player == 3:
#         return player + lose
#     elif player > elf:
#         return player + win
#     elif player < elf:
#         return player + lose


# with open("./inputs/input2.txt", "r") as file:
#     for ronda in file:
#         list_ = ronda.strip().split(sep=" ")
#         score += get_score(elf=list_[0], player=list_[1])

# print(score)


# --- PART II ---
magic_hat = {
    # Win
    "Z":{"A": paper + win, "B": scissors + win, "C": rock + win},
    # Lose
    "X":{"A": scissors + lose, "B": rock + lose, "C": paper + lose},
    # Draw
    "Y":{"A": rock + draw, "B": paper + draw, "C": scissors + draw},
}

with open("./inputs/input2.txt", "r") as file:
    for ronda in file:
        player = ronda.strip().split(sep=" ")[1]
        elf = ronda.strip().split(sep=" ")[0]
        score += magic_hat[player][elf]

print(score)

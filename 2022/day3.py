'''
,------.               ,--.                         ,--.        ,--.   ,--.           ,--.                              
|  .--. ',--.,--. ,---.|  |,-.  ,---.  ,--,--. ,---.|  |,-.     |   `.'   | ,--,--. ,-|  |,--,--,  ,---.  ,---.  ,---.  
|  '--'.'|  ||  || .--'|     / (  .-' ' ,-.  || .--'|     /     |  |'.'|  |' ,-.  |' .-. ||      \| .-. :(  .-' (  .-'  
|  |\  \ '  ''  '\ `--.|  \  \ .-'  `)\ '-'  |\ `--.|  \  \     |  |   |  |\ '-'  |\ `-' ||  ||  |\   --..-'  `).-'  `) 
`--' '--' `----'  `---'`--'`--'`----'  `--`--' `---'`--'`--'    `--'   `--' `--`--' `---' `--''--' `----'`----' `----'  
'''
import string
letters = string.ascii_letters

def priority(item: str) -> int:
    value = letters.find(item)
    return value + 1

# --- PART I ---
# total_value = 0
# with open("./inputs/input3.txt") as file:
#     for rucksack in file:
#         rucksack = rucksack.strip()
#         pocket1 = []
#         pocket2 = []
        
#         # Distribute items in pockets
#         for i in range(len(rucksack)):
#             if i < len(rucksack)/2:
#                 pocket1.append(rucksack[i])
#             else: 
#                 pocket2.append(rucksack[i])
        
#         # Find common items
#         for item in pocket1:
#             if item in pocket2:
#                 total_value += priority(item)
#                 break
        
# print(total_value)


# --- PART II ---
with open("./inputs/input3.txt") as file:
    rucksacks = file.readlines()

# duplicates are not relevant
rucksacks = [set(rucksack.strip()) for rucksack in rucksacks]

# Make groups of 3 elves
groups = {}
for i in range(0, len(rucksacks), 3):
    groups[i] = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]

# get group badge
total_value = 0
for group_stash in groups.values():
    for item in group_stash[0]:
        if (item in group_stash[1]) and (item in group_stash[2]):
            total_value += priority(item)
            break

print(total_value)

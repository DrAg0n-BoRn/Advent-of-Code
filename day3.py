'''
,------.               ,--.                         ,--.        ,--.   ,--.           ,--.                              
|  .--. ',--.,--. ,---.|  |,-.  ,---.  ,--,--. ,---.|  |,-.     |   `.'   | ,--,--. ,-|  |,--,--,  ,---.  ,---.  ,---.  
|  '--'.'|  ||  || .--'|     / (  .-' ' ,-.  || .--'|     /     |  |'.'|  |' ,-.  |' .-. ||      \| .-. :(  .-' (  .-'  
|  |\  \ '  ''  '\ `--.|  \  \ .-'  `)\ '-'  |\ `--.|  \  \     |  |   |  |\ '-'  |\ `-' ||  ||  |\   --..-'  `).-'  `) 
`--' '--' `----'  `---'`--'`--'`----'  `--`--' `---'`--'`--'    `--'   `--' `--`--' `---' `--''--' `----'`----' `----'  
'''

# --- PART I ---
import string
letters = string.ascii_letters


def priority(item: str) -> int:
    value = letters.find(item)
    return value + 1


total_value = 0
with open("./inputs/input3.txt") as file:
    for rucksack in file:
        rucksack = rucksack.strip()
        pocket1 = []
        pocket2 = []
        
        # Distribute items in pockets
        for i in range(len(rucksack)):
            if i < len(rucksack)/2:
                pocket1.append(rucksack[i])
            else: 
                pocket2.append(rucksack[i])
        
        # Find common items
        for item in pocket1:
            if item in pocket2:
                total_value += priority(item)
                break
        
print(total_value)


# --- PART II ---
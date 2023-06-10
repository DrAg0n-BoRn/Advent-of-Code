# Calory madness

# PART I
# winner = 0
# calories = 0

# with open("./inputs/input1.txt", "r") as file:
# 	for food in file:
# 		if food.isspace():
# 			if calories > winner:
# 				winner = calories
# 			calories = 0
# 		else:
# 			calories += int(food)

# print(winner)


# PART II
winners = [0, 0, 0]
calories = 0

with open ("./inputs/input1.txt", "r") as file:
	for food in file:
		if food.isspace():
			for elf in range(len(winners)):
				if calories > winners[elf]:
					winners[elf] = calories
					winners.sort()
					break
			calories = 0
		else:
			calories += int(food)

print(winners)
print(sum(winners))
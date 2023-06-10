'''
 \\\    ///   .-.   \\\  ///       _ wWw  wWw  wWw    \\\    ///        _   \\\  /// wWw   oo_    oo_    
 ((O)  (O)) c(O_O)c ((O)(O))(OO) .' )(O)_ (O)  (O)    ((O)  (O))   /)  /||_ ((O)(O)) (O)_ /  _)-</  _)-< 
  | \  / | ,'.---.`, | \ ||  ||_/ .' / __)( \  / )     | \  / |  (o)(O) /o_) | \ ||  / __)\__ `. \__ `.  
  ||\\//||/ /|_|_|\ \||\\||  |   /  / (    \ \/ /      ||\\//||   //\\ / |(\ ||\\|| / (      `. |   `. | 
  || \/ ||| \_____/ ||| \ |  ||\ \ (  _)    \o /       || \/ ||  |(__)|| | ))|| \ |(  _)     _| |   _| | 
  ||    ||'. `---' .`||  || (/\)\ `.\ \_   _/ /        ||    ||  /,-. || |// ||  || \ \_  ,-'   |,-'   | 
 (_/    \_) `-...-' (_/  \_)     `._)\__) (_.'        (_/    \_)-'   ''\__/ (_/  \_) \__)(_..--'(_..--'  
'''

# --- PART I ---
monkeys = []
initial = ([77, 69, 76, 77, 50, 58],
           [75, 70, 82, 83, 96, 64, 62],
           [53],
           [85, 64, 93, 64, 99],
           [61, 92, 71],
           [79, 73, 50, 90],
           [50, 89],
           [83, 56, 64, 58, 93, 91, 56, 65])


class Monkey():
    def __init__(self, id_:int, items: list[int]) -> None:
        self.id = id_
        self.items = items
        self.count = 0


def operation(monkey):
    item = monkey.items.pop(0)
    monkey.count += 1
    match monkey.id:
        case 0:
            item = (item * 11) // 3
            if item % 5 == 0:
                monkeys[1].items.append(item)
            else:
                monkeys[5].items.append(item)
        case 1:
            item = (item + 8) // 3
            if item % 17 == 0:
                monkeys[5].items.append(item)
            else:
                monkeys[6].items.append(item)
        case 2:
            item = (item * 3) // 3
            if item % 2 == 0:
                monkeys[0].items.append(item)
            else:
                monkeys[7].items.append(item)
        case 3:
            item = (item + 4) // 3
            if item % 7 == 0:
                monkeys[7].items.append(item)
            else:
                monkeys[2].items.append(item)
        case 4:
            item = (item * item) // 3
            if item % 3 == 0:
                monkeys[2].items.append(item)
            else:
                monkeys[3].items.append(item)
        case 5:
            item = (item + 2) // 3
            if item % 11 == 0:
                monkeys[4].items.append(item)
            else:
                monkeys[6].items.append(item)
        case 6:
            item = (item + 3) // 3
            if item % 13 == 0:
                monkeys[4].items.append(item)
            else:
                monkeys[3].items.append(item)
        case 7:
            item = (item + 5) // 3
            if item % 19 == 0:
                monkeys[1].items.append(item)
            else:
                monkeys[0].items.append(item)


def part_one():
    # make monkeys
    for i in range(8):
        new_monkey = Monkey(id_=i, items=initial[i])
        monkeys.append(new_monkey)
    # monkey business
    for round in range(20):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                operation(monkey)
    # 2 most active monkeys
    winner = sorted([monkey.count for monkey in monkeys], reverse=True)
    print(winner[0] * winner[1])


# --- PART II ---
import math

def operation_2(monkey, lcm):
    item = monkey.items.pop(0)
    monkey.count += 1
    match monkey.id:
        case 0:
            item = (item * 11) % lcm 
            if item % 5 == 0:
                monkeys[1].items.append(item)
            else:
                monkeys[5].items.append(item)
        case 1:
            item = (item + 8) % lcm 
            if item % 17 == 0:
                monkeys[5].items.append(item)
            else:
                monkeys[6].items.append(item)
        case 2:
            item = (item * 3) % lcm 
            if item % 2 == 0:
                monkeys[0].items.append(item)
            else:
                monkeys[7].items.append(item)
        case 3:
            item = (item + 4) % lcm 
            if item % 7 == 0:
                monkeys[7].items.append(item)
            else:
                monkeys[2].items.append(item)
        case 4:
            item = (item * item) % lcm 
            if item % 3 == 0:
                monkeys[2].items.append(item)
            else:
                monkeys[3].items.append(item)
        case 5:
            item = (item + 2) % lcm 
            if item % 11 == 0:
                monkeys[4].items.append(item)
            else:
                monkeys[6].items.append(item)
        case 6:
            item = (item + 3) % lcm 
            if item % 13 == 0:
                monkeys[4].items.append(item)
            else:
                monkeys[3].items.append(item)
        case 7:
            item = (item + 5) % lcm 
            if item % 19 == 0:
                monkeys[1].items.append(item)
            else:
                monkeys[0].items.append(item)


def part_two():
    # make monkeys
    for i in range(8):
        new_monkey = Monkey(id_=i, items=initial[i])
        monkeys.append(new_monkey)
    # monkey business
    lcm = math.lcm(19, 13, 11, 3, 7, 2, 17, 5)
    for round in range(10000):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                operation_2(monkey, lcm)
    # 2 most active monkeys
    winner = sorted([monkey.count for monkey in monkeys], reverse=True)
    print(winner[0] * winner[1])
    

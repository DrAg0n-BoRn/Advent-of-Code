'''
 ______    ______   ______   ______       ___ __ __   ________   ______   ___   __    ______   ______   ______      
/_____/\  /_____/\ /_____/\ /_____/\     /__//_//_/\ /_______/\ /_____/\ /__/\ /__/\ /_____/\ /_____/\ /_____/\     
\:::_ \ \ \:::_ \ \\:::_ \ \\::::_\/_    \::\| \| \ \\::: _  \ \\:::_ \ \\::\_\\  \ \\::::_\/_\::::_\/_\::::_\/_    
 \:(_) ) )_\:\ \ \ \\:(_) \ \\:\/___/\    \:.      \ \\::(_)  \ \\:\ \ \ \\:. `-\  \ \\:\/___/\\:\/___/\\:\/___/\   
  \: __ `\ \\:\ \ \ \\: ___\/ \::___\/_    \:.\-/\  \ \\:: __  \ \\:\ \ \ \\:. _    \ \\::___\/_\_::._\:\\_::._\:\  
   \ \ `\ \ \\:\_\ \ \\ \ \    \:\____/\    \. \  \  \ \\:.\ \  \ \\:\/.:| |\. \`-\  \ \\:\____/\ /____\:\ /____\:\ 
    \_\/ \_\/ \_____\/ \_\/     \_____\/     \__\/ \__\/ \__\/\__\/ \____/_/ \__\/ \__\/ \_____\/ \_____\/ \_____\/ 
'''
# --- Preprocessing ---
def preprocess():
    with open("./inputs/input9.txt", "r") as file:
        data = [(line.strip().split(" ")[0], int(line.strip().split(" ")[1])) for line in file.readlines()]
    return data


# --- PART I ---
def move(inst_: str, head: list[int], tail: list[int]):
    xh, yh = head
    xt, yt = tail
    match inst_:
        case "U":
            yh += 1
        case "D":
            yh -= 1
        case "R":
            xh += 1
        case "L":
            xh -= 1
    # Tail looks around
    xrange = [xt-1, xt, xt+1]
    yrange = [yt-1, yt, yt+1]
    panic = False
    if xh not in xrange or yh not in yrange:
        panic = True
    if panic:
        x = xh - xt
        y = yh - yt
        if x == 0:
            yt += y//2
        elif y == 0:
            xt += x//2
        elif x > 0:
            if y > 0:
                xt += 1
                yt += 1
            else:
                xt += 1
                yt -= 1
        else:
            if y > 0:
                xt -= 1
                yt += 1
            else:
                xt -= 1
                yt -= 1
    return [xh, yh], [xt, yt]

def part_one():
    instructions = preprocess()
    H = [1000, 1000]
    T = [1000, 1000]
    visited = [tuple(T)]
    for instruction in instructions:
        for _ in range(instruction[1]):
            H, T = move(inst_=instruction[0], head=H, tail=T)
            visited.append(tuple(T))
    visited = set(visited)
    print(len(visited))
         

# --- Part II ---
# TODO

'''
Rules are ambiguous and not clear. According to the example: 

                                    ...H..
                                    ....1.
                                    ..432.
                                    .5....
                                    6.....

..H1..     "H" moves one position to (row 1, column 3)                           ..H1..
...2..     Following the logic of part I: "Knot 1" moves to (row 1, column 4)    ....2.
..43..     "Knot 2" can move to (row 2, column 5) and satisfy the condition.     ..43..
.5....     However, it arbitrarily moves to (row2, column 4).                    .5....
6.....                                                                           6.....

'''
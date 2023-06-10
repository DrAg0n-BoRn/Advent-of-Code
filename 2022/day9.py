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
def preprocess() -> list[tuple[str,int]]:
    with open("./inputs/input9.txt", "r") as file:
        data = [(line.strip().split(" ")[0], int(line.strip().split(" ")[1])) for line in file.readlines()]
    return data

# --- PART I & PART II ---
class Knot():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.stalk_x = 100
        self.stalk_y = 100
        self.recorrido = [(self.x, self.y)]
        self.id = id(self)
                
    def stalk(self, x, y):
        # check if it left the zone
        xrange = [self.x-1, self.x, self.x+1]
        yrange = [self.y-1, self.y, self.y+1]
        if x not in xrange or y not in yrange:
            # check if x or y are equal, if true, follow in a straight line
            if not self.check_sides(x, y):
                # if previous position = corner, then move to a corner
                if not self.check_corners(x, y):
                    # if false, then it was at either N, E, W, S and moved like a chess horse
                    self.check_symbol(x, y)
            self.record()
        else:
            self.stalk_x, self.stalk_y = x, y
        return self.x, self.y
    
    def check_sides(self, x, y):
        if x == self.x:
            self.y = self.stalk_y
            self.stalk_x, self.stalk_y = x, y
            return True
        elif y == self.y:
            self.x = self.stalk_x
            self.stalk_x, self.stalk_y = x, y
            return True
        else:
            return False
        
    def check_corners(self, x, y):
        if self.stalk_x == self.x + 1 or self.stalk_x == self.x - 1:
            if self.stalk_y == self.y + 1 or self.stalk_y == self.y - 1:
                self.x, self.y = self.stalk_x, self.stalk_y
                self.stalk_x, self.stalk_y = x, y
                return True
        return False
    
    def check_symbol(self, x, y):
        axis_x = x - self.x
        if axis_x > 0:
            self.x += 1
        else:
            self.x -= 1
        axis_y = y - self.y
        if axis_y > 0:
            self.y += 1
        else:
            self.y -= 1
        self.stalk_x, self.stalk_y = x, y
        
    def record(self):
        self.recorrido.append((self.x, self.y))
        
    def __repr__(self) -> str:
        return f"Stalker Knot #{self.id}"


def knot_maker(n: int=9):
    knots = []
    for _ in range(n):
        new_knot = Knot()
        knots.append(new_knot)
    return knots


def move_head(inst_: str, x: int, y: int):
    match inst_:
        case "U":
            y += 1
        case "D":
            y -= 1
        case "R":
            x += 1
        case "L":
            x -= 1
    return x, y


def solution():
    Hx, Hy = 100, 100
    knots = knot_maker()
    instructions = preprocess()
    for instruction in instructions:
        for _ in range(instruction[1]):
            Hx, Hy = move_head(inst_=instruction[0], x=Hx, y=Hy)
            newX, newY = knots[0].stalk(Hx, Hy)
            for knot in knots[1:]:
                newX, newY= knot.stalk(newX, newY)
    # Print results
    visits0 = set(knots[0].recorrido)
    visits9 = set(knots[-1].recorrido)
    print(f"First stalker knot: {len(visits0)}\nLast stalker knot: {len(visits9)}")

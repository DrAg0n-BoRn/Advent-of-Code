'''
 ______     __         __     __    __     ______     __     __   __     ______        __    __     ______     _____     __   __     ______     ______     ______    
/\  ___\   /\ \       /\ \   /\ "-./  \   /\  == \   /\ \   /\ "-.\ \   /\  ___\      /\ "-./  \   /\  __ \   /\  __-.  /\ "-.\ \   /\  ___\   /\  ___\   /\  ___\   
\ \ \____  \ \ \____  \ \ \  \ \ \-./\ \  \ \  __<   \ \ \  \ \ \-.  \  \ \ \__ \     \ \ \-./\ \  \ \  __ \  \ \ \/\ \ \ \ \-.  \  \ \  __\   \ \___  \  \ \___  \  
 \ \_____\  \ \_____\  \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\  \ \_\\"\_\  \ \_____\     \ \_\ \ \_\  \ \_\ \_\  \ \____-  \ \_\\"\_\  \ \_____\  \/\_____\  \/\_____\ 
  \/_____/   \/_____/   \/_/   \/_/  \/_/   \/_____/   \/_/   \/_/ \/_/   \/_____/      \/_/  \/_/   \/_/\/_/   \/____/   \/_/ \/_/   \/_____/   \/_____/   \/_____/ 
'''

# --- Preprocessing ---
import string
letters = string.ascii_lowercase

START_Y = None
START_X = None
END_Y = None
END_X = None

class Hill():
    def __init__(self, value: int) -> None:
        self.value = value 
        self.open = True
        
    def __repr__(self) -> str:
        return f"{self.value}"


def preprocess() -> list[list]:
    with open("./inputs/input12.txt", "r") as file:
        data_raw = [line.strip() for line in file.readlines()]
    data = []
    y = 0
    for line in data_raw:
        temp_ = []
        x = 0
        for char in line:
            if char == "S":
                elevation = 0
                global START_X, START_Y
                START_Y = y
                START_X = x
            elif char == "E":
                elevation = 26
                global END_X, END_Y
                END_Y = y
                END_X = x
            else:
                elevation = letters.find(char)
            hill = Hill(value=elevation)
            temp_.append(hill)
            x += 1
        data.append(temp_)
        y += 1
    return data


# --- PART I ---
class Walker():
    def __init__(self, mapa: list[list]) -> None:
        self.y = START_Y
        self.x = START_X
        self.winner = False
        self.active = True
        self.steps = 0
        self.history = []
        self.mapa = mapa
        self.current_hill = 0
        self.options = []
    
    def walk(self):
        # unblock
        self.unblock()
        # check
        self.check()
        # walk
        if len(self.options) == 0 and self.winner:
            self.active = False
            print("Chicken Dinner", self.steps)
        elif len(self.options) == 0:
            print("Self Destruct", self.steps)
            if self.x == START_X and self.y == START_Y:
                self.active = False
            else:
                self.reset()
        else:
            self.steps += 1
            match self.options[0]:
                case "U":
                    self.y -= 1
                case "L":
                    self.x -= 1
                case "D":
                    self.y += 1
                case "R":
                    self.x += 1
    
    def check(self):
        self.current_hill = self.mapa[self.y][self.x].value
        if self.current_hill == 26:
            self.winner = True
            return
        
        self.options = []
        # Check available options
        if self.x <= END_X and self.y <= END_Y:
            self.derecha()
            self.abajo()
            self.izquierda()
            self.arriba()
        elif self.x > END_X and self.y < END_Y:
            self.abajo()
            self.izquierda()
            self.arriba()
            self.derecha()
        elif self.x < END_X and self.y > END_Y:
            self.arriba()
            self.derecha()
            self.abajo()
            self.izquierda()
        elif self.x >= END_X and self.y >= END_Y:
            self.izquierda()
            self.arriba()
            self.derecha()
            self.abajo()
        
        # Smart selection
        if "U" in self.options and (self.y-1, self.x) in self.history and len(self.options) > 1:
            self.options.remove("U")
        if "R" in self.options and (self.y, self.x+1) in self.history and len(self.options) > 1:
            self.options.remove("R")
        if "D" in self.options and (self.y+1, self.x) in self.history and len(self.options) > 1:
            self.options.remove("D")
        if "L" in self.options and (self.y, self.x-1) in self.history and len(self.options) > 1:
            self.options.remove("L")

    def unblock(self):
        self.history.append((self.y, self.x))
        if len(self.history) >= 4:
            if self.history[-4] == self.history[-2] and self.history[-3] == self.history[-1]:
                self.mapa[self.y][self.x].open = False
                self.steps -= 3
                self.history.pop()
                self.history.pop()
                self.history.pop()
                self.y, self.x = self.history[-1]
        # print(self.history[-1])
        
    def derecha(self):
        if self.x != len(self.mapa[self.y])-1 and self.mapa[self.y][self.x+1].open:
            target = self.mapa[self.y][self.x+1].value
            if self.current_hill + 5 >= target:
                self.options.append("R")
    
    def izquierda(self):
        if self.x != 0 and self.mapa[self.y][self.x-1].open:
            target = self.mapa[self.y][self.x-1].value
            if self.current_hill + 5 >= target:
                self.options.append("L")
    
    def arriba(self):
        if self.y != 0 and self.mapa[self.y-1][self.x].open:
            target = self.mapa[self.y-1][self.x].value
            if self.current_hill + 5 >= target:
            # if self.current_hill in [target-1, target]:
                self.options.append("U")
    
    def abajo(self):
        if self.y != len(self.mapa)-1 and self.mapa[self.y+1][self.x].open:
            target = self.mapa[self.y+1][self.x].value
            if self.current_hill + 5 >= target:
                self.options.append("D")
                
    def reset(self):
        self.mapa[self.y][self.x].open = False
        self.history = []
        self.steps = 0
        self.y = START_Y
        self.x = START_X


def part_one():
    mapa = preprocess()
    walker_ = Walker(mapa)
    # for i in range(100):
    while walker_.active:
        walker_.walk()



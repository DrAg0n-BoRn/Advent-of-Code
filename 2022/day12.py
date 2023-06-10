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
# letters_inv = letters[::-1]

START_Y = None
START_X = None
END_Y = None
END_X = None

class Hill():
    def __init__(self, value: int) -> None:
        self.value = value 
        self.open = True
        self.tolerance = 0
        
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
            global START_X, START_Y, END_X, END_Y
            if char == "S":
                elevation = 0
                START_Y = y
                START_X = x
            elif char == "E":
                elevation = 26
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
        self.desde = ""
        self.checkpoint = []
        self.checkpoint_x = None
        self.checkpoint_y = None
    
    def walk(self):
        # check
        self.check()
        # walk
        if self.winner:
            self.active = False
            print("Chicken Dinner", self.steps)
        elif len(self.options) == 0:
            print("Teleport")
            self.reset()
        else:
            self.steps += 1
            match self.options[0]:
                case "U":
                    self.y -= 1
                    self.desde = "D"
                case "L":
                    self.x -= 1
                    self.desde = "R"
                case "D":
                    self.y += 1
                    self.desde = "U"
                case "R":
                    self.x += 1
                    self.desde = "L"
            self.history.append((self.y, self.x))
            self.checkpoint.append((self.y, self.x))
            self.unblock()
            self.is_lava()
            
    
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
        
        # Checkpoint
        if len(self.options) > 2:
            self.checkpoint.clear()
            self.checkpoint_x = self.x
            self.checkpoint_y = self.y
        
        # Smart selection
        if "U" in self.options and (self.y-1, self.x) in self.history and len(self.options) > 1:
            self.options.remove("U")
        if "R" in self.options and (self.y, self.x+1) in self.history and len(self.options) > 1:
            self.options.remove("R")
        if "D" in self.options and (self.y+1, self.x) in self.history and len(self.options) > 1:
            self.options.remove("D")
        if "L" in self.options and (self.y, self.x-1) in self.history and len(self.options) > 1:
            self.options.remove("L")

    def derecha(self):
        if self.x != len(self.mapa[self.y])-1 and self.desde != "R": 
            if self.mapa[self.y][self.x+1].open:
                target = self.mapa[self.y][self.x+1].value
                if self.current_hill in [target -1, target]:
                    self.options.append("R")
    
    def izquierda(self):
        if self.x != 0 and self.desde != "L":
            if self.mapa[self.y][self.x-1].open:
                target = self.mapa[self.y][self.x-1].value
                if self.current_hill in [target -1, target]:
                    self.options.append("L")
    
    def arriba(self):
        if self.y != 0 and self.desde != "U":
            if self.mapa[self.y-1][self.x].open:
                target = self.mapa[self.y-1][self.x].value
                if self.current_hill in [target-1, target]:
                    self.options.append("U")
    
    def abajo(self):
        if self.y != len(self.mapa)-1 and self.desde != "D":
            if self.mapa[self.y+1][self.x].open:
                target = self.mapa[self.y+1][self.x].value
                if self.current_hill in [target-1, target]:
                    self.options.append("D")
                
    def reset(self):
        self.y = self.checkpoint_y
        self.x = self.checkpoint_x
        self.is_lava()
        if not self.mapa[self.y][self.x].open:
            self.y = START_Y
            self.x = START_X
        for y, x in self.checkpoint:
            self.mapa[y][x].open = False
        self.steps -= len(self.checkpoint)
        self.checkpoint.clear()
        self.desde = ""
        # if len(set(self.history[-4:])) == 1:
        #     self.y = START_Y
        #     self.x = START_X
        #     self.steps = 0
        
    def unblock(self):
        if len(self.history) >= 5:
            if self.history[-1] == self.history[-5]:
                self.mapa[self.history[-1][0]][self.history[-1][1]].open = False
                self.mapa[self.history[-2][0]][self.history[-2][1]].open = False
                self.mapa[self.history[-3][0]][self.history[-3][1]].open = False
                self.mapa[self.history[-4][0]][self.history[-4][1]].open = False
                self.steps -= 4
    
    def is_lava(self):
        self.mapa[self.y][self.x].tolerance += 1
        if self.mapa[self.y][self.x].tolerance == 6:
            self.steps -= 6
            self.mapa[self.y][self.x].open = False
            

def part_one():
    mapa = preprocess()
    walker_ = Walker(mapa)
    while walker_.active:
        walker_.walk()
        print(walker_.history[-3:])
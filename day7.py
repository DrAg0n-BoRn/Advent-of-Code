'''
8888b.  88 88""Yb 888888  dP""b8 888888  dP"Yb  88""Yb Yb  dP     8b    d8    db    8888b.  88b 88 888888 .dP"Y8 .dP"Y8 
 8I  Yb 88 88__dP 88__   dP   `"   88   dP   Yb 88__dP  YbdP      88b  d88   dPYb    8I  Yb 88Yb88 88__   `Ybo." `Ybo." 
 8I  dY 88 88"Yb  88""   Yb        88   Yb   dP 88"Yb    8P       88YbdP88  dP__Yb   8I  dY 88 Y88 88""   o.`Y8b o.`Y8b 
8888Y"  88 88  Yb 888888  YboodP   88    YbodP  88  Yb  dP        88 YY 88 dP""""Yb 8888Y"  88  Y8 888888 8bodP' 8bodP' 
'''

# --- Preprocessing ---
def preprocess():
    with open("./inputs/input7.txt") as file:
        data = [line.strip() for line in file.readlines()]
    # Build home directory
    home = {"daxiao": 0, "control": True}
    to_pop = 0
    for index, line in enumerate(data):
        if "$" in line: 
            if "$ ls" in line or "$ cd /" in line:
                to_pop += 1
                continue
            else:
                break
        elif "dir" in line[:3]:
            home[line[4:]] = {}
        else:
            home["daxiao"] += int(line.split(sep=" ")[0])
        to_pop += 1
    # Pop used lines
    new_data = data[::-1]
    for _ in range(to_pop):
        new_data.pop()
    data = new_data[::-1]
    
    return data, home


# --- PART I ---
sizes = []
def part_one():
    data, home = preprocess()
    history = [home]
    level = 0
    for line in data:
        if "$ cd .." in line:
            history.pop()
            level -= 1
        elif "$ cd" in line:
            history[level]["control"] = True
            # add pointer to current location
            dir_ = line[5:]
            try:
                history[level][dir_]
            except KeyError:
                history[level][dir_] = {}
            finally:
                # change history index (pointer)
                history.append(history[level][dir_])
                level += 1
            # add size
            try:
                history[level]["daxiao"]
            except KeyError:
                history[level]["daxiao"] = 0
            # add control
            try: 
                history[level]["control"]
            except KeyError:
                history[level]["control"] = False
        elif "$ ls" in line or "dir" in line[:3]:
            continue
        else:
            # add level size if not repeated
            if history[level]["control"] == False:
                for pointer in history:
                    pointer["daxiao"] += int(line.split(sep=" ")[0])
    
    # Parse directories
    recursion(home)
    # Get answer
    total = 0
    for size in sizes:
        if size <= 100000:
            total += size
    print(total)

def recursion(dict_: dict):
    for key, value in dict_.items():
        if type(value) is dict:
            recursion(value)
        elif type(value) is int:
            sizes.append(value)


# --- PART II ---

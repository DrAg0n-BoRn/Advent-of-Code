'''
     _,---.     _,.---._                    ,----.    ,-,--.  ,--.--------.                ___    ,---.                  .-._           ,----.    ,-,--.    ,-,--.  
  .-`.' ,  \  ,-.' , -  `.   .-.,.---.   ,-.--` , \ ,-.'-  _\/==/,  -   , -\        .-._ .'=.'\ .--.'  \      _,..---._ /==/ \  .-._ ,-.--` , \ ,-.'-  _\ ,-.'-  _\ 
 /==/_  _.-' /==/_,  ,  - \ /==/  `   \ |==|-  _.-`/==/_ ,_.'\==\.-.  - ,-./       /==/ \|==|  |\==\-/\ \   /==/,   -  \|==|, \/ /, /==|-  _.-`/==/_ ,_.'/==/_ ,_.' 
/==/-  '..-.|==|   .=.     |==|-, .=., ||==|   `.-.\==\  \    `--`\==\- \          |==|,|  / - |/==/-|_\ |  |==|   _   _\==|-  \|  ||==|   `.-.\==\  \   \==\  \    
|==|_ ,    /|==|_ : ;=:  - |==|   '='  /==/_ ,    / \==\ -\        \==\_ \         |==|  \/  , |\==\,   - \ |==|  .=.   |==| ,  | -/==/_ ,    / \==\ -\   \==\ -\   
|==|   .--' |==| , '='     |==|- ,   .'|==|    .-'  _\==\ ,\       |==|- |         |==|- ,   _ |/==/ -   ,| |==|,|   | -|==| -   _ |==|    .-'  _\==\ ,\  _\==\ ,\  
|==|-  |     \==\ -    ,_ /|==|_  . ,'.|==|_  ,`-._/==/\/ _ |      |==|, |         |==| _ /\   /==/-  /\ - \|==|  '='   /==|  /\ , |==|_  ,`-._/==/\/ _ |/==/\/ _ | 
/==/   \      '.='. -   .' /==/  /\ ,  )==/ ,     /\==\ - , /      /==/ -/         /==/  / / , |==\ _.\=\.-'|==|-,   _`//==/, | |- /==/ ,     /\==\ - , /\==\ - , / 
`--`---'        `--`--''   `--`-`--`--'`--`-----``  `--`---'       `--`--`         `--`./  `--` `--`        `-.`.____.' `--`./  `--`--`-----``  `--`---'  `--`---'  
'''

# --- Preprocessing ---
def forest_overseer():
    with open("./inputs/input8.txt", "r") as file:
        forest = [line.strip() for line in file.readlines()]
    return forest    


# --- PART I ---
def part_one():
    forest = forest_overseer()
    visible = (len(forest)*2 + len(forest[0])*2 - 4)
    unvisible = 0
    for i in range(1, len(forest) -1, 1):
        for j in range (1, len(forest[i]) - 1, 1):
            tree = forest[i][j]
            # Check trees
            arriba = []
            abajo = []
            derecha = []
            izquierda = []
            for u in range(0, i, 1):
                arriba.append(int(forest[u][j]))
            for d in range(-1, -(len(forest)-i), -1):
                abajo.append(int(forest[d][j]))
            for r in range(j+1, len(forest[i]), 1):
                derecha.append(int(forest[i][r]))
            for l in range(j-1, -1, -1):
                izquierda.append(int(forest[i][l]))
            # Check condition
            alrededor = [max(arriba), max(abajo), max(derecha), max(izquierda)]
            if int(tree) <= min(alrededor):
                unvisible += 1
            else:
                visible += 1    
    print(f"Visible: {visible}\nUnvisible: {unvisible}")


# --- PART II ---
def part_two():
    forest = forest_overseer()
    all_scores = []
    for i in range(1, len(forest) -1, 1):
        for j in range (1, len(forest[i]) - 1, 1):
            tree = int(forest[i][j])
            # Check trees
            arriba = 0
            abajo = 0
            derecha = 0
            izquierda = 0
            for u in range(i-1, -1, -1):
                arriba += 1
                up_tree = int(forest[u][j])
                if up_tree >= tree:
                    break
            for d in range(i+1, len(forest), 1):
                abajo += 1
                down_tree = int(forest[d][j])
                if down_tree >= tree: 
                    break
            for r in range(j+1, len(forest[i]), 1):
                derecha += 1
                right_tree = int(forest[i][r])
                if right_tree >= tree:
                    break
            for l in range(j-1, -1, -1):
                izquierda += 1
                left_tree = int(forest[i][l])
                if left_tree >= tree: 
                    break
            # get scenic score
            score = arriba*abajo*derecha*izquierda
            all_scores.append(score)
    print(f"Highest scenic score: {max(all_scores)}")

part_two()

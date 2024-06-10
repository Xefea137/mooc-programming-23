#if __name__ == "__main__":



'''import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi,
        # square the difference using (yi - prediction)**2,
        # and add up all the differences in variable sse
        predicted_price = xi @ c
        subtract = yi - predicted_price
        squared = subtract**2
        sse += squared
        # sse = np.sum((y - (X @ c)y)**2)
    print(np.sum((y - (X @ c))**2))
    print(sse)

squared_error(X, y, c)'''


'''import matplotlib.pyplot as plt
from matplotlib import cm

import numpy as np
import random

N = 100
steps = 3000
tracks = 50

def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        T = max(0, ((steps - step)/steps)**3-.005)
        for i in range(tracks):
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            if S_new > S_old:
                x[i], y[i] = x_new, y_new
            else:
                if T == 0:
                    prob = 0
                else:
                    prob = np.exp(-(S_old - S_new) / T)
                if random.random() < prob:
                    x[i] = x_new
                    y[i] = y_new

    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])) 
main()'''


'''plt.xlim(0, N-1)
plt.ylim(0, N-1)
plt.imshow(h, cmap=cm.gist_earth)
plt.scatter([peak_y], [peak_x], color='red', marker='+', s=100)

for j in range(tracks):

    c = cm.tab20(j/tracks)    # use different colors for different tracks 
    plt.scatter([y[j]], [x[j]], color=c, s=20)

plt.show()'''


'''import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Polygon

import math, random        	# just for generating random mountains                                 	 
import numpy as np

n = 10000 # size of the problem: number of possible solutions x = 0, ..., n-1

# generate random mountains                                                                               	 
def mountains(n):
    h = [0]*n
    for i in range(50):
        c = random.randint(20, n-20)
        w = random.randint(3, int(math.sqrt(n/5)))**2
        s = random.random()
        h[max(0, c-w):min(n, c+w)] = [h[i] + s*(w-abs(c-i)) for i in range(max(0, c-w), min(n, c+w))]

    # scale the height so that the lowest point is 0.0 and the highest peak is 1.0
    low = min(h)
    high = max(h)
    h = [y - low for y in h]
    h = [y / (high-low) for y in h]
    return h

h = mountains(n)

# start at a random place
x0 = random.randint(1, n-1)
x = x0

# keep climbing for 5000 steps
steps = 5000

def main(h, x):
    n = len(h)
    # the climbing starts here
    for step in range(steps):
        # this is our temperature to to be used for simulated annealing
        # it starts large and decreases with each step. you don't have to change this
        T = 2*max(0, ((steps-step*1.2)/steps))**3

        # let's try randomly moving (max. 1000 steps) left or right
        # making sure we don't fall off the edge of the world at 0 or n-1
        # the height at this point will be our candidate score, S_new
        # while the height at our current location will be S_old
        x_new = random.randint(max(0, x-1000), min(n-1, x+1000))

        if h[x_new] > h[x]:
            x = x_new           # the new position is higher, go there
        else:
            if T == 0:
                prob = 0
            else:
                prob = np.exp(-(h[x] - h[x_new]) / T)
            if random.random() < prob:
                x = x_new
            # pass               # add simulated annealing here. remember to handle T=0
                               # correctly!

    return x

x = main(h, x0)
print("ended up at %d, highest point is %d" % (x, np.argmax(h)))


def gradient_fill(x, y, fill_color=None, ax=None, **kwargs):
    if ax is None:
        ax = plt.gca()

    line, = ax.plot(x, y, **kwargs)
    if fill_color is None:
        fill_color = line.get_color()

    zorder = line.get_zorder()
    alpha = line.get_alpha()
    alpha = 1.0 if alpha is None else alpha

    z = np.empty((100, 1, 4), dtype=float)
    rgb = mcolors.colorConverter.to_rgb(fill_color)
    z[:,:,:3] = rgb
    z[:,:,-1] = np.linspace(0, alpha, 100)[:,None]

    xmin, xmax, ymin, ymax = x.min(), x.max(), y.min(), y.max()
    im = ax.imshow(z, aspect='auto', extent=[xmin, xmax, ymin, ymax],
                   origin='lower', zorder=zorder)

    xy = np.column_stack([x, y])
    xy = np.vstack([[xmin, ymin], xy, [xmax, ymin], [xmin, ymin]])
    clip_path = Polygon(xy, facecolor='none', edgecolor='none', closed=True, zorder=-100)
    ax.add_patch(clip_path)
    im.set_clip_path(clip_path)

    return line, im

def plot_exercise6_intermediate():
    xx = np.array(list(range(n)))
    yy = np.array(h)
    plt.figure(figsize=(10,2))
    plt.gca().set_ylim(0, 1.2)
    plt.gca().set_xlim(0, n)
    plotlim = plt.gca().get_xlim() + plt.gca().get_ylim()  
    cmap = mpl.cm.Blues(np.linspace(.2,.6,100))
    cmap = mpl.colors.ListedColormap(cmap[10:,:-1])
    plt.imshow([[0,0],[1,1]], cmap=cmap, interpolation='bicubic', extent=plotlim, zorder=-200)  
    plt.grid(False)
    plt.fill_between(xx, 0, yy, color='rosybrown', zorder=-150)
    gradient_fill(xx, yy, 'white', plt.gca(), color='None')
    plt.plot([x0], [h[x0]], color='k', marker='s', markersize=10, zorder=50)
    plt.plot([x], [h[x]], color='r', marker='*', markersize=15, zorder=51) 

    plt.show()

plot_exercise6_intermediate()
'''

'''class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"

class RecipeBook:
    def __init__(self):
        self.__recipe_book = []

    def add_recipe(self, recipe: Recipe):
        self.__recipe_book.append(recipe)

    def remove_recipe(self, recipe):
        for recipes in self.__recipe_book:
            if recipes.name == recipe:
                self.__recipe_book.remove(recipes)
                return True

    def recipe_by_name(self, name):
        for recipes in self.__recipe_book:
            if recipes.name == name:
                return recipes
        return None

    def recipes_containing_ingredients(self, ingredient_list):
        recipes_list = []
        for recipes in self.__recipe_book:
            for ingredient in ingredient_list:
                if ingredient not in recipes.ingredients:
                    break
            else:
                recipes_list.append(recipes)
        
        return recipes_list

    def recipes_within_time(self, time: int):
        recipes_list = []
        for recipes in self.__recipe_book:
            if recipes.time <= time:
                recipes_list.append(recipes)
        
        return recipes_list

    def recipes_with_all_ingredients(self, ingredient_list):
        recipes_list = []
        for recipes in self.__recipe_book:
            for recipes_ingredient in recipes.ingredients:
                if recipes_ingredient not in ingredient_list:
                    break
            else:
                recipes_list.append(recipes)

        return recipes_list            

    def all_recipes(self):
        new_recipe_book = []
        for recipes in self.__recipe_book:
            new_recipe_book.append(recipes)
        
        return new_recipe_book

    def __str__(self):
        print("RecipeBook:")
        return "\n".join([f"Recipe(name='{recipes.name}', ingredients={recipes.ingredients}, time={recipes.time}, instructions='{recipes.instructions}')" 
                        for recipes in self.__recipe_book])

class RecipeBookApplication:
    def __init__(self):
        self.recipe = RecipeBook()
    
    def commands(self):
        print("Commands:")
        print("0 - Exit")
        print("1 - Add recipe")
        print("2 - Remove recipe")
        print("3 - Search recipe by name")
        print("4 - Search recipe by ingredients")
        print("5 - Search recipe by preparation time")
        print("6 - Search recipe by available ingredients")
        print("7 - Return all recipes")
        print("8 - Clear memory")

    def execute(self):
        with open("recipes.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                name, ingredients, time, instructions = parts
                self.recipe.add_recipe(Recipe(name, ingredients, time, instructions))

        print("Recipe book program")
        self.commands()
        while True:
            try:
                command = int(input("Enter command: "))
                if command == 0:
                    break
                elif command == 1:
                    self.add_recipe()
                elif command == 2:
                    self.remove_recipe()
                elif command == 3:
                    self.recipe_by_name()
                elif command == 4:
                    self.recipes_containing_ingredients()
                elif command == 5:
                    self.recipes_within_time()
                elif command == 6:
                    self.recipes_with_all_ingredients()
                elif command == 7:
                    self.all_recipes()
                elif command == 8:
                    self.clear_memory()
            except ValueError:
                self.commands()

    def add_recipe(self):
        name = input("Enter recipe name: ")
        for recipes in self.recipe.all_recipes():
            if name in recipes.name:
                print("Recipe already exists")
                return
        ingredients = input("Enter recipe ingredients separated by comma: ")
        ingredient_list = ingredients.split(',')
        time = int(input("Enter recipe cooktime (min): "))
        instructions = input("Enter recipe instructions: ")
        self.recipe.add_recipe(Recipe(name, ingredient_list, time, instructions))
        print(f"Added recipe {name}")

        with open("recipes.txt", "a") as file:
            file.write(f"{name};{ingredients};{time};{instructions}\n")

    def remove_recipe(self):
        name = input("Enter name of recipe to remove: ")
        if self.recipe.remove_recipe(name):
            print(f"Removed recipe {name}")
        else:
            print(f"No recipe found with name {name}")

        with open("recipes.txt", "r") as file:
            data = file.readlines()
        
        new_data = []
        for recipe in data:
            if name not in recipe:
                new_data.append(recipe)

        with open("recipes.txt", "w") as file:
            file.writelines(new_data)

    def recipe_by_name(self):
        name = input("Enter recipe name to search: ")
        recipe = self.recipe.recipe_by_name(name)
        if recipe == None:
            print(f"No recipe found with name {name}")
        else:
            print(recipe)

    def recipes_containing_ingredients(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas:")
        ingredient_list = ingredients.split(",")
        recipe_list = self.recipe.recipes_containing_ingredients(ingredient_list)
        if not recipe_list:
            print(f"No recipe found with ingredients {recipe_list}")
        else:
            print(f"Found recipes with ingredients {ingredient_list}")
            for recipes in recipe_list:
                print(recipes)

    def recipes_within_time(self):
        time = int(input("Enter the preparation time of the recipe you're looking for (min): "))
        recipe_list = search.recipe.recipes_within_time(time)
        if not recipe_list:
            print(f"No recipe found with preparation time {time} min")
        else:
            print(f"Found recipes with preparation time {time} min:")
            for recipes in recipe_list:
                print(recipes)

    def recipes_with_all_ingredients(self):
        ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas:")
        ingredient_list = ingredients.split(",")
        recipe_list = self.recipe.recipes_with_all_ingredients(ingredient_list)
        if not recipe_list:
            print(f"No recipe found with ingredients {recipe_list}")
        else:
            print(f"Found recipes with ingredients {ingredient_list}")
            for recipes in recipe_list:
                print(recipes)

    def all_recipes(self):
        all_recipes = self.recipe.all_recipes()
        if not all_recipes:
            print("No recipes found")
        else:
            print("Found recipes:")
            for recipes in all_recipes:
                print(recipes)

    def clear_memory(self):
        all_recipes = self.recipe.all_recipes()
        for recipe in all_recipes:
            self.recipe.remove_recipe(recipe.name)
        print("Memory cleared")

        with open("recipes.txt", "w") as file:
            pass
                
if __name__ == "__main__":
    x = RecipeBookApplication()
    x.execute()'''


'''import pygame

class Sokoban:
    def __init__(self):
        pygame.init()
        
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)             #6
        self.width = len(self.map[0])           #17
        self.scale = self.images[0].get_width() #50

        window_height = self.scale * self.height    #300
        window_width = self.scale * self.width      #850
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        self.game_font = pygame.font.SysFont("Arial", 24)

        pygame.display.set_caption("Sokoban")

        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "target", "box", "robot", "done", "target_robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.moves = 0

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #move(y, x)
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)

                if event.key == pygame.K_F2:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()

            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((0, 0, 0))

        for y in range(self.height):
            for x in range(self.width):
                #for list we have to get the height(row) and then the width(column)
                square = self.map[y][x]
                #for graphics we give width(x) and then height(y)
                self.window.blit(self.images[square], (x * self.scale, y * self.scale))

        game_text = self.game_font.render("Moves: " + str(self.moves), True, (255, 0, 0))
        self.window.blit(game_text, (25, self.height * self.scale + 10))

        game_text = self.game_font.render("F2 = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, self.height * self.scale + 10))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, self.height * self.scale + 10))

        if self.game_solved():
            game_text = self.game_font.render("Congratulations, you solved the game!", True, (255, 0, 0))
            game_text_x = self.scale * self.width / 2 - game_text.get_width() / 2
            game_text_y = self.scale * self.height / 2 - game_text.get_height() / 2
            pygame.draw.rect(self.window, (0, 0, 0), (game_text_x, game_text_y, game_text.get_width(), game_text.get_height()))
            self.window.blit(game_text, (game_text_x, game_text_y))

        pygame.display.flip()

    def find_robot(self ):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)

    def move(self, move_y, move_x):
        if self.game_solved():
            return

        robot_old_y, robot_old_x = self.find_robot() 
        robot_new_y = robot_old_y + move_y
        robot_new_x = robot_old_x + move_x

        #robot hit wall as 1 is wall
        if self.map[robot_new_y][robot_new_x] == 1:
            return

        #for moving the box
        #if robot in 3(box) or 5(box on target)
        if self.map[robot_new_y][robot_new_x] in [3, 5]:
            box_new_y = robot_new_y + move_y
            box_new_x = robot_new_x + move_x

            #no change if new box location in 1,3,5
            if self.map[box_new_y][box_new_x] in [1, 3, 5]:
                return

            #-3 is box to floor and +3 is floor to box in the load_image images list or target to box on targer
            #so the old location of box(which is new robot location) is becoming a floor(next part robot gets on it) and the new location is getting the box
            self.map[robot_new_y][robot_new_x] -= 3
            self.map[box_new_y][box_new_x] += 3

        #-4 is robot to floor and +4 is floor to robot in images list
        #old location of robot is becoming a floor and the new location is getting a robot
        self.map[robot_old_y][robot_old_x] -= 4
        self.map[robot_new_y][robot_new_x] += 4

        self.moves += 1

    def game_solved(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [2, 6]:
                    return False
        return True

if __name__ == "__main__":
    Sokoban()'''

'''import string
name = "Moe Leah Elena"
for item in range(len(name)):
    if name[item] in string.ascii_letters:
        print(name[item])'''

'''from datetime import datetime
time_now = datetime.now()
midsummer = datetime(2021, 6, 26)
print(time_now)
print(midsummer)

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
print(person1.values())
print(person1.keys())
print(person1.items())'''
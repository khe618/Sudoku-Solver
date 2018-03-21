from random import random, shuffle, sample



class Individual:
    def __init__(self):
        self.arr = []
        self.mistakes = 0
        self.fitness_function()
    def __init__(self, arr = False):
        self.arr = []
        self.mistakes = 0
        if arr != False:
            for a in arr:
                temp = a[:]
                availiable_numbers = list(numbers - set(a))
                shuffle(availiable_numbers)
                for i in range(9):
                    if temp[i] == 0:
                        temp[i] = availiable_numbers.pop()
                self.arr.append(temp)
            self.fitness_function()
    def fitness_function(self):
        for i in range(9):
            self.mistakes += len(numbers - self.get_column(i))
        for i in range(3):
            for j in range(3):
                self.mistakes += len(numbers - self.get_box(i, j))
    def get_column(self, i):
        column = []
        for row in self.arr:
            column.append(row[i])
        return set(column)
    def get_box(self, i, j):
        box = []
        y_bound = i * 3
        x_bound = j * 3
        for m in range(y_bound, y_bound + 3):
            for n in range(x_bound, x_bound + 3):
                box.append(self.arr[m][n])
        return set(box)    
    def mutate(self):
        for i in range(9):
            if random() < 0.1: #mutation rate
                (i1, i2) = sample(availiable_indices[i], k = 2)
                (self.arr[i][i1], self.arr[i][i2]) = (self.arr[i][i2], self.arr[i][i1])

def create_children(n):
    children_arr = []
    cum_prbs = [0]
    for individual in population:
        cum_prbs.append( cum_prbs[-1] + (1 / (individual.mistakes ** 2) ) )
    cum_prbs = cum_prbs[1:]
    cum_prbs = [x / cum_prbs[-1] for x in cum_prbs]
    while len(children_arr) < n:
        rand = random()
        for k, prb in enumerate(cum_prbs):
            if rand <= prb:
                parent_1 = population[k]
                break
        rand = random()
        for k, prb in enumerate(cum_prbs):
            if rand <= prb:
                parent_2 = population[k]
                break
        (temp_1, temp_2) = ([], [])
        for i in range(9):
            temp_1.append(parent_1.arr[i][:])
            temp_2.append(parent_2.arr[i][:])
        crossing_point = int(random() * 3) + 1  
        for i in range(crossing_point):
            (temp_1[i], temp_2[i]) = (temp_2[i], temp_2[i])
        child_1 = Individual()
        child_2 = Individual()
        (child_1.arr, child_2.arr) = (temp_1, temp_2)
        child_1.fitness_function()
        child_2.fitness_function()
        children_arr.append(child_1)
        children_arr.append(child_2)
    return children_arr

def replace(n):
    #n must be even to maintain constant population 
    children = create_children(n)
    population[len(population) - n:] = children

numbers = {1,2,3,4,5,6,7,8,9}
arr = [[4, 0, 0, 0, 0, 6, 0, 0, 0],
       [0, 6, 0, 0, 0, 0, 0, 0, 9],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 2, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 3, 0, 6, 0, 0, 2, 0],
       [1, 0, 0, 0, 0, 0, 9, 0, 0],
       [8, 0, 0, 0, 0, 5, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 5]]
availiable_indices = []
for a in arr:
    t = []
    for k, number in enumerate(a):
        if number == 0:
            t.append(k)
    availiable_indices.append(t)
population = [Individual(arr) for i in range(200)]
n = 150 #replacement number
for i in range(2000): #generations
    population.sort(key = lambda x: x.mistakes)
    print(population[0].mistakes)
    replace(n)
    for i in range(1, len(population)):
        population[i].mutate()
        

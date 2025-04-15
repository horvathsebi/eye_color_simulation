import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

eye_colors = ('brown', 'blue')
allels = ('B', 'b')

# creating a person class with the needed attributes
class Person:
    def __init__(self, allel, generation, eye_color):
        self.allel = allel
        self.generation = generation
        self.eye_color = eye_color

emberek = []


# creating the first generation
for number in range(1000):
    allel = ''.join(random.choices(allels, k=2))
    eye_color = 'brown' if 'B' in allel else 'blue'
    person = Person(allel, generation=1, eye_color=eye_color)
    emberek.append(person)

ember_data = pd.DataFrame([{'allel': person.allel, 'eye color': person.eye_color, 'generation': person.generation} for person in emberek])


# function for random sampling parents and creating children
def reproduce(parent1, parent2):
    child_allel = random.choice(parent1.allel) + random.choice(parent2.allel)
    if child_allel == 'Bb' or child_allel == 'BB' or child_allel == 'bB':
        return child_allel, 'brown'
    else:
        return child_allel, 'blue'


# function for simulating random population growth for the generation
def simulating_population(ember_data, num_gens):
    current_generation = ember_data.copy()
    for gens in tqdm(range(num_gens), desc="simulating gens..."):
        new_gen = []
        for _ in range(len(current_generation) // 2):
            parent1 = current_generation.sample().iloc[0]
            parent2 = current_generation.sample().iloc[0]

            for _ in range(random.randint(0, 4)):
                child_allel, child_eye_color = reproduce(parent1, parent2)
                child = Person(child_allel, parent1['generation'] + 1, child_eye_color)
                new_gen.append({'allel': child.allel, 'generation': child.generation, 'eye color': child.eye_color})

        new_gen_df = pd.DataFrame(new_gen)
        ember_data = pd.concat([ember_data, new_gen_df], ignore_index=True)
        current_generation = new_gen_df

    return ember_data


# function to plot the simulations results over generations
def plot_one_simulaiton(simulation):
    counts = simulation.groupby(['generation', 'eye color']).size().unstack(fill_value=0)
    counts.plot(kind='line', color=['blue', 'brown'])
    plt.title('eye color distribution across generations')
    plt.xlabel('generation')
    plt.ylabel('number of people')
    plt.legend(title='eye color')
    plt.grid()
    plt.show()


# plot_one_simulaiton(simulation)


# function to compare results over a number of futures
def monte_carlo(ember_data, num_futures):
    distr = []
    for n in tqdm(range(num_futures), desc="simulating futures..."):
        rand_sim = simulating_population(ember_data,10)
        rand_sim = rand_sim.groupby(['generation', 'eye color']).size().unstack(fill_value=0)
        rand_sim['run_' + str(n)] = rand_sim['blue']/rand_sim['brown']
        distr.append(rand_sim['run_' + str(n)])

    distr_df = pd.DataFrame(distr).T
    return distr_df


mt_simulation = monte_carlo(ember_data,10)
mt_simulation.to_excel('eye_color_simulation/monte_carlo.xlsx')

# function to plot all the runs (only works with small number of runs, becomes unreadable) 
def plot_blue_to_brown_mt(distr_df):
    distr_df.iloc[:, 1:].plot(legend=False)
    plt.xlabel("generations")
    plt.ylabel("blue to brown ratio in generation")
    plt.show()

plot_blue_to_brown_mt(mt_simulation)







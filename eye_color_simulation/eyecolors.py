import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

eye_colors = ('brown', 'blue')
allels = ('B', 'b')


class Person:
    def __init__(self, allel, generation, eye_color):
        self.allel = allel
        self.generation = generation
        self.eye_color = eye_color
        


emberek = []

for number in range(1000):
    allel = ''.join(random.choices(allels, k=2))
    eye_color = 'brown' if 'B' in allel else 'blue'
    person = Person(allel, generation=1, eye_color=eye_color)
    emberek.append(person)

ember_data = pd.DataFrame([{'allel': person.allel, 'eye color': person.eye_color, 'generation': person.generation} for person in emberek])


def reproduce(parent1, parent2):
    child_allel = random.choice(parent1.allel) + random.choice(parent2.allel)
    if child_allel == 'Bb' or child_allel == 'BB' or child_allel == 'bB':
        return child_allel, 'brown'
    else:
        return child_allel, 'blue'

def simulating_population(ember_data, num_iter):
    current_generation = ember_data.copy()
    for generations in tqdm(range(num_iter), desc="simulating gens..."):
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

num_iter = int(input('how many generations?: '))


simulation = simulating_population(ember_data, num_iter)

print(simulation.head(4))


#simulation.to_excel('szemek.xlsx')



counts = simulation.groupby(['generation', 'eye color']).size().unstack(fill_value=0)


counts.plot(kind='line', color=['blue', 'brown'])
plt.title('eye color distribution across generations')
plt.xlabel('generation')
plt.ylabel('number of people')
plt.legend(title='eye color')
plt.grid()
plt.show()


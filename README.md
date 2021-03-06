# easy gene - easy to use genetic algorythm

Easy gene is a simple way to introduce genetic algorythms into your project. 
With a total line count of 37 lines.
Insperation for this project was https://www.youtube.com/watch?v=RxTfc4JLYKs.  
## usage example:
Lets say we are trying to create a ideal animal. In the real world the score_animal(animal) function is unknown. 
We have two parameters, arm_length and torso_length. In this example we start with a 
population of 8 animals with distributed values. We use mutation rates of 0.2 for both 
parameters, save two parents every generation, and evolve 100 times. 
```python
from easy_gene import evolve


def score_animal(animal): # max score is when the value is 3, 6
    return 1 / (abs(animal['arm_length'] - 3) + abs(animal['torso_length'] - 6) + 1)

population = [
    {'arm_length': 2.0, 'torso_length': 2.0},
    {'arm_length': 6.0, 'torso_length': 7.0},
    {'arm_length': 4.0, 'torso_length': 2.0},
    {'arm_length': 9.0, 'torso_length': 5.0},
    {'arm_length': 4.0, 'torso_length': 2.0},
    {'arm_length': 9.0, 'torso_length': 5.0},
    {'arm_length': 4.0, 'torso_length': 2.0},
    {'arm_length': 9.0, 'torso_length': 5.0},
]

mutation_rates = {'arm_length': 0.2, 'torso_length': 0.2}
num_parents = 2

iterations = 100
max_scores = []
for _ in range(iterations):
    scores = [score_animal(animal) for animal in population]
    population = evolve(population, scores, num_parents, mutation_rates)
    max_scores.append(max(scores))
        
print(population[0])
```
result:
```
{'arm_length': 3.1127586555075375, 'torso_length': 6.533470856616043}
```
max scores:
![alt text](https://github.com/thomsn/easy_gene/blob/master/Figure_1.png)
- x axis = iteration
- y axis = score
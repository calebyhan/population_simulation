import matplotlib.pyplot as plt

import population

population = population.Population(1000, 100, 10, 5, 25, 1)
population.start()
stats = population.get_stats()

print(stats)

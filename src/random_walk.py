# NumPy is imported, seed is set
import numpy as np
import matplotlib.pyplot as plt

# Initialize random_walk
random_walk = [0]
x_axis = list(range(100))

# Complete the ___
for x in x_axis:
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step, and make sure step can't go below 0
    if dice <= 2:
        step = max(10,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

plt.plot(random_walk)

plt.savefig('./figures/prueba.png')

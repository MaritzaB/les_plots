import math
import matplotlib as plt
import time

cosine_x = 0
x = (3.1416/4)

inicio = time.time_ns()
coseno_x1 = math.cos(x)
final = time.time_ns()
total_time_1 = ((final - inicio)/1e8)

print(f"coseno de {x} es ", math.cos(x), total_time_1)

inicio = time.time_ns()
for number in range(0,10,1):
    dos_n = (2*number)
    factorial = math.factorial(dos_n)
    cosine_x += ((-1)**number)*(x**dos_n/factorial)

final = time.time_ns()
total_time = ((final - inicio)/1e8)
print(cosine_x, total_time)

e_value = 0
for n in range(1,100000):
    e_value += (1 + (1/n))**n

print(e_value)
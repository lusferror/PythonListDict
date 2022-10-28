#Remember import random function here:
import random

my_list = [4,5,734,43,45]

for x in range(0,10):
    numero= random.randint(1,999)
    my_list.append(numero)
#The magic is here:
print(my_list)
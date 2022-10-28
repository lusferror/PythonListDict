arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sum_odds(array):
    aux=0
    for i in arr:
        if i%2!=0:
            aux+=i
    return aux

print(str(sum_odds(arr)))

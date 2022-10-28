
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def primeraLetra(item):
    return item[0]=="R"
resulting_names= list(filter(primeraLetra, all_names))
print(resulting_names)





par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
array=[]
for i in par:
    if i!=" ":
        array.append(i.lower())
array=set(array)
for key in array:
    cLetra=0
    for i in par:
        if i.lower()==key:
            cLetra+=1
    counts[key]=cLetra 

print(counts)


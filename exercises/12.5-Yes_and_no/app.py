theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def siyno(item):
    if item==0:
        return "woko"
    else:
        return "wiki"

new_list= list(map(siyno, theBools))

print(new_list)

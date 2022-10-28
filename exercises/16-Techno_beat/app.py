def lyrics_generator(array):
    aux=""
    for i in range(0,len(array)-1):
        if i==0:
            if array[i-1]==1 and array[i]==1 and array[i+1]==1:
                aux+=" !!!Break the base!!! "
        elif array[i]==0:
            aux+=" Boom "
        elif array[i]==1:
            aux+=" Drop the base "
    return aux


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))




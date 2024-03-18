new_array=[] # an array to hold all of the results 
# array with five numbers 
array = [0,1,2,3,4]
for i in range(len(array)): # the array has five values, so this is n=5 
    for j in range(len(array)): # still the same array so n = 5 
        new_array.append(i*j) # every computation made is stored here 

print(len(new_array))
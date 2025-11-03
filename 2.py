def generate_combinations(elements, start_index, current_combinations, k):
    count = 0
    count = count + 1;
    if len(current_combinations) == k:
        print("combinations are:", current_combinations)
        return 
    for i in range (len(elements)):
        current_combinations.append(elements[i])
        generate_combinations(elements , i+1,current_combinations,k)
        current_combinations.pop()
    


elements = ['A','B','C','D']
k = 3
generate_combinations(elements,0,[],k)





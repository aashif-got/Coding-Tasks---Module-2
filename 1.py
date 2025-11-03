


def generate_permutation_(elements, current_purmutations, used):
    if len(current_purmutations) ==  len(elements):
        print("permutations: ", current_purmutations)
        return
    for i in range (len(elements)):
        if not used[i]:
            used[i] = True
            current_purmutations.append(elements[i])
            generate_permutation_(elements, current_purmutations,used)
            current_purmutations.pop()
            used[i] = False
elements = ['A', 'B', 'C']
used = [False] * len(elements)
generate_permutation_(elements,[],used)







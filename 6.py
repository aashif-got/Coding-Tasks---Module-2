
def generate_combinations(elements, start_index, current_combination, all_combinations):
    
    all_combinations.append(current_combination[:])

   
    for i in range(start_index, len(elements)):
        current_combination.append(elements[i])
        generate_combinations(elements, i + 1, current_combination, all_combinations)
        current_combination.pop()  



def knapsack(value, weight, item_list, max_weight):
    n = len(item_list)
    max_value = 0
    best_combination = []

    
    all_combinations = []
    generate_combinations(list(range(n)), 0, [], all_combinations)

    # Check each combination
    for combo in all_combinations:
        temp_weight = 0
        temp_value = 0
        items_selected = []

        for i in combo:
            temp_weight += weight[i]
            temp_value += value[i]
            items_selected.append(item_list[i])

        if temp_weight <= max_weight and temp_value > max_value:
            max_value = temp_value
            best_combination = items_selected

    return max_value, best_combination



items  = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
weights = [2,4,3,5,6,8]
values = [3,6,2,4,7,1]
capacity = 16


best_value, best_items = knapsack(values, weights, items, capacity)


print("Best combination of items:", best_items)
print("Maximum value:", best_value)
print("Total weight:", sum(weights[items.index(i)] for i in best_items))

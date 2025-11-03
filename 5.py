#knapsack problem 
def knapsack(value, weight, item_list, max_weight):
    n = len(item_list)
    max_value = 0
    best_combination = ""
    for comb in range (2**n):
        temp_weight = 0
        temp_value = 0
        combination = bin(comb)[2:].zfill(n)
        items_selected = []
        for i in range (n):
            if combination[i] == '1':
                temp_weight = temp_weight + weight[i]
                temp_value = temp_value + value[i]

        if temp_weight <= max_weight and temp_value > max_value:
            max_value = temp_value
            best_combination = combination
    return max_value, best_combination

items  = ['A1', 'A2','A3','A4','A5','A6']
weight = [2,4,3,5,6,8]
value = [3,6,2,4,7,1]
capacity = 16
best_value, best_combination = knapsack(value, weight, items, capacity)
print("Combination in binary:", best_combination)
print("Maximum value:", best_value)
print("Items selected:", end= "")
for i in range (len(items)):
    if best_combination[i] == '1':
        print(items[i], end ="")


#Travelling Salesman Problem (TSP) – Brute force Approach

def generate_permutation_(elements, current_, used, all_perm):
    if len(current_) == len(elements):
        all_perm.append(current_[:])  
        return
    for i in range (len(elements)):
        if not used[i]:
            used[i] = True
            current_.append(elements[i])
            generate_permutation_(elements, current_,used,all_perm)
            current_.pop()
            used[i] = False

def TSP(distance_matrix, source):
    n = len(distance_matrix)
    cities = []
    for i in range (n):
        if i != source:
            cities.append(i) 
    used = [False] * len(cities)
    permutation = []
    generate_permutation_(cities, [], used, permutation)

    min_distance = float('inf')
    best_path = []
    for i in permutation:
        path = [source] + i + [source]
        total_dis = 0
        for i in range (len(path) -1):
            total_dis = total_dis + distance_matrix[path[i]][path[i+1]]
        if total_dis < min_distance:
            min_distance = total_dis
            best_path = path [:]

    return min_distance, best_path
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cities = [0, 1, 2, 3]
source = 0
min_dist, best_path = TSP(dist_matrix, source)
print("Shortest Distance:", min_dist)
print("Best Path:", " -> ".join(str(i) for i in best_path))


    



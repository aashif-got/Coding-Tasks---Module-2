import math 



def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(pts):
    n = len(pts)
    if n <= 3:
        return brute_force(pts)

    mid = n // 2
    mid_pt = pts[mid]   

    # Divide into left and right halves
    dl, pair_left = closest_pair(pts[:mid])
    dr, pair_right = closest_pair(pts[mid:])

    # Find smaller distance
    if dl < dr:
        d_min = dl
        best_pair = pair_left
    else:
        d_min = dr
        best_pair = pair_right

    # Build the strip
    strip = [p for p in pts if abs(p[0] - mid_pt[0]) < d_min]

    # Find closest in strip
    ds, pair_strip = strip_closest(strip, d_min)
    if ds < d_min:
        return ds, pair_strip
    else:
        return d_min, best_pair
    

def brute_force(pts):
    min_distance = float('inf')
    pair = (None, None)
    n = len(pts)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(pts[i], pts[j])
            if d < min_distance:
                min_distance = d
                pair = (pts[i], pts[j])
    return min_distance, pair

def strip_closest(strip, d_min):
    min_distance = d_min
    pair = (None, None)

    # Sort strip by y-coordinate
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # Only check pts within d_min in y
            if (strip[j][1] - strip[i][1]) < min_distance:
                d = dist(strip[i], strip[j])
                if d < min_distance:
                    min_distance = d
                    pair = (strip[i], strip[j])
            else:
                break
    return min_distance, pair




pts = [(1, 2), (4, 6), (7, 8), (2, 3), (9, 10), (5, 4), (11, 12), (8, 9)]

    
pts.sort(key=lambda p: p[0])

min_distance, best_pair = closest_pair(pts)
print(f"Closest Pair: {best_pair}")
print(f"Minimum Distance: {min_distance:.2f}")
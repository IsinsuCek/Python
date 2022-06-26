import heapq
l = [1, 2, 7, 3, 9, 5]
h = []

for i in l:
    heapq.heappush(h,i)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))


city_map = {
    'A': {'B': 5, 'C': 12},
    'B': {'C': 10},
    'C': {'D': 3},
    'D': {'E': 7, 'F': 8},
}

def shortest_path(src, dest, city_map):
    h = []
    heapq.heappush(h, [0, src])

    while len(h):
        current_distance, current_place = heapq.heappop(h)
        print(current_distance,current_place)
        if current_place == dest:
            print('found the shortest path from {} to {} with {}'.format(src, dest, current_place))
            break
        for neigh in city_map[current_place]:
            heapq.heappush(h,[current_distance+city_map[current_place][neigh],neigh])
print(shortest_path('A', 'D', city_map))
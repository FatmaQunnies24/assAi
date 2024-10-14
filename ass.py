import math
#BFS
grid = [
    [(0, 0), (0, 0), (1, -1), (0, 0)],
    [(0, 0), (2, 1), (3, -1), (4, -1)],
    [(5, -1), None, (6, -1), (0, 0)],
    [(0, 0), (7, 1), (8, -1), (0, 0)]
]

def g(x):
    return math.sqrt(2 * x)

total_cost = 0

for row in grid:
    for room in row:
        if room is None:
            total_cost += 1
        elif room[1] == -1:
            total_cost += 2 * g(room[0])
        elif room[1] == 1:
            total_cost += g(room[0])

print("Cost", total_cost)



total_cost_DFS = 0

for row in grid:
    for room in row:
        if room is None:
            total_cost_DFS += 1
        elif room[1] == -1:
            total_cost_DFS += 2 * g(room[0])
        elif room[1] == 1:
            total_cost_DFS += g(room[0])

print("Cost", total_cost_DFS)
#DFS
total_cost_DFS = 0

num_rows = len(grid)
num_cols = len(grid[0])

for col in range(num_cols):
    for row in range(num_rows):
        room = grid[row][col]
        if room is None:
            total_cost_DFS += 1
        elif room[1] == -1:
            total_cost_DFS += 2 * g(room[0])
        elif room[1] == 1:
            total_cost_DFS += g(room[0])

print("Cost (DFS):", total_cost_DFS)
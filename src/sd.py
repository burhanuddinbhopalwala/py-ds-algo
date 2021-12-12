# # * There is a square field which is full of trees planted in a grid. Each tree takes up one position and has a height between 0 and 10.
# # * You are tasked with hanging an electric wire that runs straight over the field.
# # *
# # *
# # * The wire may enter the field from the north(vertically) or west(horizontally) direction. The wire can only pass above trees that are of a lesser height. The wire's hangs at the same height for its entire length over the field.
# # * Write a program that takes as input the height of each tree in the field. It should return the direction(N or W) and position from which the wire should enter the field, so that it is hanging closest to the ground.


# # * Input << 2D each element height of the tree[0 10]

# # * Output << N, W(Enter direction) Closest to the ground +
# # * position of the Tree with which are entering(x, y)


# # class Grid:
# #     def __init__(self, grid_store):
# #         self.store = grid_store


# n = 3
# grid = [[3,  2, 5],
#         [10, 5, 3],
#         [1,  2, 9]]


# def return_dir(max_row, max_col, west_position, north_position, grid=grid):
#     temp_rows = []
#     for index, row in enumerate(grid):
#         temp_max = max(row)
#         west_position = index
#         temp.append([temp_max, west_position])

#     temp_cols = []
#     for index in range(n):
#         north_position = index
#         temp_cols.append([temp_max, north_position])

#     min_enter = min(min(temp_rows[:][0]), min(temp_cols))

#     return None


# max_row = float('-inf')
# max_col = float('-inf')

# west_position = -1
# north_position = -1
# print(return_dir(max_row, max_col, west_position, grid))

# # * g = Grid(grid)


n = 3

grid = [[3,  2, 7],
        [2, 1, 1],
        [1,  2, 9]]

# * Output:
# (N, 2)


def find_direction(grid=grid, north_dir=-1, west_dir=-1):
    rows_scanned = []
    for index, row in enumerate(grid):
        west_dir = index
        rows_scanned.append((max(row), west_dir))

    nrow = len(grid)
    ncol = len(grid[0])

    cols_scanned = []
    for index in range(ncol):
        max_col = -1
        for j in range(nrow):
            temp = grid[j][index]
            if temp > max_col:
                max_col = temp
                north_dir = index
        cols_scanned.append((max_col, north_dir))

    min_row = 11
    min_west_dir = -1
    for ele in rows_scanned:
        if min_row > ele[0]:
            min_row = ele[0]
            min_west_dir = ele[1]

    min_col = 11
    min_north_dir = -1
    for ele in cols_scanned:
        if min_col > ele[0]:
            min_col = ele[0]
            min_north_dir = ele[1]

    final_cost = min(min_row, min_col)
    if final_cost == min_row:
        return ('W', min_west_dir)
    return ('N', min_north_dir)


print(find_direction(grid))

def boom_bomb_coordinates(mat, ro, co):
    result = []
    possible_bomb_damage_coordinates = [
        # [ro, co],
        [ro, co + 1],
        [ro, co - 1],
        [ro - 1, co],
        [ro + 1, co],
        [ro - 1, co - 1],
        [ro - 1, co + 1],
        [ro + 1, co - 1],
        [ro + 1, co + 1],
    ]
    for r, c in possible_bomb_damage_coordinates:
        if 0 <= r < len(mat) and 0 <= c < len(mat[0]):
            result.append([r, c])

    return result


size = int(input())
matrix = []

for i in range(size):
    matrix.append([int(x) for x in input().split()])
bomb_coordinates = input().split(' ')

for bomb in bomb_coordinates:
    row, col = [int(x) for x in bomb.split(',')]
    bomb_damage = matrix[row][col]

    for r, c in boom_bomb_coordinates(matrix, row, col):
        if  matrix[r][c] > 0:
            matrix[r][c] -= bomb_damage
    matrix[row][col] = 0
active_cells = 0
sum_cells = 0
for ready_row in matrix:
    for num in ready_row:
        if num > 0:
            active_cells += 1
            sum_cells += num
print(f'Alive cells: {active_cells}')
print(f'Sum: {sum_cells}')

for ready_row in matrix:
    print(*ready_row, sep=' ')

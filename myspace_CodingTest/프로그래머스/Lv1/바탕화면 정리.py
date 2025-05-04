# 내가 작성한 코드
def solution1(wallpaper):
    wallpaper_list = []

    for lst in wallpaper:
        wallpaper_list.append(list(lst))

    index_arr = []
    result = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper_list[i][j] == '#':
                index_arr.append((i, j))

    row_arr = sorted(index_arr, key=lambda x: x[0])
    col_arr = sorted(index_arr, key=lambda x: x[1])

    result.append((row_arr[0][0], col_arr[0][1], row_arr[-1][0] + 1, col_arr[-1][1] + 1))

    for lst in result:
        return list(lst)


# chat gpt4o
def solution2(wallpaper):
    min_row = float('inf')
    max_row = -1
    min_col = float('inf')
    max_col = -1

    for i, row in enumerate(wallpaper):
        for j, cell in enumerate(row):
            if cell == '#':
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    return [min_row, min_col, max_row + 1, max_col + 1]
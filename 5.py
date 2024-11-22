class Solution(object):

    def generate_n_rectangles(self, number_of_rectangles):
        array = []
        list_of_sizes = []

        for i in range(number_of_rectangles):
            j = i + 1
            list_of_sizes.append(j)

        size_of_final_print = 1 + ((list_of_sizes[-1] - 1) * 4)

        for row in range(size_of_final_print):
            row = ["  " for _ in range(size_of_final_print)]
            array.append(row)

        center = -2
        for i in range(list_of_sizes[-1]):
            center += 2
        array[center][center] = "# "

        vectors = [[2, 2], [2, -2], [-2, 2], [-2, -2]]
        list_of_centers = [[center, center]]
        visited = set(tuple(corner) for corner in list_of_centers)

        for _ in list_of_sizes:
            new_list_of_centers = []
            for cord in list_of_centers:
                x = cord[0]
                y = cord[1]
                for vector in vectors:
                    dx, dy = vector
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < size_of_final_print
                        and 0 <= ny < size_of_final_print
                        and (nx, ny) not in visited
                    ):
                        array[nx][ny] = "# "
                        new_list_of_centers.append([nx, ny])
                        visited.add((nx, ny))
                    list_of_centers = new_list_of_centers

        list_of_corners = [
            [0, 0],
            [0, size_of_final_print - 1],
            [size_of_final_print - 1, 0],
            [size_of_final_print, size_of_final_print - 1],
        ]

        for _ in list_of_sizes:
            new_list_of_corners = []

            top_left, top_right, bottom_left, bottom_right = list_of_corners

            for x in range(top_left[1], top_right[1] + 1):
                array[top_left[0]][x] = "# "
            for x in range(bottom_left[1], bottom_right[1] + 1):
                array[bottom_left[0]][x] = "# "
            for y in range(top_left[0], bottom_left[0]):
                array[y][top_left[1]] = "# "
            for y in range(top_right[0], bottom_right[0]):
                array[y][top_right[1]] = "# "

            new_list_of_corners.append([top_left[0] + 2, top_left[1] + 2])
            new_list_of_corners.append([top_right[0] + 2, top_right[1] - 2])
            new_list_of_corners.append([bottom_left[0] - 2, bottom_left[1] + 2])
            new_list_of_corners.append([bottom_right[0] - 2, bottom_right[1] - 2])

            list_of_corners = new_list_of_corners

        for row in array:
            for char in row:
                print(char, end="")
            print("")


Solution().generate_n_rectangles(3)

# def has_path(maze_str):
#     maze = maze_str.split()
#     rows = len(maze)
#     cols = len(maze[0])

#     def dfs(row, col):
#         # Base cases: check if out of bounds or hit a wall
#         if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] == '#':
#             print('inside false',maze[row][col])
#             return False

#         # Check if we reached the destination
#         if maze[row][col] == 'D':
#             print('inside true',maze[row][col])

#             return True

#         # Mark the current cell as visited
#         maze[row] = maze[row][:col] + '#' + maze[row][col+1:]

#         # Recursively explore all possible directions
#         return any(dfs(row + dr, col + dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])

#     # Find the starting point 'S'
#     for i in range(rows):
#         for j in range(cols):
#             if maze[i][j] == 'S':
#                 return dfs(i, j)

#     # If 'S' is not found, return False
#     return False

# # # Example usage
# # maze_input = "S### #   #  # ## #  # # ##    D"
# # print(has_path(maze_input))  # Output: True

# # maze1 = "S### # ###  # ## #  # # ##     D"    
# # print(has_path(maze1))  # Output: False


# maze_input = "S### #   #  # ## #  # # ##    D"
# print(has_path(maze_input))  # Output: True

# maze1 = "S### # ###  # ## #  # # ##     D"
# print(has_path(maze1))  # Output: False


def has_path(maze_str):
    # Parse the maze string into a 2D grid
    maze = [list(row) for row in maze_str.split('\n')]
    rows, cols = len(maze), len(maze[0])

    # Define a recursive DFS function
    def dfs(row, col):
        # Base cases: check if out of bounds or hit a wall
        if row < 0 or row >= rows or col < 0 or col >= cols or maze[row][col] == '#':
            return False
        # Check if we reached the destination
        if maze[row][col] == 'D':
            return True
        # Mark the current cell as visited
        maze[row][col] = '#'
        # Recursively explore all possible directions
        return any(dfs(row + dr, col + dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])

    # Find the starting point 'S' and start DFS
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                return dfs(i, j)
    # If 'S' is not found, return False
    return False

# Example usage:
maze_input = "S### #   #  # ## #  # # ##    D"
print(has_path(maze_input))  # Output: True

maze_input = "S### # ###  # ## #  # # ##     D"
print(has_path(maze_input))  # Output: False

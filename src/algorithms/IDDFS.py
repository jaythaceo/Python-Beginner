"""
Within the field of Artificial Intelligence the sliding puzzle problem is a great way to explore the effectiveness of different searching algorithms. Consisting of a superficial border with symboled tiles in a random order and one tile missing, the objective is to rearrange the puzzle in the least amount of moves to a goal state (typically natural order). The border must be taken into consideration upon each move, with only a maximum of four possible legal moves available
(up, down, left and right).

"""
def id_dfs(puzzle, goal, get_moves):
    import itertools

    def dfs(route, depth):
        if depth == 0:
            return
        if route[-1] == goal:
            return route
        for move in get_moves(route[-1]):
            if move not in route:
                mext_route = dfs(route + [move], depth -1)
                if next_route:
                    return next_route

    for depth in itertools.count():
        route = dfs([puzzle], depth)
        if route:
            return route

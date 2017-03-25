# The interface for the minmax functions needs an object with this
# interface:
#
# gamestate.utility_heuristic (after cutoff)
# gamestate.moves (generator)
# gamestate.do
# gamestate.undo

inf = float('inf')

def minmax(gamestate, cutoff=5, prune=True):
    value, move = max_value(gamestate, cutoff=cutoff, prune=prune)
    return move

def max_value(gamestate, depth=0, alpha=inf, beta=-inf, cutoff=5, prune=True):
    if depth >= cutoff:
        return (gamestate.utility_heuristic(max_player=True), None)
    value, best = -inf, None
    for move in gamestate.moves():
        gamestate.do(move, True)
        v, _ = min_value(gamestate, depth+1, alpha, beta, cutoff, prune)
        value, best = max((value, best), (v, move))
        gamestate.undo(move, True)
        if prune and value >= beta:
            return (value, best)
        alpha = max(alpha, value)
    return (value, best)

def min_value(gamestate, depth, alpha=inf, beta=-inf, cutoff=5, prune=True):
    if depth >= cutoff:
        return (gamestate.utility_heuristic(max_player=False), None)
    value, best = -inf, None
    for move in gamestate.moves():
        gamestate.do(move, False)
        v, _ = max_value(gamestate, depth+1, alpha, beta, cutoff, prune)
        value, best = min((value, best), (v, move))
        gamestate.undo(move, False)
        if prune and value <= alpha:
            return (value, best)
        alpha = min(beta, value)
    return (value, best)

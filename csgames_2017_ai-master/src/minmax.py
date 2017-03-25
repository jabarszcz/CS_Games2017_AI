# gamestate.next_move_heuristic (next move ordering for minmax search)
# gamestate.utility_heuristic (after cutoff)
# gamestate.do
# gamestate.undo

def minmax(gamestate, cutoff=5, prune=true):
    value, move = max_value(gamestate, cutoff=cutoff, prune=prune)
    return move

def max_value(gamestate, depth=0, alpha=inf, beta=-inf, cutoff=5, prune=true):
    if depth >= cutoff:
        return gamestate.utility_heuristic()
    value, best = -inf, None
    for move in gamestate.moves():
        gamestate.do(move)
        v, _ = min_value(gamestate, depth+1, alpha, beta, cutoff, prune)
        value, best = max((value, best), (v, move))
        gamestate.undo(move)
        if prune and value >= beta:
            return (value, best)
        alpha = max(alpha, value)
    return (value, best)

def min_value(gamestate, depth, alpha=inf, beta=-inf, cutoff=5, prune=true):
    if depth >= cutoff:
        return gamestate.utility_heuristic()
    value, best = -inf, None
    for move in gamestate.moves():
        gamestate.do(move)
        v, _ = max_value(gamestate, depth+1, alpha, beta, cutoff, prune)
        value, best = min((value, best), (v, move))
        gamestate.undo(move)
        if prune and value <= alpha:
            return (value, best)
        alpha = min(beta, value)
    return (value, best)

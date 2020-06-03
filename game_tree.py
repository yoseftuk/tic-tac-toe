
        
ceche = {}
def create_game_tree(board = [0]*9, turn = -1, i = 0):
    memo = ceche.get(str(board))
    if memo is not None:
        return memo
    win = winner(board)
    node = {"board" : board, "win": win, "turn": turn}
    children = []
    if win == 0:
        for i in range(len(board)):
            if board[i] == 0:
                b = [k for k in board]
                b[i] = turn
                children.append(create_game_tree(b, -1 if turn == 1 else 1))
    node["children"] = children
    ceche[str(board)] = node
    return node
    
def winner(b):
    if b[0] == b[1] == b[2] or b[0] == b[3] == b[6]: return b[0]
    if b[3] == b[4] == b[5] or b[1] == b[4] == b[7] or b[0] == b[4] == b[8] or b[2] == b[4] == b[6]: return b[4]
    if b[6] == b[7] == b[8] or b[2] == b[5] == b[8]: return b[8]
    return 0

def make_choise(state):
    children = state.get("children")
    max_x = -2
    max_i = 0
    for i in range(len(children)):
        m = pre_choise(children[i])
        if max_x < m:
            max_x = m
            max_i = i
    return max_i

def pre_choise(state):
    children = state.get("children")
    turn = state.get("turn")
    win = state.get("win")
    if len(children) == 0: return win
    weights = [pre_choise(child) for child in children]
    return min(weights) if turn == -1 else max(weights)
    
board = create_game_tree()
    

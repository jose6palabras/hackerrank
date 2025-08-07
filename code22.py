def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    queen_moves = []
    r, c = r_q, c_q
    while r<n:
        r = r + 1
        pos_right = [r, c]
        if pos_right in obstacles:
            break
        else:
            queen_moves.append(pos_right)
    r, c = r_q, c_q
    while r>1:
        r = r - 1
        pos_left = [r, c]
        if pos_left in obstacles:
            break
        else:
            queen_moves.append(pos_left)
    r, c = r_q, c_q
    while c<n:
        c = c + 1
        pos_up = [r, c]
        if pos_up in obstacles:
            break
        else:
            queen_moves.append(pos_up)
    r, c = r_q, c_q
    while c>1:
        c = c - 1
        pos_down = [r, c]
        if pos_down in obstacles:
            break
        else:
            queen_moves.append(pos_down)
    r, c = r_q, c_q
    while r<n and c<n:
        r = r + 1
        c = c + 1
        pos_right_up = [r, c]
        if pos_right_up in obstacles:
            break
        else:
            queen_moves.append(pos_right_up)
    r, c = r_q, c_q
    while r>1 and c<n:
        r = r - 1
        c = c + 1
        pos_left_up = [r, c]
        if pos_left_up in obstacles:
            break
        else:
            queen_moves.append(pos_left_up)
    r, c = r_q, c_q
    while r<n and c>1:
        r = r + 1
        c = c - 1
        pos_right_down = [r, c]
        if pos_right_down in obstacles:
            break
        else:
            queen_moves.append(pos_right_down)
    r, c = r_q, c_q
    while r>1 and c>1:
        r = r - 1
        c = c - 1
        pos_left_down = [r, c]
        if pos_left_down in obstacles:
            break
        else:
            queen_moves.append(pos_left_down)
    return len(queen_moves)
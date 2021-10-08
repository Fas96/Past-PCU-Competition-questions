def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)

    # size length of subboard
    s = side // 2

    # offsets for outter/inner squares of subboard
    offsets = (0, -1), (side - 1, 0)

    for dy_outter, dy_inner in offsets:
        for dx_outter, dy_inner in offsets:
            # if the outter corner is not set
            if not board[top + dy_outter][left + dx_outter]:
                # ..label the inner corner
                board[top + s + dy_inner][left + s + dy_inner] = lab

    # next level
    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                # Recursive calls, if s is at least 2
                lab = cover(board, lab, top + dy, left + dx, s)

    return lab


if __name__ == '__main__':
    board = [[0] * 8 for _ in range(8)]
    board[7][7] = -1
    cover(board)
    print(board)
    for row in board:
        print(("  %2i" * 8) % tuple(row))

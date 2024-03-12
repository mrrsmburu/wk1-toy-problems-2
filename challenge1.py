def solution(A):
    total_bricks = sum(A)
    n = len(A)
    if total_bricks % n != 0:
        return -1

    bricks_per_box = total_bricks // n
    moves = 0
    for bricks_in_box in A:
        moves += abs(bricks_per_box - bricks_in_box)
    
    return moves

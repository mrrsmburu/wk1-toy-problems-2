def solution(N):
    if N <= 0:
        return ""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num_letters = len(alphabet)
    num_repeats = N // num_letters
    remainder = N % num_letters

    result = alphabet * num_repeats + alphabet[:remainder]
    return result
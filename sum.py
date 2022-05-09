for _ in range(int(input())):
    R, S = input().split()
    S = list(S)
    for word in S:
        print(word * int(R), end='')
    print()
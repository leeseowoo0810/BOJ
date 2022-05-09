for _ in range(int(input())):
    quiz = input()
    score = cnt = 0
    for word in quiz:
        if word == 'O':
            cnt += 1
        else:
            cnt = 0
        score += cnt
    print(score)

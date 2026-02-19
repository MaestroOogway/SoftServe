def solution(n):
    if n < 0:
        return 0

    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

print(solution(579579))
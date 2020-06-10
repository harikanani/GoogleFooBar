def solution(M, F):
    m, f = int(M), int(F)
    total = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m <= 0:
            return "impossible"
        if f == 1:
            return str(total + m - 1)
        else:
            total += int(m/f)
            m, f = f, m % f
    return str(total)

# Test Cases
print(solution('4','7'))
print(solution('2','1'))

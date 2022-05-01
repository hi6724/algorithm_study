def decimal(n, k):
    rev_base = ''
    while n > 0:
        n, m = n // k, n % k
        rev_base += str(m)
    return rev_base[::-1]


def is_prime_number(k):
    try:
        k = int(k)
    except:
        return False
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k**0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    decimal_num = decimal(n, k)
    decimal_list = (decimal_num.split("0"))
    for i in decimal_list:
        if (is_prime_number(i)):
            answer += 1
    return answer


test_n = 437674
test_k = 3
dd = decimal(test_n, test_k)
print(solution(test_n, test_k))

# print(is_prime_number(4))
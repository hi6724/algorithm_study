def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed_text = ""
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if prev == s[i:i + step]:
                count += 1

            else:
                compressed_text += str(count) + prev if count >= 2 else prev
                prev = s[i:i + step]
                count = 1
        compressed_text += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed_text))

    return answer


test_case = 'aabbcaaa'
print(solution(test_case))
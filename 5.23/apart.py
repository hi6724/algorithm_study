test = '''
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0 
'''

# def sol(arr):
#     ans = 0
#     for i in range(2, len(arr) - 2):
#         max_height = max(
#             [arr[i - 2], arr[i - 1], arr[i], arr[i + 1], arr[i + 2]])
#         second_height = max([arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]])
#         if arr[i] == max_height:
#             ans += max_height - second_height
#     print(ans)

# sol(list(map(int, test.split())))

# # for rep in range(10):

# #     ans = 0

# #     print(f'#{rep+1} {ans}')


def sol(arr):
    ans = 0
    for i in range(2, len(arr) - 2):
        max_height = max(
            [arr[i - 2], arr[i - 1], arr[i], arr[i + 1], arr[i + 2]])
        second_height = max([arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]])
        if arr[i] == max_height:
            ans += max_height - second_height
    return ans


for rep in range(10):
    input()
    arr = list(map(int, input().split()))
    ans = sol(arr)
    print(f"#{rep+1} {ans}")
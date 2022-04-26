id_list = ['muzi', 'frodo', 'apeach', 'neo']
report = [
    'muzi frodo', 'muzi frodo', 'muzi frodo', 'apeach frodo', 'frodo neo',
    'muzi neo', 'apeach muzi'
]
k = 2


def sol(id_list, report, k):
    reported_dict = {}
    report_dict = {}
    for i in id_list:
        reported_dict[i] = 0
        report_dict[i] = []

    for i in report:
        x, y = (i.split())
        if y not in report_dict[x]:
            report_dict[x].append(y)
            reported_dict[y] = reported_dict[y] + 1
    reported_dict = list(
        dict(filter(lambda e: e[1] >= k, reported_dict.items())).keys())
    print(reported_dict)
    for i in report_dict:
        count = 0
        for j in report_dict[i]:
            if (j in reported_dict):
                count += 1
        report_dict[i] = count
    ans = []
    for i in id_list:
        ans.append(report_dict[i])
    return (ans)


print(sol(id_list, report, k))

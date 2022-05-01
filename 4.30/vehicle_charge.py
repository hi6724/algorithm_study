import math


def solution(fees, records):
    answer = []
    new_records = {}
    for record in records:
        record = record.split()
        vehicle_id = record[1]
        judge = record[2]
        time = (record[0].split(":"))
        time = int(time[0]) * 60 + int(time[1])

        if vehicle_id in new_records:
            if new_records[vehicle_id][1] == "IN":
                charge = time - new_records[vehicle_id][0] + new_records[
                    vehicle_id][2]
                new_records[vehicle_id][1] = "OUT"
                new_records[vehicle_id][2] = charge
            else:
                new_records[vehicle_id] = [
                    time, judge, new_records[vehicle_id][2]
                ]
        else:
            new_records[vehicle_id] = [time, judge, 0]
    for record in new_records:
        if new_records[record][1] == "IN":
            new_records[record][1] = "OUT"
            new_records[record][2] += (1439 - new_records[record][0])
    index = sorted(new_records)
    for record in index:
        result = 0
        time = new_records[record][2]
        if time <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        answer.append(result)
    return answer


# 기본시간 기본요금 단위시간 단위요금
test_fees = [120, 0, 60, 591]
test_records = [
    "16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT",
    "23:58 3961 IN"
]
# 나간순서대로? 인듯
test_results = [14600, 34400, 5000]
# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
print(solution(test_fees, test_records))
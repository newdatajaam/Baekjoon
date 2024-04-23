def solution(fees, records):
    total_fees = {}
    car_num_list = []
    time_list = []
    for parking in records:
        time_cal, car_num, types = parking.split()
        h, m = time_cal.split(":")
        time = int(h) * 60 + int(m)

        if types == 'IN':
            car_num_list.append(car_num)
            time_list.append(time)
        elif types == 'OUT':
            if car_num in total_fees:   
              total_fees[car_num] = total_fees[car_num] + (time - time_list.pop(car_num_list.index(car_num)))
            else:
              total_fees[car_num] = (time - time_list.pop(car_num_list.index(car_num)))
            car_num_list.remove(car_num)

    if car_num_list: # 만약 아직 출차하지 않은 차량이 있다면 
        for i in range(len(car_num_list)):
          if car_num_list[i] in total_fees:
            total_fees[car_num_list[i]] = total_fees[car_num_list[i]] + ((23*60+59) - time_list[i])
          else:
            total_fees[car_num_list[i]] = ((23*60+59) - time_list[i])

    basic_min, basic_fee, per_min, per_fee = fees

    for key, value in total_fees.items():
        if value <= basic_min:
            total_fees[key] = basic_fee
        else:
            if ((value - basic_min) % per_min) != 0: 
              total_fees[key] = basic_fee + (((value - basic_min) // per_min)+1) * per_fee
            else:
              total_fees[key] = basic_fee + ((value - basic_min) // per_min) * per_fee

    answer = []
    sorted_dict = sorted(total_fees.items(), key = lambda item: item[0])
    for key, value in sorted_dict:
        answer.append(value)
    return answer

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
solution(fees, records)
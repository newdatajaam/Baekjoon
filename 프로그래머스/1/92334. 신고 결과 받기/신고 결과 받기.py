def solution(id_list, report, k):
    reported_cnt = {id_ : 0 for id_ in id_list}
    reporter = {id_ : [] for id_ in id_list}
    final_report_names = []
    
    for ids in report:
        id1, id2 = ids.split()
        if id2 in reporter[id1]:
            continue
        else:
          reporter[id1].append(id2)
          reported_cnt[id2] += 1

    for key, value in reported_cnt.items():
        if value >= k:
            final_report_names.append(key)
            
    answer = [0] * len(id_list)
    for name in final_report_names:     
        idx_cnt = 0
        for names in reporter.values():
            if name in names:
                answer[idx_cnt] += 1
            idx_cnt += 1
    return answer
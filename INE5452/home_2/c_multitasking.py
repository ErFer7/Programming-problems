"""
Multitasking.
"""

while True:
    one_time_tasks, repeating_tasks = map(int, input().split())

    if one_time_tasks == 0 and repeating_tasks == 0:
        break

    time_dict_order = []
    task_time_id = 0
    time_dict = {}

    for _ in range(one_time_tasks):
        start, end = map(int, input().split())

        time_dict_order.append(task_time_id)

        if start not in time_dict:
            time_dict[start] = [(task_time_id, 0)]  # 0 Para o início
        else:
            time_dict[start].append((task_time_id, 0))

        if end not in time_dict:
            time_dict[end] = [(task_time_id, 1)]  # 1 Para o fim
        else:
            time_dict[end].append((task_time_id, 1))

        task_time_id += 1

    for _ in range(repeating_tasks):
        start, end, interval = map(int, input().split())

        while start < 1000000:
            time_dict_order.append(task_time_id)

            if start not in time_dict:
                time_dict[start] = [(task_time_id, 0)]
            else:
                time_dict[start].append((task_time_id, 0))

            if end not in time_dict:
                time_dict[end] = [(task_time_id, 1)]
            else:
                time_dict[end].append((task_time_id, 1))

            start += interval
            end += interval

            task_time_id += 1

    

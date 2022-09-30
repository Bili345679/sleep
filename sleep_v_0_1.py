import json
import time

# v_0_1 通过时间间隔预测下一次是否应该醒来
def sleep(sleep_time=False, sleep_to=False, start_time=False):
    if not start_time:
        start_time = time.time_ns()

    if sleep_time:
        # 从睡眠时间算醒来时间
        sleep_time *= 1000000000
        sleep_to = sleep_time + start_time
    elif not sleep_to:
        # 既没有睡眠时间，也没有醒来时间，直接退出
        return False
    else:
        sleep_to = sleep_to * 1000000000

    # 间隔和
    interval_sum = 0
    # 间隔次数
    interval_count = 0
    # 每次间隔内检测次数
    interval_check_time_list = {}
    # 当前时间
    now_time = time.time_ns()
    # 最后更新时间
    last_time = now_time

    # 退出方式
    out_way = 1

    # 在当前时间小于目标时间时循环
    while now_time < sleep_to:
        # 如果时间更新
        if not last_time == now_time:
            # 增加间隔和
            interval_sum += now_time - last_time
            # 增加间隔次数
            interval_count += 1
            # 平均间隔
            avg_interval = interval_sum / interval_count
            # 预测下一次更新是否会超过目标时间
            if avg_interval + now_time > sleep_to:
                out_way = 2
                break
        # 再次获取当前时间
        now_time = time.time_ns()

        if now_time in interval_check_time_list:
            interval_check_time_list[now_time] += 1
        else:
            interval_check_time_list[now_time] = 0
    return out_way


if __name__ == "__main__":
    num = 0
    offset_list = []
    while num < 100:
        sleep_time = 1 / 60 / 2
        start_time = time.time()
        sleep(sleep_time)
        end_time = time.time()

        interval_time = end_time - start_time
        # print("\n")
        # print("sleep_to", start_time + sleep_time)
        # print(start_time)
        # print(end_time)
        # print(interval_time)
        # print((interval_time - sleep_time) / sleep_time * 100, "%")

        offset_list.append((interval_time - sleep_time) / sleep_time * 100)
        num += 1

        # with open("./record.json", "w+") as file:
        #     json.dump(record_list, file)

    with open("./test_record/1.json", "w+") as file:
        json.dump(offset_list, file)
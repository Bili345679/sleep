import json
import time

# v_0_2_a 通过上一次时间更新间隔过程中发生的检测次数推测是否超过醒来时间
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
    # 每次间隔列表
    interval_list = []
    # 每次间隔内检测次数
    interval_check_time_list = {}
    # 每次间隔检测时间
    last_interval_check_time = 0
    # 当前时间
    now_time = time.time_ns()
    # 最后更新时间
    last_time = now_time
    # 更新时间列表
    time_list = [now_time]

    # 退出方式
    out_way = 1

    # 在当前时间小于目标时间时循环
    while now_time < sleep_to:
        # 如果时间更新
        if not last_time == now_time:
            time_list.append(now_time)
            interval = now_time - last_time
            # 增加间隔和
            interval_sum += interval
            # 增加间隔次数
            interval_count += 1
            # 间隔列表
            interval_list.append(interval)

            # 上一次间隔中，每次check时间
            if interval_list[-1] != 0 and interval_check_time_list[time_list[-2]] != 0:
                last_interval_check_time = (
                    interval_list[-1] / interval_check_time_list[time_list[-2]]
                )

            # 平均间隔
            avg_interval = interval_sum / interval_count
            if avg_interval + now_time > sleep_to:
                out_way = 2
                break

            # 更新最后更新时间
            last_time = now_time

        # 再次获取当前时间
        now_time = time.time_ns()

        if now_time in interval_check_time_list:
            interval_check_time_list[now_time] += 1
        else:
            interval_check_time_list[now_time] = 0

        # # 如果上一次间隔平均检测时间 * 当前间隔检测次数 + 当前时间
        if last_interval_check_time * interval_check_time_list[now_time] + now_time > sleep_to:
            out_way = 3
            break

    return out_way


if __name__ == "__main__":
    num = 0
    offset_list = []
    while num < 100:
        sleep_time = 1 / 60 / 2
        start_time = time.time()
        out_way = sleep(sleep_time)
        end_time = time.time()

        interval_time = end_time - start_time
        # print("\n")
        # print(out_way)
        # print(start_time)
        # print(end_time)
        # print(interval_time)
        # print((interval_time - sleep_time) / sleep_time * 100, "%")
        
        offset_list.append((interval_time - sleep_time) / sleep_time * 100)
        num += 1

    with open("./test_record/2a.json", "w+") as file:
        json.dump(offset_list, file)
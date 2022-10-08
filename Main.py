import sleep_v_0__1
import sleep_v_0_0
import sleep_v_0_1
import sleep_v_0_2_a
import sleep_v_0_2_b
import sleep_v_0_3
import sleep_v_0_4
import time
import json


def test(function, save_name):
    num = 0
    offset_list = []
    while num < 100:
        sleep_time = 0.001

        start_time = time.perf_counter()
        function(sleep_time)
        end_time = time.perf_counter()

        interval_time = end_time - start_time
        # print("\n")
        # print("sleep_to", start_time + sleep_time)
        # print(start_time)
        # print(end_time)
        # print(interval_time)
        # print((interval_time - sleep_time) / sleep_time * 100, "%")

        offset_list.append((interval_time - sleep_time) / sleep_time * 100)
        num += 1

    with open("./test_record/" + save_name + ".json", "w+") as file:
        json.dump(offset_list, file)


test(sleep_v_0__1.sleep, "-1")
test(sleep_v_0_0.sleep, "0")
test(sleep_v_0_1.sleep, "1")
test(sleep_v_0_2_a.sleep, "2_a")
test(sleep_v_0_2_b.sleep, "2_b")
test(sleep_v_0_3.sleep, "3")
test(sleep_v_0_4.sleep, "4_1")
test(sleep_v_0_4.sleep_pc, "4_2")
test(sleep_v_0_4.sleep_pc_easy, "4_3")

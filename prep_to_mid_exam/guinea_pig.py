def write_weights():
    weight_list = []
    for i in range(1, 5):
        kgs = float(input())
        weight_list.append(kgs)
    return weight_list


def transform_units_to_grams(my_list_to_grams):

    for i in range(len(my_list_to_grams)):
        my_list_to_grams[i] = my_list_to_grams[i] * 1000
    return my_list_to_grams


def transform_units_to_kgs(my_list_to_kgs):
    for i in range(len(my_list_to_kgs)):
        my_list_to_kgs[i] = my_list_to_kgs[i] / 1000
    return my_list_to_kgs


def main_logic(work_list):
    no_more_consumables = True
    for day in range(1, 31):
        work_list[0] = work_list[0] - 300
        if work_list[0] <= 0:
            no_more_consumables = False
            break
        if day % 2 == 0:
            work_list[1] = work_list[1] - (work_list[0] * 0.05)
            if work_list[1] <= 0:
                no_more_consumables = False
                break
        if day % 3 == 0:
            work_list[2] = work_list[2] - (work_list[3] / 3)
            if work_list[2] <= 0:
                no_more_consumables = False
    return work_list, no_more_consumables


weight = write_weights()
weight_in_grams = transform_units_to_grams(weight)
result, consumables = main_logic(weight_in_grams)
result_in_kgs = transform_units_to_kgs(result)

if consumables:
    print(f"Everything is fine! Puppy is happy! Food: {result_in_kgs[0]:.2f}, Hay: {result_in_kgs[1]:.2f}, Cover: {result_in_kgs:.2f}.")
else:
    print(f"Merry must go to the pet store!")

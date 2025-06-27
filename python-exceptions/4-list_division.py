#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            element1 = my_list_1[i]
            element2 = my_list_2[i]

            division_result = element1 / element2
            result.append(division_result)

        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        finally:
            pass

    return result

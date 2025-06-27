#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # 跳过非整数类型，继续处理下一个元素
            continue
        except IndexError:
            # 如果索引超出范围，抛出异常
            raise
    print()  # 打印换行符
    return count

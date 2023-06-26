#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lists = []
    
    for i in range(list_length):
        try:
            new_list = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            new_list = 0
        except zeroDivisionError:
            print("division by 0")
            new_list = 0
        except IndexError:
            print("outnof range")
            new_list = 0
        finally:
            lists.append(new_list)
    return lists

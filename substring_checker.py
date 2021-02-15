def substring_checker(
        first_string,
        second_string
):
    for i in range(len(first_string) - len(second_string) + 1):
        find_flag = True
        for j in range(len(second_string)):
            if first_string[i + j] != second_string[j]:
                find_flag = False
                break
        if find_flag:
            return True
    return False

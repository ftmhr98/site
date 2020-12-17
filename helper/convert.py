def convert_int(nums):
    strings = [str(num) for num in nums]

    a_string = "".join(strings)

    an_integer = int(a_string)
    return an_integer


def convert_list(number):
    flat_1 = [x for ls in number for x in ls]
    return flat_1


def str_to_length(base_str, length, do_dots=True):
    base_str = str(base_str)
    ret_str = base_str.ljust(length)[:length]
    if do_dots and len(base_str) + 3 >= length:
        return ret_str[:-3] + "..."
    return ret_str

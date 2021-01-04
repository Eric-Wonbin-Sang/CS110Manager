from General import Functions


class Student:

    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name

        self.iter = self.get_iter()
        self.middle_name = self.get_middle_name()

        self.submission_dir = self.get_submission_dir()

    def get_middle_name(self):
        split_str_list = self.first_name.split(" ")
        if len(split_str_list) == 1:
            return None
        self.first_name = split_str_list[0].strip()
        return split_str_list[-1].strip()

    def get_iter(self):
        split_str_list = self.first_name.split(",")
        if len(split_str_list) == 1:
            return None
        self.first_name = split_str_list[0].strip()
        return split_str_list[-1].strip()

    def get_submission_dir(self):
        return "{}{}{}".format(
            self.last_name,
            self.iter if self.iter is not None else "",
            self.first_name
        ).lower()

    def __str__(self):
        return "first: {}\tmiddle: {}\titer: {}\tlast: {}".format(
            Functions.str_to_length(self.first_name, 14, do_dots=True),
            Functions.str_to_length(self.middle_name, 14, do_dots=True),
            Functions.str_to_length(self.iter, 14, do_dots=True),
            Functions.str_to_length(self.last_name, 14, do_dots=True)
        )

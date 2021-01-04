import os
import glob
import shutil

from get_student_list import student_list

from General import Constants


def get_student_file_path_list_list(source_dir):

    file_path_list_list = []
    for file_name in os.listdir(source_dir):

        student_name = file_name.split("_")[0]
        file_path_list = glob.glob("{}/{}*".format(source_dir, student_name))
        file_path_list = [f.replace("\\", "/") for f in file_path_list]

        if (student_dir := "{}/{}".format(source_dir, student_name)) in file_path_list:
            file_path_list.remove(student_dir)

        if file_path_list not in file_path_list_list:
            file_path_list_list.append(file_path_list)

    if not file_path_list_list[0]:
        return []
    return file_path_list_list


def group_submissions(source_dir):
    student_file_path_list_list = get_student_file_path_list_list(source_dir)
    for student_file_path_list in student_file_path_list_list:
        student_name = student_file_path_list[0].split("/")[-1].split("_")[0]
        student_dir = "{}/{}".format(source_dir, student_name)

        if not os.path.exists(student_dir):
            os.mkdir(student_dir)

        for student_file_path in student_file_path_list:
            new_file_name = "_".join(student_file_path.split("/")[-1].split("_")[3:])
            new_file_path = "{}/{}/{}".format(source_dir, student_name, new_file_name)
            os.rename(student_file_path, new_file_path)


def move_to_check(source_dir, delete_check_contents=True):

    print("Moving to {}".format(Constants.check_dir))
    if delete_check_contents:
        for file_name in os.listdir(Constants.check_dir):
            file_path = os.path.join(Constants.check_dir, file_name)
            print("\tDeleting", file_name)
            if os.path.isdir(file_path):
                try:
                    shutil.rmtree(file_path)
                except PermissionError:
                    os.rmdir(file_path)
            elif os.path.isfile(file_path):
                os.remove(file_path)
    for student in student_list:
        # print(student.submission_dir)
        if student.submission_dir in os.listdir(source_dir):
            # print(student.submission_dir)
            new_file_path = "{}/{}".format("check_dir", student.submission_dir)
            if not os.path.exists(new_file_path):
                shutil.copytree(
                    "{}/{}".format(source_dir, student.submission_dir),
                    new_file_path
                )
        else:
            # print(student, "not found!")
            pass


def parse_raw_submissions(source_dir):
    group_submissions(source_dir)
    move_to_check(source_dir)


if __name__ == '__main__':
    parse_raw_submissions("2020F_final_project_submissions")

import parse_submissions_download


def main():

    source_dir = "2020F_final_project_submissions"

    parse_submissions_download.group_submissions(source_dir)
    parse_submissions_download.move_to_check(source_dir, delete_check_contents=True)


main()

SIZE_OF_ID = 8
LOCATION_OF_ID = 0
LOCATION_OF_NAME = 1
LOCATION_OF_SEMESTER = 2
LOCATION_OF_GRADE = 3


def check_valid_id(student_id: str) -> bool:
    if len(student_id) != SIZE_OF_ID:
        return False
    if student_id[0] == '0':
        return False
    for digit in student_id:
        if not digit.isdigit():
            return False
    return True


def check_valid_name(name: str) -> bool:
    for letter in name:
        if not letter.isalpha() and not letter == ' ':
            return False
    return True


def check_valid_semester(semester: str) -> bool:
    if not semester.isdigit():
        return False
    if int(semester) < 1:
        return False
    return True


def check_valid_grade_average(grade: str) -> bool:
    if not grade.isdigit():
        return False
    if 100 >= int(grade) > 50:
        return True
    return False


def check_valid_line(line_as_list: list) -> bool:
    return check_valid_id(line_as_list[LOCATION_OF_ID])\
        and check_valid_name(line_as_list[LOCATION_OF_NAME])\
        and check_valid_grade_average(line_as_list[LOCATION_OF_GRADE])\
        and check_valid_semester(line_as_list[LOCATION_OF_SEMESTER])


def calculate_final_grade(student_id: str, hw_grade: int) -> int:
    last_digits_sum = student_id[- 2:]
    return int((int(last_digits_sum) + hw_grade)/2)


#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    f = open(input_path, 'r')
    students = dict()
    for line in f:
        line_as_list = line.split(',')
        line_as_list = [item.strip("\n ") for item in line_as_list]
        if check_valid_line(line_as_list):
            students[line_as_list[LOCATION_OF_ID]] = int(line_as_list[LOCATION_OF_GRADE])
    f.close()
    students_sorted = sorted(students)
    total_grade = 0
    f2 = open(output_path, 'w')
    for index in students_sorted:
        grade = calculate_final_grade(index, students[index])
        f2.write(f"{index}, {students[index]}, {grade}\n")
        total_grade += grade
    f2.close()
    return int(total_grade/len(students))
# TODO: check if print \n in and of file


SIZE_OF_ABC = 26
FIRST_LETTER = 'a'


def make_hist(s: str) -> list:
    s = s.lower()
    letters_histogram = [0]*SIZE_OF_ABC
    for letter in s:
        letters_histogram[ord(letter)-ord(FIRST_LETTER)] += 1
    return letters_histogram


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    first_hist = make_hist(s1)
    second_hist = make_hist(s2)
    for index in range(SIZE_OF_ABC):
        if second_hist[index] < first_hist[index]:
            return False
    return True

from gradesCalc import *


# Testing your implemented functions, feel free to add more tests below
def main():
    # Testing the `final_grade` function
    input_path = 'tests/input'
    output_path = 'tests/out'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    assert course_avg == 70

    # Testing empty input
    input_path_empty = 'tests/empty'
    output_path_empty = 'tests/empty_out'
    course_avg = final_grade(input_path=input_path_empty, output_path=output_path_empty)
    assert course_avg == 0

    # Testing the `check_strings` function
    s1 = 'naanb'
    s2 = 'baNaNa'
    result = check_strings(s1=s1, s2=s2)
    assert check_strings(s1="aabbcc", s2="abcabc")
    assert not check_strings(s1="aaa", s2="abcabc")
    assert check_strings(s1="caba", s2="abcabc")
    assert check_strings(s1="naanb", s2="baNaNa")
    assert not check_strings(s1="ananas", s2="baNaNa")
    assert not check_strings(s1="bannn", s2="baNaNa")
    assert result


if __name__ == "__main__":
    main()

from student import student_details

def test_student_details():
    expected_output = (
        "Student Name: Keerti\n"
        "USN: 01FE24BCA284\n"
        "DIVISION: E\n"
        "Age: 19"
    )

    assert student_details("Keerti", "01FE24BCA284", "E", 19) == expected_output

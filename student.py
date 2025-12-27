def student_details(name, usn, div, age):
    result = (
        f"Student Name: {name}\n"
        f"Student USN : {usn}\n"
        f"Division: {div}\n"
        f"Age: {age}"
    )
    return result


if __name__ == "__main__":
    name = "Keerti"
    usn = "01FE24BCA284"
    div = "E"
    age = 19
    print(student_details(name, usn, div, age))
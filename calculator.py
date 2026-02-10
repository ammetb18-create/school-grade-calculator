def calculate_average(grades):
    return sum(grades) / len(grades)


def get_student_status(average):
    if average >= 6:
        return "Passed"
    else:
        return "Failed"


def main():
    grades = []
    num_grades = int(input("Enter the number of grades: "))

    for i in range(num_grades):
        grade = float(input(f"Enter grade {i + 1}: "))
        grades.append(grade)

    average = calculate_average(grades)
    status = get_student_status(average)

    print(f"\nFinal average: {average:.2f}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()

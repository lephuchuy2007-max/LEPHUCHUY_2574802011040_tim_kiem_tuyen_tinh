# btap15.py

def sort_students(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][0] > students[j+1][0]:
                students[j], students[j+1] = students[j+1], students[j]
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] < students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]
    return students

if __name__ == "__main__":
    students = [('An', 8), ('Ba', 9), ('Cu', 8)]
    print("Sắp xếp danh sách học sinh:", sort_students(students))
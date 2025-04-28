# Riley Ahlrichs        4-4-2025
# Lab 11: This script reads student and score data from files, calculates total scores,
# sums, and averages, and writes the result to a new file called grades.txt.

def read_students(filename):
    student_names = {}
    with open(filename, 'r') as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                student_id = parts[0].strip()
                name = parts[1].strip()
                student_names[student_id] = name
    return student_names

def read_scores(filename):
    student_scores = {}
    with open(filename, 'r') as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                student_id = parts[0].strip()
                score = int(parts[2].strip())
                if student_id not in student_scores:
                    student_scores[student_id] = []
                student_scores[student_id].append(score)
    return student_scores

def calculate_grades(student_names, student_scores):
    grade_data = []

    for student_id in student_names:
        name = student_names[student_id]
        scores = student_scores.get(student_id, [])
        total_scores = len(scores)
        sum_scores = sum(scores)
        avg_score = round(sum_scores / total_scores, 1) if total_scores > 0 else 0.0

        grade_data.append((student_id, name, total_scores, sum_scores, avg_score))

    return grade_data

def write_grades(filename, grade_data):
    with open(filename, 'w') as file:
        file.write("Student ID,Name,Total Scores,Sum of All Scores,Score Average\n")
        for student in grade_data:
            line = f"{student[0]},{student[1]},{student[2]},{student[3]},{student[4]}"
            file.write(line + "\n")
    print(f"Grades successfully written to '{filename}'")

def main():
    # Read student ID to name mapping
    student_names = read_students("students.txt")

    # Read scores and organize them by student ID
    student_scores = read_scores("scores.txt")

    # Calculate grades
    grade_data = calculate_grades(student_names, student_scores)

    # Output to file
    write_grades("grades.txt", grade_data)

if __name__ == "__main__":
    main()
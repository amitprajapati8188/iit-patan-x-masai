# Name: Pritam Jitendra Prajapati
# Roll Number: iitp_aimlh_2601019
# Assignment: Python Functions & Modularity - Student Grade Analyzer

def process_scores(students):
    """Calculates average scores for each student."""
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

def classify_grades(averages):
    """Assigns letter grades based on internal thresholds."""
    GRADE_A = 90
    GRADE_B = 75
    GRADE_C = 60
    
    classified = {}
    for name, avg in averages.items():
        if avg >= GRADE_A:
            grade = 'A'
        elif avg >= GRADE_B:
            grade = 'B'
        elif avg >= GRADE_C:
            grade = 'C'
        else:
            grade = 'F'
        classified[name] = (avg, grade)
    return classified

def generate_report(classified, passing_avg=70):
    """Prints the final report and returns the count of passed students."""
    print("===== Student Grade Report =====")
    total_students = len(classified)
    passed_count = 0
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
            
        print(f"{name:<9} | Avg: {avg:>6.2f} | Grade: {grade} | Status: {status}")
    
    failed_count = total_students - passed_count
    
    print("=" * 32)
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {failed_count}")
    
    return passed_count

if __name__ == "__main__":
    student_data = {
        "Alice": [85, 90, 82, 88],
        "Bob": [60, 65, 58, 67],
        "Clara": [95, 98, 92, 100],
        "Pritam": [70, 75, 80, 72] 
    }

    student_averages = process_scores(student_data)
    classified_data = classify_grades(student_averages)
    total_passed = generate_report(classified_data, passing_avg=70)
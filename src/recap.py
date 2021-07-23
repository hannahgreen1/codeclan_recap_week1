# WRITE YOUR FUNCTIONS HERE
def get_cohort_name(cohort):
    return cohort["cohort_name"]

def get_total_staff(cohort):
    return cohort["staff"]["total_staff"]

def get_student_names(cohort):
    list_students = []
    for student in cohort["students"]:
            list_students.append(student["name"])
    return list_students 
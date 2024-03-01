import pandas as pd

file_path = 'excel.xlsx'
students_data = pd.read_excel(file_path, sheet_name='Frontend Bootcamp Students')

students_data_reset = students_data.reset_index(drop=True)

total_students = len(students_data_reset)

num_males = len(students_data_reset[students_data_reset['Gender'] == 'Male'])
num_females = total_students - num_males

num_tehran = len(students_data_reset[students_data_reset['City'] == 'تهران'])

num_react = len(students_data_reset[students_data_reset['Skills'].str.contains('React', na=False)])
num_framework = len(students_data_reset[students_data_reset['Skills'].str.contains('Vue', na=False)])

num_experienced = len(students_data_reset[students_data_reset['Have Experience'] == 1])

general_info = {
    'Total Students': total_students,
    'Number of Males': num_males,
    'Number of Females': num_females,
    'Number of Students from Tehran': num_tehran,
    'Number of Students with React Knowledge': num_react,
    'Number of Students with any Framework Knowledge': num_framework,
    'Number of Experienced Students': num_experienced
}

print(general_info)

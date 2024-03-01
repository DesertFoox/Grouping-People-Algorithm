import pandas as pd
from grouping import modified_create_priority_groups_refined

# Reading the students data from the Excel file
students_data_path = "excel.xlsx"
students_data = pd.read_excel(students_data_path, sheet_name="Frontend Bootcamp Students")

# Calling the modified_create_priority_groups_refined function to create the priority groups
final_priority_groups = modified_create_priority_groups_refined(students_data)

# Printing the final groups for verification
for i, group in enumerate(final_priority_groups, 1):
    print(f"Group {i}:")
    print(group)
    print("=" * 50)

# You can also save the final groups to a new Excel file if needed
output_path = "final_groups.xlsx"
with pd.ExcelWriter(output_path) as writer:
    for i, group in enumerate(final_priority_groups, 1):
        group.to_excel(writer, sheet_name=f"Group {i}", index=False)

import pandas as pd

def create_city_groups(city_group, students_data):
    groups = []
    while len(city_group) > 0:
        group = pd.DataFrame(columns=city_group.columns)
        experienced_or_react = city_group[
            (city_group['Skills'].str.contains('React', na=False, regex=True)) |
            (city_group['Have Experience'] == 1)
        ]
        basic_skills = city_group[
            city_group['Skills'].str.contains('Js | HTML | Css', na=False, regex=True) &
            ~city_group.index.isin(experienced_or_react.index)
        ]

        if len(experienced_or_react) > 0:
            max_experienced = 2 if len(experienced_or_react) >= 2 else 1
            experienced_to_add = experienced_or_react.head(max_experienced)
            group = pd.concat([group, experienced_to_add])
            city_group = city_group.loc[~city_group.index.isin(experienced_to_add.index)]

        remaining_slots = 6 - len(group)
        members_to_add = basic_skills.head(remaining_slots)
        group = pd.concat([group, members_to_add])
        city_group = city_group.loc[~city_group.index.isin(members_to_add.index)]

        if len(group) >= 3 or len(city_group) == 0:
            groups.append(group)
            students_data = students_data.drop(index=group.index)

    return groups, students_data

def original_create_priority_groups_refined(students_data):
    priority_groups = []
    nearby_cities = [
        ('تهران', 'کرج'),
        ('اصفهان', 'یزد'),
        *[(city, city) for city in students_data['City'].unique() if city not in ('تهران', 'کرج', 'اصفهان', 'یزد')]
    ]

    for city1, city2 in nearby_cities:
        nearby_students = students_data[students_data['City'].isin([city1, city2])]
        new_groups, students_data = create_city_groups(nearby_students, students_data)
        priority_groups.extend(new_groups)

    return priority_groups

def modified_create_priority_groups_refined(students_data):
    priority_groups = original_create_priority_groups_refined(students_data)
    grouped_students = pd.concat(priority_groups, ignore_index=True)
    ungrouped_students = students_data.loc[~students_data.index.isin(grouped_students.index)]
    
    if not ungrouped_students.empty:
        priority_groups.append(ungrouped_students)

    return priority_groups

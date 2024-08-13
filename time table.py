timetable = {
    'Monday': ['Math', 'Science', 'English', 'History', 'Break'],
    'Tuesday': ['Science', 'Math', 'Geography', 'Art', 'Break'],
    'Wednesday': ['English', 'History', 'Math', 'Science', 'Break'],
    'Thursday': ['Geography', 'Art', 'Math', 'English', 'Break'],
    'Friday': ['History', 'English', 'Science', 'Geography', 'Break']
}

# Print the timetable
for day, periods in timetable.items():
    print(f'{day}: {", ".join(periods)}')

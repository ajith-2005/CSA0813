days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
period_duration = 50

timetable = []

for day in days:
    periods = []
for period in range(1, 8):
    periods.append(f'Period {period}: 08:00 AM - 08:50 AM')
    timetable.append({day: periods})
for day_schedule in timetable:
    for day, periods in day_schedule.items():
        print(f'{day}:')
    for period_time in periods:
        print(f'  {period_time}')

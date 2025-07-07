from datetime import datetime, timedelta

def schedule_tasks(tasks, start_time=None, end_time=None):
    if not start_time:
        start_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    if not end_time:
        end_time = start_time.replace(hour=20)

    schedule = []
    current_time = start_time

    for task in tasks:
        duration = timedelta(hours=task.effort_hours)
        if current_time + duration <= end_time:
            schedule.append({
                "title": task.title,
                "start": current_time.strftime("%I:%M %p"),
                "end": (current_time + duration).strftime("%I:%M %p"),
                "score": round(task.priority_score, 2)
            })
            current_time += duration
        else:
            print(f"⚠️ Not enough time for '{task.title}'")

    return schedule

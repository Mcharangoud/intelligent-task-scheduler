from task import Task
from model import train_model, get_features
from scheduler import schedule_tasks
import pandas as pd

tasks = [
    Task("AI Assignment", "2025-07-08 17:00", "High", 3, False),
    Task("Prepare Exam", "2025-07-10 09:00", "Medium", 5, True),
    Task("Team Meeting", "2025-07-07 11:00", "High", 1, False),
    Task("Revise Notes", "2025-07-09 21:00", "Low", 2, True),
]

model = train_model()

for task in tasks:
    features = get_features(task)
    df_feat = pd.DataFrame([features])
    task.priority_score = model.predict(df_feat)[0]

tasks_sorted = sorted(tasks, key=lambda x: x.priority_score, reverse=True)
final_schedule = schedule_tasks(tasks_sorted)

print("\n📅 Optimized Daily Schedule:\n")
for s in final_schedule:
    print(f"{s['start']} - {s['end']}: {s['title']} (Score: {s['score']})")

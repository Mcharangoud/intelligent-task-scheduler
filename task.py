from datetime import datetime
import uuid

class Task:
    def __init__(self, title, deadline, priority, effort_hours, flexible, dependencies=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        self.priority = priority
        self.effort_hours = effort_hours
        self.flexible = flexible
        self.dependencies = dependencies or []
        self.priority_score = 0

    def __repr__(self):
        return f"{self.title} (Priority: {self.priority}, Effort: {self.effort_hours}h, Deadline: {self.deadline})"

import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

def encode_priority(priority):
    return {'Low': 1, 'Medium': 2, 'High': 3}.get(priority, 1)

def get_features(task):
    hours_left = (task.deadline - datetime.now()).total_seconds() / 3600
    return {
        'hours_left': max(hours_left, 0),
        'priority_level': encode_priority(task.priority),
        'effort_hours': task.effort_hours,
        'is_flexible': int(task.flexible),
        'dependency_count': len(task.dependencies)
    }

def train_model():
    data = [
        {'hours_left': 5,  'priority_level': 3, 'effort_hours': 1, 'is_flexible': 0, 'dependency_count': 0, 'priority_score': 95},
        {'hours_left': 48, 'priority_level': 2, 'effort_hours': 3, 'is_flexible': 1, 'dependency_count': 0, 'priority_score': 70},
        {'hours_left': 24, 'priority_level': 1, 'effort_hours': 2, 'is_flexible': 1, 'dependency_count': 1, 'priority_score': 60},
        {'hours_left': 12, 'priority_level': 3, 'effort_hours': 4, 'is_flexible': 0, 'dependency_count': 0, 'priority_score': 90},
        {'hours_left': 72, 'priority_level': 2, 'effort_hours': 1, 'is_flexible': 1, 'dependency_count': 0, 'priority_score': 65},
    ]
    df = pd.DataFrame(data)
    X = df.drop("priority_score", axis=1)
    y = df["priority_score"]
    model = LinearRegression()
    model.fit(X, y)
    return model

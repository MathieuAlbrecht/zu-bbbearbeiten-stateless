from dataclasses import dataclass
from datetime import datetime


todos = []


@dataclass
class Todo:
    title: str
    created_at: datetime
    isCompleted: bool = False



def add(title, created_at):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    if isinstance(created_at, str):
        created_at = datetime.strptime(created_at, "%Y-%m-%d")
    todos.append(Todo(title, created_at))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted

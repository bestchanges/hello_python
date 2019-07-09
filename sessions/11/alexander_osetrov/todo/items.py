from base import Base
from sqlalchemy import Column, Integer, String, Boolean


class Item(Base):

    __tablename__ = 'todo_items'
    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    completed = Column(Boolean, default=True)
    order = Column(Integer)

    def __init__(self, id, title, completed, order):
        self.id = id
        self.title = title
        self.completed = completed
        self.order = order

    def columns(self):
        item = {'id': self.id,
                'title': self.title,
                'completed': self.completed,
                'order': self.order}
        return item

    def __repr__(self):
        return f"<ToDo Item('{self.id}', '{self.title}', '{self.completed}', '{self.order}')"

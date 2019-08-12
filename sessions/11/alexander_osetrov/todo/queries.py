from items import Item
from base import Base, engine, Session


class DBQuery:

    Base.metadata.create_all(engine)

    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def get_items(self):
        query = self.session.query(Item).all()
        items = [item.columns() for item in query]
        return items

    def add_item(self, values):
        self.session.add(values)
        self.session.commit()

    def update_item(self, item_id, values):
        self.session.query(Item).filter(Item.id == item_id).update(values)
        self.session.commit()

    def delete_item(self, item_id):
        self.session.query(Item).filter(Item.id == item_id).delete()
        self.session.commit()

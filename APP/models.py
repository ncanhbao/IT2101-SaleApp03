from APP import db, app
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)


products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://i.pinimg.com/564x/f3/0f/0c/f30f0cabd564ed9cb848c9b416fd9c07.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


# if __name__ == '__main__':
    # with app.app_context():
        # p1 = Product(name="Xiaomi Redmi Note 12", price=5000000, category_id=1)
        # db.session.add(p1)
        # db.session.commit()
        # db.create_all()

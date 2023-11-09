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
    image = Column(String(100), default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fsieuthikhan.com%2Fkhan-gia-dinh&psig=AOvVaw3CGVHaHz_-TD0FOGaP1ZP8&ust=1699594656214000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPiFq9GZtoIDFQAAAAAdAAAAABAD')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        #c1 = Category(name="Mobile")
        #c2 = Category(name="Tablet")
        #c3 = Category(name="Desktop")
        #db.session.add(c1)
        #db.session.add(c2)
        #db.session.add(c3)
        #db.session.commit()
        db.create_all()

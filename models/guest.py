from database import db 


class Guest(db.Model):
   __tablename__ = 'guests'


   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   occupation = db.Column(db.String, nullable=True)  # Add this line to define the occupation


   appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete')


   def to_dict(self):
       return {
           'id': self.id,
           'name': self.name,
           'occupation': self.occupation,  # Include occupation in the dict
           'appearances': [appearance.to_dict() for appearance in self.appearances]
       }

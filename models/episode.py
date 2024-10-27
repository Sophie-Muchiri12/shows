from database import db 



class Episode(db.Model):
   __tablename__ = 'episodes'


   id = db.Column(db.Integer, primary_key=True)
   date = db.Column(db.String, nullable=False)
   number = db.Column(db.Integer, nullable=False)


   appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete')


   def to_dict(self):
       return {
           'id': self.id,
           'date': self.date,
           'number': self.number,
           'appearances': [{'id': appearance.id, 'rating': appearance.rating, 'guest_id': appearance.guest_id} for appearance in self.appearances]
       }

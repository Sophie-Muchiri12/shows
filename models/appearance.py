from database import db 




class Appearance(db.Model):
   __tablename__ = 'appearances'


   id = db.Column(db.Integer, primary_key=True)
   rating = db.Column(db.Integer, nullable=False)
   episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
   guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)


   guest = db.relationship('Guest', back_populates='appearances', cascade='all, delete')
   episode = db.relationship('Episode', back_populates='appearances', cascade='all, delete')


   def to_dict(self):
       return {
           'id': self.id,
           'rating': self.rating,
           'episode_id': self.episode_id,
           'guest_id': self.guest_id,
           'guest_name': self.guest.name,  # Accessing guest name
           'guest_occupation': self.guest.occupation,  # Accessing guest occupation
           'episode_number': self.episode.number  # Optional: Accessing episode number if needed
       }

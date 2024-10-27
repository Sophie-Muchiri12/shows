from app import app, db
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

def seed_database():
    with app.app_context():  # This ensures the application context is available
        # Create and add guests to the database
        guests = [
            {"year": 1999, "occupation": "actor", "show_date": "1999-01-11", "guest_name": "Michael J. Fox"},
            {"year": 1999, "occupation": "Comedian", "show_date": "1999-01-12", "guest_name": "Sandra Bernhard"},
            {"year": 1999, "occupation": "television actress", "show_date": "1999-01-13", "guest_name": "Tracey Ullman"},
            {"year": 1999, "occupation": "film actress", "show_date": "1999-01-14", "guest_name": "Gillian Anderson"},
            {"year": 1999, "occupation": "actor", "show_date": "1999-01-18", "guest_name": "David Alan Grier"},
            {"year": 1999, "occupation": "actor", "show_date": "1999-01-19", "guest_name": "William Baldwin"},
            {"year": 1999, "occupation": "Singer-lyricist", "show_date": "1999-01-20", "guest_name": "Michael Stipe"},
            {"year": 1999, "occupation": "model", "show_date": "1999-01-21", "guest_name": "Carmen Electra"},
            {"year": 1999, "occupation": "actor", "show_date": "1999-01-25", "guest_name": "Matthew Lillard"},
            {"year": 1999, "occupation": "stand-up comedian", "show_date": "1999-01-26", "guest_name": "David Cross"},
            {"year": 1999, "occupation": "actress", "show_date": "1999-01-27", "guest_name": "Yasmine Bleeth"},
            {"year": 1999, "occupation": "actor", "show_date": "1999-01-28", "guest_name": "D. L. Hughley"},
        ]

        for guest_data in guests:
            guest = Guest(name=guest_data['guest_name'], occupation=guest_data['occupation'])  # Corrected 'name' to 'guest_name'
            db.session.add(guest)

        # Create and add episodes to the database
        episodes = [
            {"date": "1/11/99", "number": 1},
            {"date": "1/12/99", "number": 2},
            {"date": "1/13/99", "number": 3},
            {"date": "1/14/99", "number": 4},
            {"date": "1/18/99", "number": 5},
            {"date": "1/19/99", "number": 6},  # Added more episodes for variety
            {"date": "1/20/99", "number": 7},
            {"date": "1/21/99", "number": 8},
            {"date": "1/25/99", "number": 9},
            {"date": "1/26/99", "number": 10},
            {"date": "1/27/99", "number": 11},
            {"date": "1/28/99", "number": 12},
        ]

        for episode_data in episodes:
            episode = Episode(date=episode_data['date'], number=episode_data['number'])
            db.session.add(episode)

        # Commit guests and episodes to the database first
        db.session.commit()

        # Create and add appearances for all guests
        appearances = [
            {"guest_name": "Michael J. Fox", "episode_dates": ["1/11/99"], "rating": 5},
            {"guest_name": "Sandra Bernhard", "episode_dates": ["1/12/99"], "rating": 5},
            {"guest_name": "Tracey Ullman", "episode_dates": ["1/13/99"], "rating": 5},
            {"guest_name": "Gillian Anderson", "episode_dates": ["1/14/99"], "rating": 5},
            {"guest_name": "David Alan Grier", "episode_dates": ["1/18/99"], "rating": 5},
            {"guest_name": "William Baldwin", "episode_dates": ["1/19/99"], "rating": 5},
            {"guest_name": "Michael Stipe", "episode_dates": ["1/20/99"], "rating": 5},
            {"guest_name": "Carmen Electra", "episode_dates": ["1/21/99"], "rating": 5},
            {"guest_name": "Matthew Lillard", "episode_dates": ["1/25/99"], "rating": 5},
            {"guest_name": "David Cross", "episode_dates": ["1/26/99"], "rating": 5},
            {"guest_name": "Yasmine Bleeth", "episode_dates": ["1/27/99"], "rating": 5},
            {"guest_name": "D. L. Hughley", "episode_dates": ["1/28/99"], "rating": 5},
        ]

        for appearance_data in appearances:
            guest = Guest.query.filter_by(name=appearance_data['guest_name']).first()

            for episode_date in appearance_data['episode_dates']:
                episode = Episode.query.filter_by(date=episode_date).first()

                if guest and episode:  # Check if both guest and episode exist
                    # Create and add the appearance
                    appearance = Appearance(guest_id=guest.id, episode_id=episode.id, rating=appearance_data['rating'])
                    db.session.add(appearance)

        # Commit all appearances to the database
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()

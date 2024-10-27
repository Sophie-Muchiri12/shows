from flask import jsonify, request
from database import db
from models import Episode, Guest, Appearance



def create_routes(app):
    # a. GET /episodes
    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        episodes_data = [{"id": episode.id, "date": episode.date, "number": episode.number} for episode in episodes]
        return jsonify(episodes_data), 200

    # b. GET /episodes/:id
    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode(id):
        episode = Episode.query.get(id)
        if episode:
            appearances = Appearance.query.filter_by(episode_id=id).all()
            appearances_data = [
                {
                    "id": appearance.id,
                    "guest_id": appearance.guest_id,
                    "rating": appearance.rating,
                    "episode_id": appearance.episode_id,
                    "guest": {
                        "id": appearance.guest.id,
                        "name": appearance.guest.name,
                        "occupation": appearance.guest.occupation
                    }
                }
                for appearance in appearances
            ]
            episode_data = {
                "id": episode.id,
                "date": episode.date,
                "number": episode.number,
                "appearances": appearances_data
            }
            return jsonify(episode_data), 200
        else:
            return jsonify({"error": "Episode not found"}), 404

    # c. GET /guests
    @app.route('/guests', methods=['GET'])
    def get_guests():
        guests = Guest.query.all()
        guests_data = [{"id": guest.id, "name": guest.name, "occupation": guest.occupation} for guest in guests]
        return jsonify(guests_data), 200

    # d. POST /appearances
    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()

        # Validate the presence of required fields
        if not data:
            return jsonify({"errors": ["No data provided"]}), 400

        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        # Validate rating is between 1 and 5
        if rating is None or not (1 <= rating <= 5):
            return jsonify({"errors": ["Rating must be between 1 and 5"]}), 422

        # Validate the existence of episode and guest
        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)
        if not episode or not guest:
            return jsonify({"errors": ["Invalid episode or guest"]}), 422

        # Create the appearance
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()

        # Prepare response data
        response_data = {
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "episode": {
                "id": episode.id,
                "date": episode.date,
                "number": episode.number
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }

        return jsonify(response_data), 201

    # e. DELETE /episodes/:id
    @app.route('/episodes/<int:id>', methods=['DELETE'])
    def delete_episode(id):
        episode = Episode.query.get(id)
        if episode:
            # First, delete all associated appearances
            appearances = Appearance.query.filter_by(episode_id=id).all()
            for appearance in appearances:
                db.session.delete(appearance)
            
            # Then delete the episode
            db.session.delete(episode)
            db.session.commit()

            return jsonify({"message": "Episode and its appearances deleted successfully"}), 200
        else:
            return jsonify({"error": "Episode not found"}), 404

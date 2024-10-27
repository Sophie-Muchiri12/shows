# Late-Show-

Table of Contents
Project Overview
Features
Technologies Used
Installation
Database Setup
Usage
Routes
Error Handling
Testing the API
Contributing
License
Project Overview
This API provides structured endpoints to handle data related to:

Episodes: TV episodes of the Late Show.
Guests: Guests who have appeared on the Late Show.
Appearances: The appearances of each guest on a specific episode, including ratings.
The project is built using Flask (a Python web framework) and SQLAlchemy (an ORM for database handling). It supports full CRUD functionality for managing the data and uses serializers to return neatly formatted JSON responses.

# Features
CRUD operations for managing episodes, guests, and appearances.
RESTful routes that follow best practices.
Structured JSON responses with nested data (e.g., guests within episodes).

Error handling for invalid requests.
Input validation to ensure correct data handling.

# Technologies Used
Python: Core programming language for the API.
Flask: Web framework used to build the API.
SQLAlchemy: Object Relational Mapper (ORM) for handling database interactions.
SQLite: Relational database used to store data.
Marshmallow: Used for data serialization and deserialization.
Alembic: Used for database migrations.
Installation
To get started with the Late Show API, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/Miguel7113/Late-Show-
cd Late-Show

# Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the dependencies:


pip install -r requirements.txt
Database Setup
Run the database migrations:

flask db upgrade
Seed the database (optional): If you have a seed file, you can use it to populate your database with initial data.

python seed.py
Start the Flask server:

flask run
Your API should now be running at http://127.0.0.1:5000/.

# Usage
You can interact with the API using tools like Postman, curl, or any HTTP client. The following routes are available for interaction.

Routes
Episodes
GET /episodes: Retrieve all episodes with nested guest data.

GET /episodes/
: Retrieve a single episode by its ID, including guest appearances.

Example:

GET http://127.0.0.1:5000/episodes
Guests
GET /guests: Retrieve all guests with nested episodes they have appeared in.

Example:

GET http://127.0.0.1:5000/guests
Appearances
POST /appearances: Create a new appearance by linking a guest to an episode.

Example:

POST http://127.0.0.1:5000/appearances
{
    "episode_id": 1,
    "guest_id": 1,
    "rating": 5
}

# Error Handling
The API provides appropriate error messages and status codes in case of invalid requests.

404 Not Found: When a resource cannot be found.
400 Bad Request: For requests with invalid input or missing data.
For example, if you attempt to create an appearance for an episode that doesn't exist, you'll receive a 404 Not Found response with an error message.

# Testing the API
- Using Postman
Open Postman.
Create a new request for the desired endpoint (e.g., GET /episodes).
Send the request and check the response for correctness.
Using curl
You can also test the API using curl commands. For example:

curl -X GET http://127.0.0.1:5000/episodes
Expected Responses
For each route, the API returns structured JSON data, such as:

Example: GET /episodes


[
  {
    "id": 1,
    "title": "The Late Show Premiere",
    "air_date": "1999-01-11",
    "guests": [
      {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    ]
  }
]
Example: POST /appearances

{
  "id": 1,
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1,
  "episode": {
    "id": 1,
    "title": "The Late Show Premiere",
    "air_date": "1999-01-11"
  },
  "guest": {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
}
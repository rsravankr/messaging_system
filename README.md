# Messaging System API

This project is a RESTful Django-based API for creating and retrieving messages between users. It includes functionalities for user authentication, sending messages, retrieving message threads, and searching within message threads.

## Features

- User authentication (sign up and log in) using email and password.
- Sending messages to other users.
- Retrieving message threads between the logged-in user and other users.
- Searching for a word or phrase within a message thread.

## Technologies Used

- Django
- Django REST framework
- MySQL (to store users, and messages)
- Docker
- Docker Compose

## Prerequisites

- Python 3.6+
- Docker
- Docker Compose

## Project Structure


```
messaging_system/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── messaging_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    └── views.py
```

## Setup and Installation

    
###  Docker Setup
    
```bash
    # Clone the repository:

    git clone https://github.com/rsravankr/messaging_system.git
    cd messaging_system
    
    # Ensure Docker and Docker Compose are installed.

    # Build and start the Docker containers:
  
    docker-compose up --build

    # Run migrations inside the Docker container:
    docker-compose exec web python manage.py migrate
 ```

## Usage
API Endpoints \
Register a new user:

URL: http://localhost:8000/api/auth/register/ \
Method: POST \
Body: JSON 
```
{
    "username": "exampleuser",
    "email": "user@example.com",
    "password": "password123"
}
```

Log in:
URL: http://localhost:8000/api/auth/login/ \
Method: POST \
Body: JSON

```
{
    "username": "exampleuser",
    "password": "password123"
}
```
Send a message:

URL: http://localhost:8000/api/messages/send/ \
Method: POST \
Headers: Authorization token \
Body: JSON \
```
{
    "receiver": 2,
    "content": "Hello, how are you?"
}
```
Retrieve a message thread:

URL: http://localhost:8000/api/messages/thread/<user_id>/ \
Method: GET \
Headers: Authorization token \

Search within messages:

URL: http://localhost:8000/api/messages/search/<user_id>/?query=<search_term> \
Method: GET \
Headers: Authorization token \

### Extensibility

Split message service into 3 seperate services for the apis
1. Auth service
2. Message Service
3. Search service
# Python Flask - Rest API
This project is based on Advanced REST APIs Flask Python course you can find on Udemy.

External URL: https://www.udemy.com/course/advanced-rest-apis-flask-python

# Features
In this project you can find a lot of powerful features, which was covered in this course and extended by me.

## Topics covered:

* Marshmallow for data serialization and deserialization
* Send e-mails and user confirmations
* Upload images
* Postgres Integration
* Database migrations
* Handle payments using Stripe

## To Do:
* Third party login using OAuth (GitHub is used as the example)
* Flask Babel translations
* Pagination

## Extended:

* Password encryption
* Upload videos

# Endpoints

Below you can find all available endpoints.

| Method | URI | Protected | Description |
|--------|-----|-----------|-------------|
| POST   | `/register` | No | Register new User |
| POST   | `/login` | No | Login User |
| POST   | `/refresh` | Yes | Refresh access token |
| POST   | `/logout` | Yes | Logout User |
| GET    | `/user_confirm/<string:confirmation_id>` | No | Confirm User registration |
| GET    | `/confirmation/user/<int:user_id>` | No | This endpoint is used for testing and viewing Confirmation models and should not be exposed to public |
| POST   | `/confirmation/user/<int:user_id>` | No | Resend confirmation email |
| GET    | `/user/<int:user_id>` | No | Get User data |
| DELETE | `/user/<int:user_id>` | No | Delete User |
| POST   | `/upload/image` | Yes | Upload User image |
| GET    | `/image/<string:filename>` | Yes | Get image by filename |
| DELETE | `/image/<string:filename>` | Yes | Delete image by filename |
| PUT    | `/upload/avatar` | Yes | Upload User avatar image |
| GET    | `/avatar/<int:user_id>` | No | Get User avatar |
| GET    | `/items` | No | Get items list |
| GET    | `/item/<string:name>` | No | Get item data |
| POST   | `/item/<string:name>` | Yes | Store new item |
| PUT    | `/item/<string:name>` | Yes | Update item data |
| DELETE | `/item/<string:name>` | Yes | Delete item |
| GET    | `/stores` | No | Get stores list |
| GET    | `/store/<string:name>` | No | Get store data |
| POST   | `/store/<string:name>` | No | Store new store |
| DELETE | `/store/<string:name>` | No | Delete store |
| GET    | `/orders` | No | Get orders data |
| POST   | `/orders` | No | Store new order |


# Dockerize

Run `docker-compose up --build` to build the project or `python app.py`.

# Black
Black is the uncompromising Python code formatter. You can run every command inside container using `docker exec -it {container_name} {command}`
To run Black use `docker exec -it {container_name} black .`

# Database Migrations

1. Run `docker-compose exec python flask db init` to initialize migrations (if not exists).
2. Run `docker-compose exec python flask db migrate` to create new migrations.
3. Run `docker-compose exec python flask db upgrade` to upgrade a database.
4. Run `docker-compose exec python flask db downgrade` to downgrade a database.

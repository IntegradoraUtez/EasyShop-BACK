import json
import pymysql
from shared.database_manager import DatabaseConfig


def lambda_handler(event, context):
    jsonBody = json.loads(event['body'])
    email = jsonBody['email']
    password = jsonBody['password']
    name = jsonBody['name']
    lastname = jsonBody['lastname']
    birthdate = jsonBody['birthdate']
    gender = jsonBody['gender']
    type = jsonBody['type']
    id = jsonBody['id']

    if email is None or password is None or name is None or lastname is None or birthdate is None or gender is None or type is None or id is None:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Missing required fields"
            }),
        }

    update_user_put(email, password, name, lastname, birthdate, gender, type, id)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User updated successfully"
        }),
    }


def update_user_put(email, password, name, lastname, birthdate, gender, type, id):
    db = DatabaseConfig()
    connection = db.get_new_connection()

    try:
        with connection.cursor() as cursor:
            insert_query = "UPDATE Users SET email=%s, password=%s, name=%s, lastname=%s, birthdate=%s, gender = %s, type = %s WHERE id = %s"
            cursor.execute(insert_query, (email, password, name, lastname, birthdate, gender, type, id))
            connection.commit()
    finally:
        connection.close()



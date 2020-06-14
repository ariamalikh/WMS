from database import connect
import psycopg2

def create_user(full_name, email, username, password, role_id):
    """ insert a new role into the user table """
    sql = """INSERT INTO public."User"(full_name, email, username, password, role_id)
             VALUES(%s, %s, %s, %s, %s) RETURNING id;"""

    conn = None
    user_id = None
    try:
        conn, cur = connect()

        cur.execute(sql, (full_name, email, username, password, role_id))

        #get the current generated id back
        user_id = cur.fetchone()[0]

        #commit the changes to the database
        conn.commit()

        #close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id
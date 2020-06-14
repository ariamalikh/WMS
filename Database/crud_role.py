from database import connect
import psycopg2

def create_role(role_name, description):
    """ insert a new role into the role table """
    sql = """INSERT INTO public."Role"(role_name, description)
             VALUES(%s, %s) RETURNING id;"""

    conn = None
    role_id = None
    try:
        conn, cur = connect()

        cur.execute(sql, (role_name, description,))

        #get the current generated id back
        role_id = cur.fetchone()[0]

        #commit the changes to the database
        conn.commit()

        #close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return role_id

    
import connect 

def read_reg() :
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM Clientes"

    cursor.execute(sql_read)
    conn.commit()

    result = cursor.fetchall()
    
    return result
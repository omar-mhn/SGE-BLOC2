import connect 

def read_reg() :
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_read = "SELECT * FROM Clientes"

    cursor.execute(sql_read)
    conn.commit()

    result = cursor.fetchall()

    #print(result[9])
    #print(result[9][3])
    #print(result[14])
    #print(result[14][1])
    #print(result[19])
    #print(result[19][4])




    return result

read_reg()
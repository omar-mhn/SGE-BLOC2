import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE Clientes
    SET Nombre_Cliente= 'Lyes'
    WHERE Nombre_Cliente = 'Aleix'
    '''
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}
import connect

# fonction pour créer un enregistrement dans la DB avec une requête préparée
def create_reg():
    # créer la connexion et la garde dans une variable conn
    conn = connect.connection_db()

    #créer un curseur avec la conneion gardée dans la variable conn
    cursor = conn.cursor()

   #Consulta preparada amb %s
    sql_create = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

    # Valeurs à ajouter, dans l'ordre, aux %s de VALUES de la requête préparée.
    values=('omar', 'carrer de columbia', '624413452', 'correu@correu.com', '12_09_1998')
    
    # maintenant envoyer la consultation preparé avec les valeurs utulisant le curseur 
    cursor.execute(sql_create,values)

    # faire les modifications a la BD selon execute()
    conn.commit()

    # fermer les connexions 
    conn.close()
    cursor.close()
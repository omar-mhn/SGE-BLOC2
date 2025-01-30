import create_registre as cr
import read_registre as rr


#Trucada per executar la funció a l'arxiu create_registre.py
#cr.create_reg()
result = rr.read_reg()
for i in result:
    print('\n')
    print('Nom: ' + i[1])
    print('Adreca: ' + i[2])
    print('telèfon: ' + i[3])
    print('email: ' + i[4])
    print('neixament ' + i[5])


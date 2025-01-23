import create_registre as cr
import read_registre as rr

#Appel pour exécuter la fonction dans le fichier create_registre.py
# cr.create_reg()

results = rr.read_reg()

for i in results:
    print('\n')
    print('Nom: ' + i[0])
    print('Adrece: ' + i[1])
    print('telèfon: ' + i[2])
    print('email: ' + i[3])
    print('neixament: ' + i[4])

    print(results)
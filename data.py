import sqlite3

path = 
banco = sqlite3.connect(path + )
cursor = banco.cursor()

#Marcas
cursor.execute("INSERT INTO Marcas VALUES(1, 'Natura')")
cursor.execute("INSERT INTO Marcas VALUES(2, 'Oboticário')")

#Fixaxoes
cursor.execute("INSERT INTO Fixaxoes VALUES (1, 'Delicado')")
cursor.execute("INSERT INTO Fixaxoes VALUES(2, 'Sensual')")

#Volumes
cursor.execute("INSERT INTO Volumes VALUES(1, 'Elmo Vol. 2')")
cursor.execute("INSERT INTO Volumes VALUES(2, 'Royalty Vol. 1')")

#Essencias
cursor.execute("INSERT INTO Essencias VALUES(1, 'Extravagante')")
cursor.execute("INSERT INTO Essencias VALUES(2, 'Suave')")

#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES(1, 'Elmo', 25, 1, 1, 1)")
cursor.execute("INSERT INTO Perfumes VALUES(2, 'Royalty', 30, 2, 2, 2)")

#Essencia_Perfume
cursor.execute("INSERT INTO Essencia_Perfume VALUES(2, 1)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1, 2)")
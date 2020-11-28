#Importando SQLite
import sqlite3

#Definindo Caminho
path = 
banco = sqlite3.connect(path + )
cursor = banco.cursor()

#Começando as tabelas do BD
cursor.execute('CREATE TABLE IF NOT EXISTS Marcas(id integer, nome text)')
cursor.execute('CREATE TABLE IF NOT EXISTS Fixaxoes(id integer, nome text)')
cursor.execute('CREATE TABLE IF NOT EXISTS Volumes(id integer, nome text)')
cursor.execute('CREATE TABLE IF NOT EXISTS Essencias(id integer, nome text)')
cursor.execute('CREATE TABLE IF NOT EXISTS Perfumes(id integer, nome text, quantidade integer, id_volume_FK integer, id_marca_FK integer, id_fixaxoes_FK integer)')
cursor.execute('CREATE TABLE IF NOT EXISTS Essencia_Perfume(id_essencia_FK integer, id_perfume_FK integer)')

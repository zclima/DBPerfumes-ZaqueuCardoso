import  sqlite3

def titulo(n, s):
    print('=' * n)
    print(f'{s}'.center(n))
    print('=' * n)

path = 
banco = sqlite3.connect(path + )
cursor = banco.cursor()

#Perfume e marca
cursor.execute("SELECT * FROM Perfumes AS P JOIN Marcas AS M ON P.id_marcas_FK = M.id")
tabela = cursor.fetchall()
titulo(78, 'Perfume Marca')
print('ID'.ljust(5) + 'Nome'.ljust(21) + 'M.Nome'.ljust(20) + 'Quantidade'.ljust(10))
for linha in tabela:
    print(str(linha[0]).ljust(5), end='')
    print(linha[5].ljust(21), end='')
    print(linha[4].ljust(20), end='')
    print(linha[1])

#Marca
cursor.execute("SELECT * FROM Marca ORDEM BY nome")
tabela = cursor.fetchall()
titulo(78, 'Marcas')
print('ID'.ljust(5) + 'Marcas'.ljust(21))
for linha in tabela:
    print(str(linha[0]).ljust(5), end='')
    print(linha[5])

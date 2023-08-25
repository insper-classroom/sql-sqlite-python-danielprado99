
class SQL:
    def __init__(self, nome_tabela, conn):
        self.nome_tabela = nome_tabela
        self.conn = conn
        self.cursor = conn.cursor()

    def cria_tabela(self, lista_colunas):
        fila = f'CREATE TABLE IF NOT EXISTS {self.nome_tabela} (ID INTEGER PRIMARY KEY AUTOINCREMENT,'

        for i in range(len(lista_colunas)-1):
            fila += f'{lista_colunas[i][0]} {lista_colunas[i][1]},'

        fila += f'{lista_colunas[-1][0]} {lista_colunas[-1][1]})'

        self.cursor.execute(fila)
        

    def insere_registo(self):
        fila = f'INSERT INTO {self.nome_tabela} ('

        for i in range(len(lista_colunas)-1):
            fila += f'{lista_colunas[i][0]},'

        fila += f'{lista_colunas[-1][0]} VALUES ('

        for i in range(len(lista_colunas)-1):
            fila += '?, '
        
        fila += '?);'

        self.cursor.executemany(fila, self.nome_tabela)
        self.conn.commit()

    
    
        

        



        


tabela = SQL('estudantes', 'conn')

lista_colunas = [['Nome', 'TEXT NOT NULL'], ['Idade', 'INTEGER']] 







             




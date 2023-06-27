import sqlite3
from utils import *

db_arquivo = './clientes.sqlite3'

class DBCliente():

    def __init__(self):
        self.con = sqlite3.connect(db_arquivo)
        self.cur = self.con.cursor()

    def get_cliente(self, valor):
        c = {}
        try:
            sql = f"SELECT * FROM Cliente WHERE cpf like '%{valor}%'"
            result = self.cur.execute(sql)
            cliente = result.fetchone()
            desc = self.cur.description
            for i in range(len(cliente)):
                c.update({desc[i][0]:cliente[i]})
        except TypeError:
            sql = f"SELECT * FROM Cliente WHERE nome like '%{valor}%'"
            result = self.cur.execute(sql)
            cliente = result.fetchone()
            desc = self.cur.description
            for i in range(len(cliente)):
                c.update({desc[i][0]:cliente[i]})
        except:
            c = { 'error': 'Cliente not found'}
        finally:
            return c

    def get_enderecos(self, cpf):
        sql = f'SELECT * FROM Endereco WHERE id_cliente_fk = {cpf}'
        enderecos = {}
        try:
            result = self.cur.execute(sql)
            lista_enderecos = result.fetchall()
            desc = self.cur.description()
        except:
            pass
        return lista_enderecos

    def get_tipo_endereco(self):

        sql = 'SELECT * FROM Tipo_Endereco'

        result = self.cur.execute(sql)
        tipos = result.fetchall()
        tipo = {}
        for t in tipos:
            tipo.update(to_dict(t))
        return tipo

    def get_tipo_telefone(self):

        sql = 'SELECT * FROM Tipo_Telefone'

        result = self.cur.execute(sql)
        tipos = result.fetchall()
        tipo = {}
        for t in tipos:
            tipo.update(to_dict(t))
        return tipo
        
    def get_estados(self):

        sql = 'SELECT * FROM Estado'

        result = self.cur.execute(sql)
        estados = result.fetchall()
        est = {}
        for estado in estados:
            est.update(to_dict(estado))
        return est



if __name__ == '__main__':
    clientes = DBCliente()
    a = clientes.get_enderecos('11111111111')
    print(a)
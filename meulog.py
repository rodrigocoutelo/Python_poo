import datetime as dt

class Meulog():

  def __init__():
    pass

  @staticmethod
  def entrada(classe, metodo,acao, *parameteros):
    hora = dt.datetime.now()
    print (f"[{hora} | Classe: {classe} | Metodo: {metodo} | Ação: {acao} | Parameteros: {parameteros}")

  @staticmethod
  def saida(classe, metodo,acao, *valores):
    hora = dt.datetime.now()
    print (f"[{hora} | Classe: {classe} | Metodo: {metodo} | Ação: {acao} | Valores Retornados: {valores}")

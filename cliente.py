import random
import datetime as dt
from loja import Loja


class Cliente(object):

  def __init__(self, nome):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    self.hora_aluguel = None
    self.quantidade = None
    self.modalidade = None
    print(f"Classe Cliente | Metodo Construtor | Cria instância de cliente\n{self}\n")

  def __repr__(self)->str:
    return f"[Cliente -> id:{self._id}|nome:{self.nome}|hora alguel:{self.hora_aluguel}]"

  def alugar(self, quantidade, modalidade, loja):
    if not isinstance(loja, Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo alugar | parametro loja inválido. Tipo {type(loja)}')

    print(f"Classe Cliente | Metodo alugar | Cliente {self.nome} solicita o aluguel de {quantidade} de bicicletas na modalidade {modalidade} a loja {loja.nome}\n{self}\n")
    self.hora_aluguel = dt.datetime.now()
    self.quantidade = quantidade
    return loja.locar(self)

  def devolver(self, loja)->float:
    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  devolve os produtos a {loja.nome}\n{self}\n")
    valor_locacao = loja.receber(self)
    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  recebe da {loja.nome} o valor total da locação R${valor_locacao}\n{self}\n")
    return valor_locacao

  def ler_estoque(self, loja)->int:
    if not isinstance(loja, Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo ler_estoque | parametro loja inválido. Tipo {type(loja)}')
    print(f"Classe Cliente | Metodo ler_estoque | Cliente {self.nome} vê o estoque da loja {loja.nome}\n{self}\n")
    return loja.mostrar_estoque()



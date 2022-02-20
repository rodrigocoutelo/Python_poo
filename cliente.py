import random
from locacao import Locacao
from loja import Loja


class Cliente(object):

  def __init__(self, nome):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    print(f"Classe Cliente | Metodo Construtor | Cria instância de cliente\n{self}\n")

  def __repr__(self)->str:
    return f"[Cliente -> id:{self._id}|nome:{self.nome}]"

  def alugar(self, quantidade, modalidade, loja)->Locacao:
    if not isinstance(loja, Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo alugar | parametro loja inválido. Tipo {type(loja)}')
    print(f"Classe Cliente | Metodo alugar | Cliente {self.nome} solicita o aluguel de {quantidade} de bicicletas na modalidade {modalidade} a loja {loja.nome}\n{self}\n")
    locacao = Locacao(self, loja, quantidade, modalidade)
    return loja.locar(locacao)

  def devolver(self, locacao:Locacao)->float:
    if not isinstance(locacao,Locacao):
     raise ValueError(f'Erro | Classe Cliente  | Metodo devolver - parametro locacao inválido. Tipo {type(locacao)}')

    if locacao.cliente != self:
      raise Exception(f"Erro | Classe Cliente  | Metodo devolver | Essa locação não pertence ao cliente {self.nome}")

    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  devolve os produtos a {locacao.loja.nome}\n{locacao}\n")

    locacao = locacao.loja.receber(locacao)

    print(f"Classe Cliente | Metodo devolver | Cliente {self.nome}  recebe da {locacao.loja.nome} o valor total da locação R${locacao.valor_locacao}\n{locacao}\n")

    return locacao.valor_locacao

  def ler_estoque(self, loja)->int:
    if not isinstance(loja, Loja):
      raise ValueError(f'Erro | Classe Cliente | Metodo ler_estoque | parametro loja inválido. Tipo {type(loja)}')
    print(f"Classe Cliente | Metodo ler_estoque | Cliente {self.nome} vê o estoque da loja {loja.nome}\n{self}\n")
    return loja.mostrar_estoque()



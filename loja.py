import random
import locacao as loc
from locacao import Locacao


class Loja(object):

  def __init__(self, nome:str, estoque:int):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    self._estoque = estoque
    if type(estoque) != int:
      raise ValueError(f"Erro | Classe Loja | Metodo Construtor | parametro estoque inválido. Tipo {type(estoque)}")

    print(f"Classe Loja | Metodo Construtor | Cria instância de Loja\n{self}\n")

  def __repr__(self)->str:
    return f"[Loja -> Id: {self._id}|Nome: {self.nome}|Estoque: {self._estoque}]\n"

  def mostrar_estoque(self)->int:
    print(f"Classe Loja | Metodo mostrar_estoque | Loja {self.nome} mostra o estoque ao Cliente\n{self}\n")
    return self._estoque

  def locar(self, locacao:Locacao)->Locacao:
    if locacao.quantidade > self._estoque:
      raise Exception(f"Erro | Classe Loja | Metodo locar | Loja {self.nome} com estoque indisponível")

    self._estoque -= locacao.quantidade
    locacao.abrir_locacao()
    print(f"Classe Loja | Metodo locar | Loja {self.nome} recebe pedido de locação do Cliente {locacao.cliente.nome}\n{locacao}\n")
    return locacao

  def receber(self, locacao:Locacao)->Locacao:
    if not isinstance(locacao, Locacao):
      raise ValueError(f'Erro | Classe Loja |Metodo receber | parametro locacao inválido. Tipo {type(locacao)}')
    if locacao.status == None:
      raise Exception(f"Erro | Classe Loja | Metodo receber | Locação não aberta. Não pode ser devolvida.")
    if locacao.status == loc._FECHADA:
      raise Exception (f"Erro | Classe Loja | Metodo receber | Locação encerrada. Não pode ser mais devolvida.")

    print(f"Classe Loja | Metodo receber | Loja {self.nome} recebeu os produtos de volta do Cliente {locacao.cliente.nome} e vai processar os cálculos\n{locacao}\n")

    self._estoque += locacao.quantidade
    valor_locacao = self.calcula_valor_locacao(locacao)
    locacao.valor_locacao = valor_locacao
    locacao.fechar_locacao()
    return locacao

  def calcula_valor_locacao(self, locacao:Locacao)->float:
    print(f"Classe Loja | Metodo calcula_valor_locacao | Loja {self.nome} calcula o valor da locação\n{locacao}\n")
    locacao.calcula_tempo_locacao()
    if locacao.modalidade == loc._HORA:
      valor_locacao = locacao.duracao_locacao * 5 * locacao.quantidade
    elif locacao.modalidade == loc._DIA:
      valor_locacao = locacao.duracao_locacao * 25 * locacao.quantidade
    elif locacao.modalidade == loc._SEMANA:
       valor_locacao = locacao.duracao_locacao * 100 * locacao.quantidade

    if self.is_elegivel_desconto(locacao):
      valor_locacao = 0.7 * valor_locacao
    print(f"Classe Loja | Metodo is_elegivel_desconto | Loja {self.nome} checa se o produto é elegivel de desconto | Retorno {self.is_elegivel_desconto(locacao)}\n{locacao}\n")
    return valor_locacao


  def is_elegivel_desconto(self, locacao:Locacao)->bool:
    if (locacao.quantidade >= 3):
      return True
    return False

import random
import datetime as dt

from cliente import Cliente


class Loja(object):

  def __init__(self, nome:str, estoque:int):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    self._estoque = estoque
    self._inicio = None
    self._fim = None

    if type(estoque) != int:
      raise ValueError(f"Erro | Classe Loja | Metodo Construtor | parametro estoque inválido. Tipo {type(estoque)}")

    print(f"Classe Loja | Metodo Construtor | Cria instância de Loja\n{self}\n")

  def __repr__(self)->str:
    return f"[Loja -> Id: {self._id}|Nome: {self.nome}|Estoque: {self._estoque}]\n"

  def mostrar_estoque(self)->int:
    print(f"Classe Loja | Metodo mostrar_estoque | Loja {self.nome} mostra o estoque ao Cliente\n{self}\n")
    return self._estoque

  def locar(self, cliente) -> Cliente:
    if cliente.quantidade > self._estoque:
      raise Exception(f"Erro | Classe Loja | Metodo locar | Loja {self.nome} com estoque indisponível")
    if not isinstance(cliente,Cliente):
      raise Exception(f"Erro | Classe Loja | Metodo locar | parametro loja inválido. Tipo {type(cliente)}")
    self._estoque -= cliente.quantidade
    self._inicio = cliente.hora_aluguel
    print(f"Classe Loja | Metodo locar | Loja {self.nome} recebe pedido de locação do Cliente {cliente.nome}\n")
    return cliente

  def receber(self, cliente:Cliente) -> float:
    print(f"Classe Loja | Metodo receber | Loja {self.nome} recebeu os produtos de volta do Cliente {cliente.nome} e vai processar os cálculos\n")
    self._estoque += cliente.quantidade
    self._fim = cliente.hora_aluguel
    valor_locacao = self.calcula_valor_locacao(cliente)
    return valor_locacao

  def calcula_valor_locacao(self, cliente:Cliente)->float:
    print(f"Classe Loja | Metodo calcula_valor_locacao | Loja {self.nome} calcula o valor da locação\n")
    duracao_locacao = self.calcula_tempo_locacao()
    if cliente.modalidade == "hora":
      valor_locacao = cliente.duracao_locacao * 5 * cliente.quantidade
    elif cliente.modalidade == "dia":
      valor_locacao = cliente.duracao_locacao * 25 * cliente.quantidade
    elif cliente.modalidade == "semana":
       valor_locacao = cliente.duracao_locacao * 100 * cliente.quantidade

    if self.is_elegivel_desconto(cliente):
      valor_locacao = 0.7 * valor_locacao
    print(f"Classe Loja | Metodo is_elegivel_desconto | Loja {self.nome} checa se o produto é elegivel de desconto | Retorno {self.is_elegivel_desconto(cliente)}\n")
    return valor_locacao


  def is_elegivel_desconto(self, cliente:Cliente)->bool:
    if (cliente.quantidade >= 3):
      return True
    return False

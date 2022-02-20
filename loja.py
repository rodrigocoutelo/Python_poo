import random
import datetime as dt


class Loja(object):

  def __init__(self, nome:str, estoque:int):
    self._id = random.randint(1,999) #simulando a geraçao de id único para loja
    self.nome = nome
    self._estoque = estoque
    self._inicio = None
    self._fim = None

    if type(estoque) != int:
      raise Exception(f"Erro | Classe Loja | Metodo Construtor | parametro estoque inválido. Tipo {type(estoque)}")

    print(f"Classe Loja | Metodo Construtor | Cria instância de Loja\n{self}\n")

  def __repr__(self)->str:
    return f"[Loja -> Id: {self._id}|Nome: {self.nome}|Estoque: {self._estoque}]\n"

  def mostrar_estoque(self)->int:
    print(f"Classe Loja | Metodo mostrar_estoque | Loja {self.nome} mostra o estoque de {self._estoque} bicletas ao Cliente\n")
    return self._estoque

  def locar(self, cliente):
    if cliente.quantidade > self._estoque:
      raise Exception(f"Erro | Classe Loja | Metodo locar | Loja {self.nome} com estoque indisponível. Solicitado: {cliente.quantidade} - Disponível {self._estoque}")

    if cliente.hora_aluguel != None :
      raise Exception(f"Erro | Classe Loja | Metodo locar | Cliente {cliente.nome} já tem uma locação em andamento")

    if cliente.quantidade <= 0 :
      raise Exception(f"Erro | Classe Loja | Metodo locar | parametro loja inválido. Quantidade 0 ou negativa [{cliente.quantidade}] ")


    cliente.hora_aluguel = dt.datetime.now()
    self._estoque -= cliente.quantidade
    self._inicio = dt.datetime.now()

    print(f"Classe Loja | Metodo locar | Loja {self.nome} recebe pedido de locação do Cliente {cliente.nome}\n{cliente}\n")
    return cliente

  def receber(self, cliente) -> float:
    print(f"Classe Loja | Metodo receber | Loja {self.nome} recebeu os produtos de volta do Cliente {cliente.nome} e vai cálcular o valor da locação\n{self}\n{cliente}\n")
    self._estoque += cliente.quantidade
    self._fim = cliente.hora_aluguel
    valor_locacao = self.calcula_valor_locacao(cliente)
    print(f"Classe Loja | Metodo receber | Loja {self.nome} devolve o valor da locação ao Cliente {cliente.nome}\n{self}\n{cliente}\n")
    return valor_locacao

  def calcula_valor_locacao(self, cliente)->float:
    print(f"Classe Loja | Metodo calcula_valor_locacao | Loja {self.nome} calcula o valor da locação do Cliente {cliente.nome}\n{self}\n{cliente}\n")
    duracao_locacao = self.calcula_tempo_locacao(cliente)
    if cliente.modalidade == "hora":
      valor_locacao = duracao_locacao * 5 * cliente.quantidade
    elif cliente.modalidade == "dia":
      valor_locacao = duracao_locacao * 25 * cliente.quantidade
    elif cliente.modalidade == "semana":
       valor_locacao = duracao_locacao * 100 * cliente.quantidade

    if self.is_elegivel_desconto(cliente):
      valor_locacao = 0.7 * valor_locacao
    print(f"Classe Loja | Metodo is_elegivel_desconto | Loja {self.nome} checa se o produto é elegivel de desconto | Retorno {self.is_elegivel_desconto(cliente)}\n{cliente}\n")
    return valor_locacao


  def calcula_tempo_locacao(self, cliente):
    if self._fim == None:
       self._fim = dt.datetime.now()

    duracao_em_segundos = (self._fim - self._inicio).total_seconds()
    print(f"Classe Locação | Método calcula_tempo_locacao | Calcula o tempo da locação na base escolhida no momento da locação \n{self}\n{cliente}\n")
    duracao_locacao = round(duracao_em_segundos / cliente._base_locacao,2)
    cliente.duracao_locacao = duracao_locacao
    return duracao_locacao

  def is_elegivel_desconto(self, cliente)->bool:
    if (cliente.quantidade >= 3):
      return True
    return False

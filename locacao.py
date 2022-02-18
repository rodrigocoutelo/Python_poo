import datetime as dt
import cliente as Cliente
import loja as Loja

_HORA = "hora"
_DIA = "dia"
_SEMANA = "semana"

class Locacao(object):

  def __init__(self, cliente:Cliente, loja:Loja, quantidade, modalidade):
    self.cliente = cliente
    self.loja = loja
    self.quantidade = quantidade
    self.modalidade = modalidade
    self.inicio = dt.datetime.now()
    self.fim = None
    self.base_locacao = None
    self._duracao_locacao = None
    self._preco_final = None

    if modalidade == _HORA:
      self.base_locacao = 3600
    elif modalidade == _DIA:
      self.base_locacao = 24*3600
    elif modalidade == _SEMANA:
      self.base_locacao = 7*24*3600
    else:
      raise Exception("Modalidade Inválida")

  def calcula_tempo_locacao(self):
    duracao_em_segundos = (self.fim - self.inicio).total_seconds()
    self.duracao_locacao = duracao_em_segundos / self.base_locacao

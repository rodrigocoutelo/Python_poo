import datetime as dt


class Locacao(object):

  def __init__(self, cliente:Cliente, loja:Loja, quantidade, modadiliadae, inicio=dt.datetime.now()):
    self.cliente = cliente
    self.loja = loja
    self.quantidade = quantidade
    self.modadiliadae = modadiliadae
    self.inicio = inicio
    self.fim = None


def calcula_tempo_locacao():
   (self.fim - self.inicio).total_seconds()

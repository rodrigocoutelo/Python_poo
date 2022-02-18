import locacao as Locacao
import cliente as Cliente

class Loja(object):

  def __init__(self, nome, estoque):
    self.nome = nome
    self._estoque = estoque

  def mostrar_estoque(self):
    return self._estoque

  def locar(self, locacao):
    if locacao.quantidade > self._estoque:
      raise Exception("Estoque indisponível")
    self._estoque -= locacao.quantidade
    return locacao

  def receber(self, locacao):
    self._estoque += locacao.quantidade
    locacao.calcula_tempo_locacao()
    if locacao.modalidade == Locacao._HORA:
      valor_locacao = locacao.duracao_locacao * 5 * locacao.quantidade
    elif locacao.modalidade == Locacao._DIA:
      valor_locacao = locacao.duracao_locacao * 25 * locacao.quantidade
    elif locacao.modalidade == Locacao._SEMANA:
       valor_locacao = locacao.duracao_locacao * 100 * locacao.quantidade

    if locacao.quantidade >= 3:
      valor_locacao = 0.7 * valor_locacao

    locacao._preco_final = valor_locacao

    return locacao

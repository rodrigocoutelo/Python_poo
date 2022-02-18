import datetime as dt
from locacao import Locacao

class Cliente(object):

  def __init__(self, nome):
    self.nome = nome
    self.locacoes = []


  def olhar_estoque(self, loja):
    print(loja.mostrar_estoque())

  def alugar(self, quantidade, modalidade, loja):
    locacao = Locacao(self,loja, quantidade, modalidade)
    return loja.locar(locacao)

  def delvover(self, locacao):
    if locacao.cliente != self:
      raise Exception("Essa locação não pertence a esse cliente")

    locacao =locacao.loja.receber(locacao)
    print("Valor da Total da Locação R$", round(locacao._preco_final,2))
    return locacao._preco_final


import datetime as dt


class Cliente(object):

  def __init__(self, nome):
    self.nome = nome
    self.hora_aluguel = None
    self.quantidade = None
    self.modalidade = None

  def olhar_estoque(self, loja):
    print(loja.mostrar_estoque())

  def alugar(self, quantidade, modalidade, loja):
    self.hora_aluguel = dt.datetime.now()
    self.quantidade = quantidade
    self.modalidade = modalidade
    loja.locar(self)

  def delvover(self, loja):
    if self.hora_aluguel == None:
      self.hora_aluguel = dt.datetime.now()
    print("R$", round(loja.receber(self),2))#metodo da loja que recebe as biciletas


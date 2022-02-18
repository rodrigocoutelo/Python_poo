from cliente import Cliente

class Loja(object):

  def __init__(self, nome, estoque):
    self.nome = nome
    self._estoque = estoque
    self.data_inicio = None
    self.data_fim = None

  def mostrar_estoque(self):
    return self._estoque

  def locar(self, cliente):
    print(cliente.nome, cliente.quantidade, cliente.modalidade, cliente.hora_aluguel)
    if cliente.quantidade > self._estoque:
      raise Exception("Estoque indisponível")
    self._estoque -= cliente.quantidade
    self.data_inicio = cliente.hora_aluguel

  def receber(self, cliente):
    print(cliente.nome, cliente.quantidade, cliente.modalidade, cliente.hora_aluguel)
    self._estoque += cliente.quantidade
    self.data_fim =  cliente.hora_aluguel
    duracao = (self.data_fim - self.data_inicio).total_seconds() #em segundos
    if cliente.modalidade == "hora":
      duracao_modalidade = duracao/3600
      valor_locacao = duracao_modalidade * 5 * cliente.quantidade
    elif cliente.modalidade == "dia":
      duracao_modalidade = duracao/(24*3600)
      valor_locacao = duracao_modalidade * 25 * cliente.quantidade
    elif cliente.modalidade == "semana":
      duracao_modalidade = duracao/(7*24*3600)
      valor_locacao = duracao_modalidade * 100 * cliente.quantidade

    if cliente.quantidade >= 3:
      valor_locacao = 0.7 * valor_locacao

    return valor_locacao

import random
import datetime as dt


_HORA = "hora"
_DIA = "dia"
_SEMANA = "semana"
_MODALIDADES = {_HORA:3600, _DIA:24*3600, _SEMANA:7*24*3600}
_ABERTA = "aberta"
_FECHADA = "fechada"


class Locacao(object):

  def __init__(self, cliente, loja, quantidade, modalidade):
    self._id =  random.randint(1,999999) #simulando a geraçao de id único para locação
    self.cliente = cliente
    self.loja = loja
    self.quantidade = quantidade
    self._dh_inicio = dt.datetime.now()
    self._dh_fim = None
    self._duracao_locacao = 0
    self._valor_locacao = 0
    self._status = None

    if type(quantidade) != int:
      raise ValueError(f'Erro | Classe Locacao | Metodo Construtor | parametro quantidade inválido. Tipo {type(quantidade)}')
    if quantidade <= 0:
      raise ValueError(f'Erro | Classe Locacao | Metodo Construtor | quantidade igual a 0 ou negativa. Quantidade solicitada {quantidade}')


    if modalidade not in _MODALIDADES:
      raise ValueError(f"Erro | Classe Locacao | Metodo Construtor | Modalidade Inválida")
    else:
      self.modalidade = modalidade
      self._base_locacao = _MODALIDADES.get(modalidade)
    print(f"Classe Locação | Método Construtor | Cria uma instância de locação \n{self}\n")

  def __repr__(self):
    if self._dh_fim != None:
      return f"[Locacao->Id:{self._id}|Cliente:{self.cliente}|Loja:{self.loja}|Quantidade:{self.quantidade}|Data Inicio:{self._dh_inicio.strftime('%d/%m/%Y %H:%M:%S')}|Data Fim:{self._dh_fim.strftime('%d/%m/%Y %H:%M:%S')}|Valor da Locação:R${self._valor_locacao}|Duração:{round(self._duracao_locacao,2)} {self.modalidade}(s)]"
    else:
       return f"[Locacao->Id:{self._id}|Cliente:{self.cliente}|Loja:{self.loja}|Quantidade:{self.quantidade}|Data Inicio:{self._dh_inicio.strftime('%d/%m/%Y %H:%M:%S')}|Data Fim:Não devolvido|Valor da Locação:R${self._valor_locacao}|Duração: {round(self._duracao_locacao,2)} {self.modalidade}(s)]"


  def calcula_tempo_locacao(self):
    if self._dh_fim == None:
      self._dh_fim = dt.datetime.now()

    duracao_em_segundos = (self._dh_fim - self._dh_inicio).total_seconds()
    self._duracao_locacao = round(duracao_em_segundos / self._base_locacao,2)
    print(f"Classe Locação | Método calcula_tempo_locacao | Calcula o tempo da locação na base escolhida no momento da locação \n{self}\n")


  @property
  def duracao_locacao(self):
    return self._duracao_locacao

  @property
  def dh_fim(self):
    return self._dh_fim

  @property
  def inicio_locacao(self):
    return self._dh_inicio

  @dh_fim.setter
  def fim_locacao(self, dh_fim_locacao):
    self._dh_fim = dh_fim_locacao

  @property
  def valor_locacao(self):
    return self._valor_locacao

  @valor_locacao.setter
  def valor_locacao(self, valor):
    self._valor_locacao = valor

  @property
  def status(self):
    return self._status

  def fechar_locacao(self):
    self._status = _FECHADA

  def abrir_locacao(self):
    self._status = _ABERTA

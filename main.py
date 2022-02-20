import datetime as dt
from loja import Loja
from cliente import Cliente

print("\n================================ Instanciando Objetos")
print("\n======Clientes")
cliente1 = Cliente("Rodrigo")
cliente2 = Cliente("Marcos")
cliente3 = Cliente("Caio")
cliente4 = Cliente("Antônio")
cliente5 = Cliente("Cecília")

print("\n======Lojas")
loja1 = Loja("LocBike", 100)
loja2 = Loja("BikeForRent", 50)
loja3 = Loja("IBike", 30)


print("\n======Cliente olha o estoque, aluga e devolve")

cliente1.ler_estoque(loja1)
cliente1.alugar(4, "hora", loja1)
cliente1.hora_aluguel += dt.timedelta(hours=10) #simula a passagem do tempo
valor1 = cliente1.devolver(loja1)
print(f"{cliente1.nome} pagou R$ {valor1} pela locação de {cliente1.quantidade} bicicletas na modalidade {cliente1.modalidade} por um periodo de {cliente1.duracao_locacao} {cliente1.modalidade}(s)\n\n")

cliente2.ler_estoque(loja2)
cliente2.alugar(4, "semana", loja2)
cliente2.hora_aluguel += dt.timedelta(days=14) #simula a passagem do tempo
valor2 = cliente2.devolver(loja2)
print(f"{cliente2.nome} pagou R$ {valor2} pela locação de {cliente2.quantidade} bicicletas na modalidade {cliente2.modalidade} por um periodo de {cliente2.duracao_locacao} {cliente2.modalidade}(s)\n\n")

print("\n================================ Testando Exceções")

print("\n======Lendo o estoque de um objeto diferente de loja")
try:
  cliente4.ler_estoque("loja")
except ValueError as e:
  print(e)

print("\n======Locação além do estoque da loja")
try:
  cliente4.alugar(200, "dia", loja3)
except Exception as e:
  print(e)

print("\n======Locação com modalidade inválida")
try:
  cliente5.alugar(20, "meses", loja2)
except Exception as ve:
  print(ve)

print("\n======Locação com quantidade invalida")
try:
  cliente5.alugar(-10, "dia", loja1)
except Exception as e:
  print(e)


print("\n======Um cliente tentando locar em uma loja sem devolver na loja onde alugou antes")
try:
  cliente4.alugar(1, "dia", loja3)
  cliente4.alugar(1, "hora", loja1)
except Exception as e:
  print(e)

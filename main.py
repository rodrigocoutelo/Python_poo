import datetime as dt
from cliente import Cliente
from locacao import Locacao
from loja import Loja


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


print("\n================================ Operação Simples")
print("\n======Cliente olha o estoque, aluga e devolve")

cliente1.ler_estoque(loja1)
locacao1 = cliente1.alugar(4, "hora", loja1)
locacao1.fim_locacao = locacao1.inicio_locacao + dt.timedelta(hours=10) #simula a passagem do tempo
valor1 = cliente1.devolver(locacao1)
print(f"{cliente1.nome} pagou R$ {valor1} pela locação de {locacao1.quantidade} bicicletas na modalidade {locacao1.modalidade} por um periodo de {locacao1.duracao_locacao} {locacao1.modalidade}(s)")


print("\n================================ Operação mais complexa")
print("\n======Cliente faz vários alugueis diferentes na mesma loja antes mesmo de devolver")
cliente2.ler_estoque(loja1)
locacao12 = cliente2.alugar(4, "hora", loja2)
locacao22 = cliente2.alugar(2, "dia", loja2)
locacao32 = cliente2.alugar(5, "semana", loja2)
locacao12.fim_locacao = locacao12.inicio_locacao + dt.timedelta(hours=30) #simula a passagem do tempo
locacao22.fim_locacao = locacao22.inicio_locacao + dt.timedelta(days=5) #simula a passagem do tempo
locacao32.fim_locacao = locacao32.inicio_locacao + dt.timedelta(days=15) #simula a passagem do tempo
valor22 = cliente2.devolver(locacao22)
valor32 = cliente2.devolver(locacao32)
valor12 = cliente2.devolver(locacao12)
print(f"{cliente2.nome} pagou R$ {valor12} pela locação de {locacao12.quantidade} bicicletas na modalidade {locacao12.modalidade} por um periodo de {locacao12.duracao_locacao} {locacao12.modalidade}(s)")
print(f"{cliente2.nome} pagou R$ {valor22} pela locação de {locacao22.quantidade} bicicletas na modalidade {locacao22.modalidade} por um periodo de {locacao22.duracao_locacao} {locacao22.modalidade}(s)")
print(f"{cliente2.nome} pagou R$ {valor32} pela locação de {locacao32.quantidade} bicicletas na modalidade {locacao32.modalidade} por um periodo de {locacao32.duracao_locacao} {locacao32.modalidade}(s)")

cliente3.ler_estoque(loja1)
locacao13 = cliente3.alugar(8, "semana", loja3)
locacao23 = cliente3.alugar(5, "hora", loja3)
locacao13.fim_locacao = locacao13.inicio_locacao + dt.timedelta(days=21) #simula a passagem do tempo
locacao23.fim_locacao = locacao23.inicio_locacao + dt.timedelta(hours=20) #simula a passagem do tempo
valor23 = cliente3.devolver(locacao23)
valor13 = cliente3.devolver(locacao13)
print(f"{cliente3.nome} pagou R$ {valor13} pela locação de {locacao13.quantidade} bicicletas na modalidade {locacao13.modalidade} por um periodo de {locacao13.duracao_locacao} {locacao13.modalidade}(s)")
print(f"{cliente3.nome} pagou R$ {valor23} pela locação de {locacao23.quantidade} bicicletas na modalidade {locacao23.modalidade} por um periodo de {locacao23.duracao_locacao} {locacao23.modalidade}(s)")


print("\n================================ Testando Exceções")

print("\n======Lendo o estoque de um objeto diferente de loja")
try:
  cliente4.ler_estoque("loja")
except ValueError as e:
  print(e)

print("\n======Locação além do estoque da loja")
try:
  locacao_alem_do_estoque=cliente4.alugar(200, "dia", loja3)
except Exception as e:
  print(e)

print("\n======Locação com modalidade inválida")
try:
  locacao_modalidade_invalida = cliente5.alugar(20, "meses", loja2)
except ValueError as ve:
  print(ve)

print("\n======Locação com quantidade invalida")
try:
  locacao_alem_do_estoque=cliente5.alugar(-10, "dia", loja1)
except Exception as e:
  print(e)



print("\n======Devolvendo um obejto locação que não foi iniciado pelo cliente com metodo alugar")
locacao_falsa = Locacao(cliente4, loja3, 1, "dia")
try:
  cliente4.devolver(locacao_falsa)
except Exception as e:
  print(e)


print("\n======Um cliente devolvendo a locação feita por outro cliente")
locacao_cliente2= Locacao(cliente2, loja2, 1, "dia")
try:
  cliente4.devolver(locacao_cliente2)
except Exception as e:
  print(e)

print("\n======Um cliente devolvendo a locação já encerrada")
try:
  cliente1.devolver(locacao1)
except Exception as e:
  print(e)


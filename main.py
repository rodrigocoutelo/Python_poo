import datetime as dt
from cliente import Cliente
from loja import Loja

rodrigo = Cliente("Rodrigo")
loja = Loja("LocBike", 100)
loja2 = Loja("BikeLok", 20)

rodrigo.olhar_estoque(loja)
rodrigo.alugar(4, "hora", loja)
rodrigo.olhar_estoque(loja)
rodrigo.alugar(1, "hora", loja)
rodrigo.olhar_estoque(loja)
rodrigo.hora_aluguel += dt.timedelta(hours=10) #simula a passagem do tempo
rodrigo.delvover(loja)
rodrigo.olhar_estoque(loja)

try:
  rodrigo.olhar_estoque(loja2)
  rodrigo.alugar(21, "hora", loja2)
except Exception as e:
  print(e)


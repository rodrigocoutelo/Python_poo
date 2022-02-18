import datetime as dt
from cliente import Cliente
from loja import Loja

pessoa1 = Cliente("Rodrigo")
pessoa2 = Cliente("Maria")
pessoa3 = Cliente("João")
loja1 = Loja("LocBike", 100)
loja2 = Loja("BikeLoc", 50)
loja3 = Loja("RentABike", 10)

pessoa1.olhar_estoque(loja1)
pessoa1.olhar_estoque(loja2)
pessoa1.olhar_estoque(loja3)


locacao1 = pessoa1.alugar(4, "hora", loja1)
locacao2 = pessoa1.alugar(1, "dia", loja1)
locacao3 = pessoa2.alugar(5, "semana", loja2)
locacao5 = pessoa3.alugar(4, "hora", loja3)
locacao6 = pessoa2.alugar(2, "semana", loja3)
locacao4 = pessoa3.alugar(5, "dia", loja2)

pessoa1.olhar_estoque(loja1)
pessoa1.olhar_estoque(loja2)
pessoa1.olhar_estoque(loja3)

#simula a passagem do tempo
locacao1.fim = locacao1.inicio + dt.timedelta(hours=10)
locacao2.fim = locacao2.inicio + dt.timedelta(days=3)
locacao3.fim = locacao3.inicio + dt.timedelta(days=14)
locacao4.fim = locacao4.inicio + dt.timedelta(days=8)
locacao5.fim = locacao5.inicio + dt.timedelta(hours=9)
locacao6.fim = locacao6.inicio + dt.timedelta(days=4)

pessoa1.delvover(locacao1)
pessoa1.delvover(locacao2)
pessoa2.delvover(locacao1)
pessoa2.delvover(locacao6)
pessoa3.delvover(locacao4)
pessoa3.delvover(locacao5)

pessoa1.olhar_estoque(loja1)
pessoa1.olhar_estoque(loja2)
pessoa1.olhar_estoque(loja3)

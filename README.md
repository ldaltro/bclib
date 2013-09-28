bclib
=====

Biblioteca python para conversão entre dolar real.A biblioteca ultiliza a taxa de venda de dolares atualizada diariamente pelo Banco central.
```python
import bclib

real = float(raw_input("Digite a quantidade em reais:"))
dolar = real/bclib.getTaxa()
print "R$",real,"=","$","%.2f" % dolar
```

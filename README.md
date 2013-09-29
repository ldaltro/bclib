bclib
=====

Biblioteca python para conversão entre dolar real.A biblioteca ultiliza a taxa de venda de dolares atualizada diariamente pelo Banco Central.
```python
import bclib

real = float(raw_input("Digite a quantidade em reais:"))
dolar = real/bclib.getTaxa()
print "R$",real,"=","$","%.2f" % dolar
```
Atenção!!!
=====
Este script só vai rodar se a lib Beautiful Soup estiver instalada no seu computador
Para instalar a Beautiful Soup no Debian use:

```
sudo apt-get install python-bs4

```
Mais informações sobre a instalação podem ser vistas em:
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

Copyright
=====
Este programa está protegido pela licença beer ware revision 42.

A LICENÇA BEER-WARE ou A LICENÇA DA CERVEJA" (Revisão 42 - Tradução Portugués Brasil 1):

Lucas Daltro <lucasdaltro5@gmail.com> escreveu este arquivo. Enquanto você retiver esta nota você
poderá fazer o que quiser com esta coisa. Caso nos encontremos algum dia e você ache
que esta coisa vale, você poderá me comprar uma cerveja em retribuição, Lucas Daltro.

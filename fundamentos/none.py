"""
None = Não valor
is e is not = é oou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print ("Execute")
else:
    print ("Não execute")

print (passou_no_if, passou_no_if is None)
print (passou_no_if, passou_no_if is not None)

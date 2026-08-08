"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Mark Alves'
outra_variavel = f'{string[:3]}ABC{string[4:]}'

#string = 'ABC'
print(outra_variavel)
print (string.zfill(100))

# Não funciona pq é tipo string imutável
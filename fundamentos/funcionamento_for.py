"""
iterável -> str, range, etc | tem método (___iter__) dentro dele .método é uma ação que se chama dentro do objeto. ex: lower.() | tudo é um objeto.
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
"""
texto = 'Luiz'.__iter__()
print(texto)
"""

texto = iter('Luiz') #__iter__
print (texto)
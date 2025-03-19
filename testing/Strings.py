# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# -------------------------------------------------------

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio'not in produtos)

# -----------------------------------------------------

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)

# ---------------------------------------------------------------

# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste.title())

# ---------------------------------------------------------------

# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)

# frase = '     ômega 3 é bom para a sáude!     '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# ------------------------------------------------------------------

# fruta = 'abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20, "-"))
# print(fruta.center(20, "-"))

# ---------------------------------------------------------------

# p = 'Bóson Treinamentos'
# print(p.startswith('B'))
# print(p.endswith('o'))

# --------------------------------------------------------------
# Docstrings
texto = """
Docstring é um espécie de documentação
que podemos inserir dentro de um módulos, função
ou classe no python, entre outros locais.
    Respeita o deslocamento do texto e é multilinhas

"""
print(texto)

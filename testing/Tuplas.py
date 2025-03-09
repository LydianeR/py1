halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5, 2, 4, 5, 6, 7, 6, 8, 9)
print(sum(t1))

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

print(sorted(alcalinos))

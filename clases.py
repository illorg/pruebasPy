class persona():
    specie = 'humano'


print(persona.specie)
persona.viva = True
hombre = persona()
print(hombre.specie, hombre.viva)

persona.viva = False
print(hombre.viva)

hombre.nombre = 'Darth'
hombre.apellido = 'Vader'

print(hombre.nombre, hombre.apellido)
print(hombre.specie, hombre.viva, hombre.nombre, hombre.apellido)

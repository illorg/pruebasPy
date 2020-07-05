nombres = ('Rodolfo', 'Juan', 'Jimena', 'Roman')
edades = (40, 25, 32, 24)
convinado = list(zip(nombres, edades))
print(convinado)

# equivalent, but using list comprehensions
sq2 = [n ** 2 for n in range(10) if not n % 2]
print(sq2)
# prints: [0, 4, 16, 36, 64] True


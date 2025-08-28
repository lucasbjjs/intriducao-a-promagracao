maior = 0
menor = 10
aprovados = 0
reprovados = 0
for i in range(1, 11):
    print(f"\naluno {i}:")
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
media = (n1 + n2 + n3)
print(f"media = {media:.2f}") 
#verifica maior e menor media
if media > maior :
    maior = media
if media < menor :
#contagem de aprovados e reprovados
    aprovados += 1
else:
    reprovados += 1
print("\n--- resultados ---")
print(f"maior media: {maior:.2f}")
print(f"menor media: {menor:.2f}")
print(f"aprovados: {reprovados}")
print(f"reprovados: {reprovados}")
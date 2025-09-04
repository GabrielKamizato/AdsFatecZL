print('-'*50)
x = input("Digite o valor de x: ")
y = input("Digite o valor de y: ")

print(f"Antes da troca: x = {x}, y = {y}")

x, y = y, x

print(f"Depois da troca: x = {x}, y = {y}")
print('-'*50)
print('Cálculo equação 2° grau')

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))


if a == 0:
    print("Isso não é uma equação do 2º grau (A não pode ser zero).")
else:

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        # Calcular as raízes
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)

        print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
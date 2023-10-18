salario = float(input("Insira o valor do salário aqui: "))
if salario > 1250 :
    aumento10 = (salario * 10) /100
    salariocaumento = salario + aumento10
    print(f"Seu salario, que era de R${salario}, recebeu um aumento de R${aumento10} e passará a ser R${salariocaumento}.")
elif salario == 1250 :
    aumento15_2 = (salario * 15) /100
    salariocaumento_2 = salario + aumento15_2
    print(f"Seu salario, que era de R${salario}, recebeu um aumento de R${aumento15_2} e passará a ser R${salariocaumento_2}.")
else :
    aumento15_3 = (salario * 15) /100
    salariocaumento_3 = salario + aumento15_3
    print(f"Seu salario, que era de R${salario}, recebeu um aumento de R${aumento15_3} e passará a ser R${salariocaumento_3}.")
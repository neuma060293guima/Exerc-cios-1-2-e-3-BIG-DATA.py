#Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.


# Vamos criar uma função que recebe o peso total dos peixes como entrada e calcula a multa, se o peso exceder 100 quilos. A multa será aplicada somente quando o peso total dos peixes ultrapassar esse limite. Vamos assumir que, por exemplo, a multa seja de R$ 10 por quilo acima do limite de 100 quilos.


def calcular_multa(peso_peixes):
    limite = 100  # Limite máximo de peso permitido
    valor_multa_por_quilo = 10  # Valor da multa por quilo acima do limite

    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * valor_multa_por_quilo
        return f"O pescador deverá pagar uma multa de R$ {multa:.2f}."
    else:
        return "O pescador não precisará pagar multa."

# Exemplo de uso
peso_total = float(input("Digite o peso total dos peixes (em quilos): "))
print(calcular_multa(peso_total))#
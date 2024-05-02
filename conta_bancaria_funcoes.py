def depositar(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito de {valor}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo or valor > limite:
        return saldo, extrato, numero_saques, "Operação falhou! Saldo insuficiente ou valor de saque excede o limite."
    
    if numero_saques >= limite_saques:
        return saldo, extrato, numero_saques, "Operação falhou! Limite de saques excedido."
    
    saldo -= valor
    extrato.append(f"Saque de {valor}")
    numero_saques += 1
    return saldo, extrato, numero_saques, f"Saque de {valor} efetuado com sucesso!"

def exibir_extrato(saldo, *, extrato):
    print("Extrato:")
    for transacao in extrato:
        print(transacao)
    print("Saldo atual:", saldo)

def criar_usuario(usuarios):
    nome = input("Nome completo: ")
    cpf = input("CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário já cadastrado com esse CPF.")
        return
    
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso.")

def criar_conta(contas, usuarios):
    agencia = "0001"
    cpf = input("CPF do titular da conta: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado.")
        return
    
    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print("Conta criada com sucesso.")

def main():
    saldo_conta = 2000
    limite = 500
    extrato = []
    limite_saques = 3
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        menu = (
            "[d] Depositar\n"
            "[s] Sacar\n"
            "[e] Extrato\n"
            "[cu] Criar usuário\n"
            "[cc] Criar conta corrente\n"
            "[q] Sair\n"
        )
        opcao = input("Escolha uma das opções do menu: " + menu)

        if opcao == "d":
            valor_deposito = float(input("Qual valor deseja depositar? "))
            saldo_conta, extrato = depositar(saldo_conta, valor_deposito, extrato)
        elif opcao == "s":
            valor_saque = float(input("Qual valor deseja sacar? "))
            saldo_conta, extrato, numero_saques, msg = sacar(
                saldo=saldo_conta,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )
            print(msg)
        elif opcao == "e":
            exibir_extrato(saldo_conta, extrato=extrato)
        elif opcao == "cu":
            criar_usuario(usuarios)
        elif opcao == "cc":
            criar_conta(contas, usuarios)
        elif opcao == "q":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
            
if __name__ == "__main__":
    main()

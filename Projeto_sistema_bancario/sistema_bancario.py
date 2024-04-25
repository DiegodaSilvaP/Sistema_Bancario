menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

=> """

Saque = 0
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        Deposito = float(input("Digite o valor do seu deposito:! "))
        
        if Deposito > 0:
            saldo += Deposito
            extrato += f"Depósito: R$: {Deposito:.2f}\n"
            print (f"Você depositou R$: {Deposito:.2f}")
            
        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "s":
        Saque = float(input("Digite o valor para saque! R$: "))
        
        if numero_saque >= LIMITE_SAQUES:
            print ("Você já efetuou a quantidade maxima de Saques!")
            continue
        
        
        elif Saque > limite:
            print("Excedeu o limite de saque de R$: 500,00")
            continue
        
        elif Saque <= 0:
            print("Valor invalido...!")
            
        elif Saque > 0:
        
            saldo > Saque
            saldo -= Saque
            extrato += f"Saque: {Saque:.2f}\n"
            numero_saque += 1
                    
            print("Aguarde um estante Contando notas...")
            
        else: 
            print("Saldo insuficiente!")
            
        
    elif opcao == "e":
        print("Não foram realizados movimento." if not extrato else extrato)
        print(f"\nSaldo: R$: {saldo:.2f}")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")        
        
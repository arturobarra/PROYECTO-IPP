from calculadora import create_account,add_transaction,get_account_balance,get_total_balance

def main():
    #create_account
    account = []
    while True:

        print("1. crear cuenta")
        print("2. agregar transaccion")
        print("3. consultal saldo de cuenta")
        print("4. consultar saldo total")
        print("5. salir")


        option = int(input("\ningrese una opcion: "))

        if option == 1:
            name = input("ingrese el nombre de la cuenta: ")
            account_type = input("ingrese el tipo de cuenta ingreso/egreso): ")     

            account_id = create_account(account, name, account_type) 

            print(f"\ncuenta creada con exito. ID de cuenta: {account_id}\n")    

        elif option == 2:
            account_id = int(input("ingrese el ID de la cuenta: "))
            description = input("ingrese la descripcion de la transaccion: ")
            amount = float(input("ingresa el monto de la transaccion: "))
            
            add_transaction(account, account_id, description, amount)

            print("\ntransaccion agregada con exito\n")
        
        elif option == 3:
            account_id = int(input("ingrese el ID de la cuenta: "))
            balance = get_account_balance(account, account_id)

            print(f"\nEl saldo de la cuenta es: {balance}\n")
        
        elif option == 4:
            balance = get_total_balance(account)
            print(f"\nEl saldo total de todas las cuentas es: {balance}\n")
        
        elif option == 5:
            print("\nGracias por usar el programa\n")
            break
        
        else:
            print("\nOpcion invalida\n")
if __name__ == "__main__":
    main()
















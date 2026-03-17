import sys


def remove_non_digits(cpf: str) -> str:
    return ''.join(filter(str.isdigit, cpf))


def validate_cpf(cpf: str) -> bool:
   
    cpf = remove_non_digits(cpf)
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    
    remainder = total % 11
    first_check = 0 if remainder < 2 else 11 - remainder
    
    if int(cpf[9]) != first_check:
        return False
    
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    
    remainder = total % 11
    second_check = 0 if remainder < 2 else 11 - remainder
    
    if int(cpf[10]) != second_check:
        return False
    
    return True


def format_cpf(cpf: str) -> str:
    cpf = remove_non_digits(cpf)
    if len(cpf) != 11:
        return cpf
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def main():
    print("=" * 50)
    print("       Validação automática de CPF")
    print("=" * 50)
    print()
    
    cpf_input = input("Digite um número de CPF: ").strip()
    
    if not cpf_input:
        print("\nError: No CPF provided!")
        sys.exit(1)
    
    formatted = format_cpf(cpf_input)
    print(f"\nCPF digitado: {formatted}")
    
    is_valid = validate_cpf(cpf_input)
    
    print("-" * 50)
    if is_valid:
        print("✅ RESULTADO: CPF é VÁLIDO")
    else:
        print("❌ RESULTADO: CPF é INVÁLIDO")
    print("-" * 50)


if __name__ == "__main__":
    main()


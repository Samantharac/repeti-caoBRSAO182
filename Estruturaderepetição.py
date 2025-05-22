
def coletar_notas():
    notas = []

    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()
        
        if entrada == "fim":
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número ou 'fim'.")

    return notas

def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    return 0

# Execução do programa
notas_turma = coletar_notas()
media_turma = calcular_media(notas_turma)

print(f"\nMédia da turma: {media_turma:.2f}")
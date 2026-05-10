from colorama import Fore, Style

niveis = [
    "Muito baixo",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    
def exibir_status(nivel):
    if 1 <= nivel <= 5:
        cor = definir_cor(nivel)
        mensagem = niveis[nivel - 1]
        print(cor + f"Nível {nivel}: {mensagem}" + Style.RESET_ALL)

    
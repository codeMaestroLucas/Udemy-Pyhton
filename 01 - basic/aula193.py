from typing import List
from time import sleep
import os

def main() -> None:
    print("="*60)
    print(f"{'DIGITE O COMANDO OU TAREFA':^60}")
    print("="*60)
    
    lista_de_tarefas: List[str] = []
    lista_desfazer: List[str] = []
    
    comandos: List[str] = ['Adicionar tarefa', 'Desfazer tarefa','Refazer tarefa', 'Limpar terminal', 'Sair']
    
    while True:
        print("Comandos:", sep="\n")
        for c, comando in enumerate(comandos):
            print(f"\033[1;33m{c + 1}\033[m - {comando}")

        resposta = str(input('>> ').strip())
        
        if resposta == '1':
            tarefa: str = input('Tarefa: ').strip().title()
            lista_de_tarefas = add_tarefa(tarefa, lista_de_tarefas)
        
        elif resposta == '2':
            lista_de_tarefas, lista_desfazer = desfazer(lista_de_tarefas, lista_desfazer)

        elif resposta == '3':
            lista_de_tarefas, lista_desfazer = refazer(lista_de_tarefas, lista_desfazer)
        
        elif resposta == '4':
            os.system('cls')
        
        elif resposta == '5':
            print("Saindo...")
            sleep(1)
            break

        else:
            print(f"\033[1;31mComando inválido!\033[m")
            continue
    
    salvar_log(lista_de_tarefas)

def mostrar_tarefas(lista: List[str]) -> None:
    """Print formatado de todas as tarefas solicitadas.

    Args:
        lista (List[str]): Lista de tarefas que vai ser mostrada.
    """
    print('\n', '-'*40)
    print(f"{'TAREFAS':^40}")
    print('-'*40)
    
    for c, tarefa in enumerate(lista):
        print(f'{c + 1:>3}) {tarefa}')
    
    print('-'*40)
    
def add_tarefa(tarefa: str, lista: List[str]) -> List[str]:
    """Função usada para adicionar tarefas à lista de tarefas.

    Args:
        tarefa (str): tarefa que será adicionada
        lista (List[str], optional): Lista que contém todas as tarefas enviadas pelo usuário.
            Defaults to None.

    Returns:
        List: Retorna a lista criada com as tarefas inseridas.
    """
    lista.append(tarefa)
    
    print(f"\033[1;32mTarefa adicionada com sucesso!\033[m")
    mostrar_tarefas(lista)
    
    return lista
    
def desfazer(lista: List[str], lista_desfazer: List[str]) -> List[str]:
    """Função usada para remover a última tarefa da lista.

    Args:
        lista (List[str]): Lista que contém todas as tarefas enviadas pelo usuário.
        lista_desfazer (List[str]): Lista que contém todas as tarefas que foram removidas.

    Returns:
        List[str]: Retorna a lista com a última tarefa removida e a lista de Refazer com a tarefa removida adicionada.
        Se a Lista de Tarefas estiver vazia então nada acontecerá e as listas inalteradas serão retornadas.
    """
    if len(lista) == 0:
        print("\033[1;31mNão há tarefas para desfazer!\033[m")
        return lista, lista_desfazer
    
    lista_desfazer.append(lista.pop())
    
    print(f"\033[1;32mTarefa removida com sucesso!\033[m")
    mostrar_tarefas(lista)
    
    return lista, lista_desfazer

def refazer(lista: List[str], lista_desfazer: List[str]) -> List[str]:
    """Função usada para refazer tarefas para a lista principal de tarefas.

    Args:
        lista (List[str]): Lista de tarefas enviadas pelo usuário.
        lista_desfazer (List[str]): Lista de tarefas que foram removidas.

    Returns:
        List[str]: Retorna as listas alteradas.
            Se a Lista Desfazer estiver vazia, então nada será alterado.
    """
    if len(lista_desfazer) == 0:
        print("\033[1;31mNão há tarefas para refazer!\033[m")
        return lista, lista_desfazer
    
    lista.append(lista_desfazer.pop())
    
    print(f"\033[1;32mTarefa refeita com sucesso!\033[m")
    mostrar_tarefas(lista)
    
    return lista, lista_desfazer

def salvar_log(lista: List[str]) -> None:
    """Função usada para salvar a lista de tarefas em um arquivo ao final do processo.
        Será chamada após o término da main()

    Args:
        lista (List[str]): lista de tarefas do usuário
    """
    with open('log.txt', 'w', encoding='utf8') as arquivo:
        for c, tarefa in enumerate(lista):
            arquivo.write(f'{c + 1}){tarefa}\n')
            
def ler_log() -> None:
    """Função usada para ler o arquivo de log.
    """
    with open('log.txt', 'r', encoding='utf8') as arquivo:
        print(arquivo.read())
    
if __name__ == "__main__":
    main()
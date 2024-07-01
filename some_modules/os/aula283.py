# LISTDIR -> Get a list of files/folders in a directory
def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    import math

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

def main() -> None:
    """Function used to run the main code."""
    import os
    
    files = os.listdir('.')
    print(files, '\n\n', type(files)) # Returns a list of the files
    for file in files:
        print(f'FILE: {file}, EXTENSION: {os.path.splitext(file)}')

        print(f'SIZE: {os.path.getsize(file)}') # This function isnt too good,
        # in the StackOverFlow they made some changes to make it better.
        print(f'SIZE: {formata_tamanho(os.path.getsize(file))}', end='\n'*2)


if __name__ == '__main__':
    main()
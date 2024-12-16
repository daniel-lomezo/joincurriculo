"""
    execute shell commands

    exec(open('src/shell.py').read())
"""
from casamento.models import ListaCasamento


# função para importar csv para o banco de dados

def import_csv_to_db():
    # printar comando e rodar pwd pelo python
    import os
    print(os.getcwd())
    # importar csv
    import csv
    # abrir arquivo csv
    with open('import.csv', 'r') as file:
        # ler arquivo csv
        reader = csv.reader(file)
        # pular cabeçalho
        next(reader)
        print(reader)
        # loop para inserir dados no banco de dados
        for row in reader:
            print(row)
            if row[2] == '-':
                row[2] = None
            if row[5] == '':
                row[5] = None
            if row[6] == '-':
                row[6] = None
            _, created = ListaCasamento.objects.get_or_create(
                nome_item=row[0],
                medida_item=row[1],
                preferencia_cor=row[2],
                tipo_lista="Lista chá de panela",
                item_ja_escolhido=False,
                codigo_seguranca=row[5],
                quem_escolheu=row[6]
            )





import_csv_to_db()
"""
    execute shell commands

    exec(open('src/shell.py').read())
"""
from casamento.models import ListaCasamento


# função para importar csv para o banco de dados

def import_csv_to_db():
    # printar comando e rodar pwd pelo python
    list = ListaCasamento.objects.all().update(item_ja_escolhido=True)





import_csv_to_db()
import os
import re

# Obtém o diretório atual
diretorio = os.getcwd()

# Padrão para encontrar arquivos com índice de repetição no formato " (1)", " (2)", etc.
padrao = re.compile(r" \(\d+\)(\.\w+)$")

# Lista todos os arquivos no diretório
for arquivo in os.listdir(diretorio):
    caminho_atual = os.path.join(diretorio, arquivo)
    
    # Verifica se é um arquivo e se tem uma extensão de imagem
    if os.path.isfile(caminho_atual) and arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
        novo_nome = padrao.sub(r"\1", arquivo)  # Remove o índice de repetição
        
        # Caminho do novo arquivo
        novo_caminho = os.path.join(diretorio, novo_nome)
        
        # Evita sobrescrever um arquivo existente
        if not os.path.exists(novo_caminho):
            os.rename(caminho_atual, novo_caminho)
            print(f'Renomeado: {arquivo} -> {novo_nome}')
        else:
            print(f'Skipped (já existe): {arquivo}')

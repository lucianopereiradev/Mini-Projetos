# Utilitários de renomeação e criação

Dois scripts Python simples:

* `rename_files.py` - renomeia todos os arquivos de uma pasta com um padrão.
* `create_files.py` - cria arquivos .txt com nomes curtos e aleatórios.

### Como usar

Abra um terminal na pasta e execute um dos comandos.

**Renomear arquivos:**
```
python rename_files.py <pasta> <padrão>
```
Exemplo pré-definido (pre):
```
python rename_files.py ./Renomear documento1
```
Isso vai renomear os arquivos na pasta `Renomear` como `documento1`,
`documento2`, etc.

**Criar arquivos aleatórios:**
```
python create_files.py <quantidade> [--dir pasta] [--length tamanho]
```
Exemplo simples:
```
python create_files.py 10
```
Cria 10 arquivos .txt com nomes curtos na pasta atual.

Pronto! Os scripts são pequenos e fáceis de mexer se você quiser
depurar ou ajustar algo.
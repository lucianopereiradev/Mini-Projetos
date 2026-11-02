# Mini-Projetos

Pequenos projetos que fiz para praticar programação, cada um focado em um conceito: lógica, manipulação de arquivos, DOM e desenvolvimento de jogos.

| Projeto | Linguagem | O que faz |
| --- | --- | --- |
| [Space InPython](<Mini Projetos/Jogo em python>) | Python · Pygame | Jogo no estilo Space Invaders |
| [Validador de CPF](<Mini Projetos/Validador de CPF>) | Python · HTML/CSS/JS | Valida CPFs pelos dígitos verificadores |
| [To-Do List](<Mini Projetos/To-Do list>) | HTML/CSS/JS | Lista de tarefas salva no navegador |
| [Nomear Tudo](<Mini Projetos/Nomear Tudo>) | Python | Renomeia e cria arquivos em lote |

## Space InPython

Jogo de nave em que você enfrenta ondas de inimigos. A cada fase há mais inimigos, e eles se movem e atiram mais rápido.

- Movimento com `←` `→` e tiro com `Espaço`
- 4 power-ups: tiro extra, velocidade, escudo e vida extra
- Pontuação multiplicada pela fase atual

```bash
cd "Mini Projetos/Jogo em python"
pip install pygame
python jogo.py
```

## Validador de CPF

Confere se um CPF é válido calculando os dois dígitos verificadores e rejeitando sequências repetidas (como `111.111.111-11`). Tem duas versões com a mesma lógica:

- **Web:** abra `index.html` no navegador. O campo aplica a máscara enquanto você digita.
- **Terminal:** `python cpf.py`

## To-Do List

Lista de tarefas em JavaScript puro: adicionar, concluir, excluir e limpar tudo, com contador de tarefas. Elas ficam salvas no `localStorage`, então continuam lá ao recarregar a página. Para usar, abra `index.html` no navegador.

## Nomear Tudo

Dois scripts para tarefas repetitivas com arquivos:

```bash
python rename_files.py <pasta> <padrão>   # documento1, documento2, ...
python create_files.py <quantidade>       # cria arquivos .txt de teste
```

Mais detalhes no [README do projeto](<Mini Projetos/Nomear Tudo/README.md>).

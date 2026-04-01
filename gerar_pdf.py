from pathlib import Path

input_file = "Todos os Baralhos.txt"
output_file = "deck.html"

cards = []

with open(input_file, "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.rstrip("\n")

        # Ignora metadados do Anki
        if not linha or linha.startswith("#"):
            continue

        partes = linha.split("\t")

        # Seu arquivo tem: pergunta, resposta, tags
        if len(partes) < 2:
            continue

        pergunta = partes[0].strip()
        resposta = partes[1].strip()

        cards.append((pergunta, resposta))

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Deck Anki</title>
  <style>
    * {{
      box-sizing: border-box;
    }}

    body {{
      font-family: Arial, sans-serif;
      margin: 32px;
      color: #111;
      line-height: 1.5;
    }}

    h1 {{
      margin-bottom: 24px;
      font-size: 28px;
    }}

    .card {{
      page-break-inside: avoid;
      border: 1px solid #d0d0d0;
      border-radius: 10px;
      padding: 18px;
      margin-bottom: 18px;
    }}

    .label {{
      font-size: 12px;
      font-weight: bold;
      text-transform: uppercase;
      color: #666;
      margin-bottom: 6px;
    }}

    .pergunta {{
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 14px;
    }}

    .resposta {{
      font-size: 15px;
    }}

    .resposta img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin-top: 8px;
    }}
  </style>
</head>
<body>
  <h1>Deck exportado do Anki</h1>
"""

for i, (pergunta, resposta) in enumerate(cards, start=1):
    html_content += f"""
  <div class="card">
    <div class="label">Pergunta {i}</div>
    <div class="pergunta">{pergunta}</div>
    <div class="label">Resposta</div>
    <div class="resposta">{resposta}</div>
  </div>
"""

html_content += """
</body>
</html>
"""

Path(output_file).write_text(html_content, encoding="utf-8")

print(f"HTML gerado com sucesso: {output_file}")
print(f"Total de cards convertidos: {len(cards)}")
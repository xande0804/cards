import json
from pathlib import Path

FILE_PATH = "cards.json"


def carregar_cards():
    if not Path(FILE_PATH).exists():
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Erro: cards.json está inválido.")
            return []


def salvar_cards(cards):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)


def main():
    cards = carregar_cards()

    print(f"\n📦 Cards atuais: {len(cards)}\n")

    contador = 1

    while True:
        print(f"\n--- NOVO CARD #{len(cards) + 1} ---")

        pergunta = input("Pergunta: ").strip()
        resposta = input("Resposta: ").strip()

        if not pergunta or not resposta:
            print("⚠️ Pergunta e resposta não podem ser vazias.")
            continue

        cards.append({
            "question": pergunta,
            "answer": resposta
        })

        print("✅ Card adicionado!")

        opcao = input("\n1 - Adicionar outro\n2 - Salvar e sair\nEscolha: ").strip()

        if opcao == "2":
            break

    salvar_cards(cards)

    print(f"\n💾 {len(cards)} cards salvos com sucesso em {FILE_PATH}!")


if __name__ == "__main__":
    main()
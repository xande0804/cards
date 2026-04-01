const flashcardEl = document.getElementById("flashcard");
const questionEl = document.getElementById("question");
const answerEl = document.getElementById("answer");
const counterEl = document.getElementById("counter");
const toggleBtn = document.getElementById("toggleBtn");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const statusMessageEl = document.getElementById("statusMessage");

let flashcards = [];
let currentIndex = 0;
let isFlipped = false;

function updateFlipState(flipped) {
  isFlipped = flipped;
  flashcardEl.classList.toggle("is-flipped", isFlipped);
  toggleBtn.textContent = isFlipped ? "Ver pergunta" : "Ver resposta";
}

function renderCard() {
  if (!flashcards.length) {
    questionEl.textContent = "Nenhum flashcard encontrado.";
    answerEl.textContent = "Adicione cards no arquivo cards.json.";
    counterEl.textContent = "0 / 0";
    toggleBtn.disabled = true;
    prevBtn.disabled = true;
    nextBtn.disabled = true;
    return;
  }

  const currentCard = flashcards[currentIndex];

  questionEl.innerHTML = currentCard.question;
  answerEl.innerHTML = currentCard.answer;
  counterEl.textContent = `${currentIndex + 1} / ${flashcards.length}`;

  updateFlipState(false);
}

function flipCard() {
  if (!flashcards.length) return;
  updateFlipState(!isFlipped);
}

function goNext() {
  if (!flashcards.length) return;
  currentIndex = (currentIndex + 1) % flashcards.length;
  renderCard();
}

function goPrev() {
  if (!flashcards.length) return;
  currentIndex = (currentIndex - 1 + flashcards.length) % flashcards.length;
  renderCard();
}

async function loadCards() {
  try {
    const response = await fetch("./cards.json", { cache: "no-store" });

    if (!response.ok) {
      throw new Error(`Erro HTTP ${response.status}`);
    }

    const data = await response.json();

    if (!Array.isArray(data)) {
      throw new Error("cards.json não contém um array válido.");
    }

    flashcards = data.filter(
      (item) =>
        item &&
        typeof item.question === "string" &&
        typeof item.answer === "string"
    );

    if (!flashcards.length) {
      throw new Error("Nenhum card válido foi encontrado em cards.json.");
    }

    renderCard();
  } catch (error) {
    console.error(error);
    statusMessageEl.textContent =
      "Erro ao carregar os flashcards. Verifique o cards.json.";
    questionEl.textContent = "Erro ao carregar deck.";
    answerEl.textContent = "Confira o arquivo cards.json.";
    counterEl.textContent = "0 / 0";
    toggleBtn.disabled = true;
    prevBtn.disabled = true;
    nextBtn.disabled = true;
  }
}

toggleBtn.addEventListener("click", flipCard);
nextBtn.addEventListener("click", goNext);
prevBtn.addEventListener("click", goPrev);

flashcardEl.addEventListener("click", flipCard);

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight") {
    goNext();
  }

  if (event.key === "ArrowLeft") {
    goPrev();
  }

  if (event.key === " " || event.key === "Enter") {
    event.preventDefault();
    flipCard();
  }
});

loadCards();
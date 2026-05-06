let cardNum = 0;
const card = document.querySelector(".flip-card");
const cardInner = document.querySelector(".flip-card-inner");
const innerCard = card.querySelector('.flip-card-inner');

function flipCard() {
  // Find 'flip-card-inner' div inside clicked card
  // const innerCard = card.querySelector('.flip-card-inner');
  // Toggle flipped class
  innerCard.classList.toggle('flipped');
}


function isCardFlipped() {
  if (cardInner) {
    if (cardInner.classList.contains(".flipped")) {
      innerCard.classList.toggle('.flipped');
    }
    else {
      console.log("FALSE");
    }
  }
}

function nextCard() {
  updateCardWord();
  if (cardNum != cardData.length - 1) {
    cardNum += 1;
  } 
  else {
      cardNum = 0;
  }
  console.log(cardData[cardNum]['en']);
  console.log(cardData[cardNum]['gr']);

  if(isCardFlipped()) {
    innerCard.classList.toggle('flipped');
  }
}

function prevCard() {
  updateCardWord();
  if (cardNum != 0) {
    cardNum -= 1;
  }
  else {
    cardNum = cardData.length - 1;
  }
  console.log(cardData[cardNum]['en']);
  console.log(cardData[cardNum]['gr']);

  isCardFlipped();
}

function updateCardWord() {
  const frontWord = cardData[cardNum]['en'];
  const backWord = cardData[cardNum]['gr'];

  const frontElement = document.querySelector('.flip-card-front p');
  const backElement = document.querySelector('.flip-card-back p');

  frontElement.textContent = frontWord;
  backElement.textContent = backWord;
}

function iterateCards() {
  console.log(cardData[cardNum]['gr']);
  console.log(cardData[cardNum]['gr']);
}


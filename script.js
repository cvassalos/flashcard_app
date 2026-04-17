function flipCard(card) {
  // Find 'flip-card-inner' div inside clicked card
  const innerCard = card.querySelector('.flip-card-inner');
  // Toggle flipped class
  innerCard.classList.toggle('flipped');
}

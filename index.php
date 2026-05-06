<head>
<html>
  <link rel="stylesheet" href="styles.css">
  <script src="./script.js"></script>
  <?php include "./stack.php" ?>
</head>
<body>
GREEK FLASHCARDS!
<br>
<div class="flip-card" onclick="flipCard(this)">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p><?php echo $english_word ?></p>
    </div>
    <div class="flip-card-back">
      <p><?php echo $greek_word ?></p>
    </div>
  </div>
</div>
<button type="button">Prev Card</button>
<button type="button">Next Card</button>
</body>
</html>


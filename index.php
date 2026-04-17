<head>
<html>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
GREEK FLASHCARDS!
<br>
<?php 
  $english_word = 'the donkey';
  $greek_word = 'το γάιδαρος';
?>
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <p><?php echo $english_word ?></p>
    </div>
    <div class="flip-card-back">
      <p><?php echo $greek_word ?></p>
    </div>
  </div>
</div>
</body>
</html>


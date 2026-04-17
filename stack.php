<html>
<head></head>
<body>
<br>

<?php
$cards = [
  'soccer' => 'ποδόσφαιρο',
  'game' => 'παιχνίδι',
  'ball' => 'μπάλα',
  'film' => 'η ταινία'
];

foreach ($cards as $key => $value) {
  echo "<h2>$key</h2><br>";
  echo "<h2>$value</h2><br>";
  echo "----------------------------------------------";
}
?>
</body>
</html>

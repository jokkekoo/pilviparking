<?php

// php tiedonhakuun tietokannasta.
// Juhanin ehdotuksen mukaan voisi laittaa suoriutumaan, kun painaa markkerista, pitää testata

ini_set('display_errors', 1);
require '../../../../phpdatabase/db.php';

$sql = "SELECT paikat, filenamepath FROM datatable ORDER BY id desc LIMIT 0, 1";

if(!$conn){
	die("Connection failed: " . mysqli_connect_error());
	}

$result = mysqli_query($conn, $sql);

while($row = mysqli_fetch_array($result)){
	echo $row['paikat'] . "|" . $row['filenamepath'];
}


?>

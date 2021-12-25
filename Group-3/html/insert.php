<?php

// Vie ensin kuvan uploads kansioon ja sitten hakee päivitysajan mukaan
// uusimman tiedoston, jonka jälkeen vie tietokantaan tiedostopolun ja paikkojen määrän.

// Kuva pitää olla .png, voidaan muuttaa mutta ei tarvitse jos raspin kuva on png automaattisesti
// Tätä ei käytetä kuvan siirtämiseen, vaan upload.php

// Tähän pitäisi lisätä injektiota vastaan suojausta

 
ini_set('display_errors', 1);
require '../../../../phpdatabase/db.php';

$uploaddir = 'uploads/';
$uploadfile = $uploaddir . basename($_FILES['image']['name']);

// tätä ei käytetä
if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadfile)){
	echo "Tiedosto on oikeanlainen ja siirretty meidän luotettaviin käsiin!\n";
} else {
	echo "Jotain meni pieleen.\n";
}

// hakee uusimman tiedoston kansiosta
$files = glob($uploaddir . "*.png");
usort($files, function($a, $b){
	return (filemtime($a) < filemtime($b));
});
$newest = $files[0];

// vie tiedot tietokantaan

if (isset($_POST['submitted']))
{
	if(!$conn){
	die("Connection failed: " . mysqli_connect_error());
	}
	$paikat = $_POST['paikat'];

	$sql = "INSERT INTO datatable (filenamepath, paikat, pvm) VALUES ('$newest', '$paikat', NOW())";
	if(mysqli_query($conn, $sql)){
		echo "New record created succesfully";
	}
	else{
		echo "Error " . $sql . "Error" . mysqli_error($conn);
	}
}

?>

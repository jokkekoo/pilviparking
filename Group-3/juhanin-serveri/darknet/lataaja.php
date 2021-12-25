<?php

$uploaddir = 'uploads/';
$uploadfile = $uploaddir . basename($_FILES['image']['name']);

echo "<p>";

if (move_uploaded_file($_FILES['image']['tmp_name'], $uploadfile)) {
	echo "File is valid, and was successfully uploaded.\n";
} else {
	echo "Upload failed";
}

$command = escapeshellcmd('python detectthis.py');
$output = shell_exec($command);

echo $output;

echo "</p>";
echo '<pre>';
echo 'Here is some more debugging info:';
print_r($_FILES);
print "</pre>";
?> 

<?php
include "fs.php";

$gizlim = "uU951753Mu";

/////////////////////// login bilgileri //////////////////
$username = $_POST["username"];
$password = $_POST["password"];
$sign = $_POST["signature"];
$islem = $_POST["islem"];

if (sifrele($password.$username.$gizlim) != $sign) {
	echo "Yanlis anahtar";
	exit;
}

$loginbu = false;

if ($username == "" and $password == "") {
	$loginbu = true;
} else if ($username == "" and $password == "") {
	$loginbu = true;
} else {
	echo "not login";
	exit;
}


$fh = fopen("","a+");
if ($islem == "read") {
	$icerik = fread($fh, filesize(''));
	echo $icerik;
} else if ($islem == "write") {
	echo "yazma modu aktif\n";
	$mesaj = "Gonderen: " . $username . " -> " . $_POST["mesaj"] . "\n";
	fwrite($fh,$mesaj);
}
fclose($fh);
?>

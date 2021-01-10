<?php
$zip=new ZipArchive;
if($zip->open('new.zip',ZipArchive::CREATE)===TRUE)
{
	$zip->addFile("1.txt");
	$zip->addFile("2.txt");
	$zip->addFile("3.txt");
	$zip->addFile("4.txt");
	echo 'zip created';
}
	$zip->close();
?>
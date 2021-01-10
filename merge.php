<?php
$lines = file('file1.txt');
$lines2 = file('file2.txt');
foreach ($lines as $key => $val) {
	echo $lines[$key]."\n";
    $lines[$key] = $val.$lines2[$key];
	
}
file_put_contents('output.txt', implode('\n', $lines));
echo 'successfull';
?>
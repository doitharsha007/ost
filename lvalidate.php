<?php
$message="";
if(count($_POST)>0) {
	$conn = mysqli_connect("localhost","root","","db1");
	$result = mysqli_query($conn,"SELECT * FROM user WHERE user_name='" . $_POST["userName"] . "' and password = '". $_POST["password"]."'");
	if(mysqli_num_rows($result)==0) 
		$message = "Invalid Username or Password!";
	else 
$message = "You are successfully authenticated!";
}
?>

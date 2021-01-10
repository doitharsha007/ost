<?php
if(count($_POST)>0) { 
foreach($_POST as $key=>$value) { 
if(empty($_POST[$key])) { 
$message = ucwords($key) . " field is required"; 
break; 
} 
} 
if(!isset($message)) {
if (filter_var($_POST['url'], FILTER_VALIDATE_IP) === false) {
    $message="ip is not a valid IP address";
}
}
if(!isset($message)) {
$email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
if (filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
    $message="email is not a valid email address";
}}
if(!isset($message)) {
if (filter_var($_POST['int'], FILTER_VALIDATE_INT) === false) {
    $message="Integer is not valid";
}}
if(!isset($message))
{
	$message="validation successfull!!!!!";
}
}
?>
<html>
<body>
<form align="center" name="validate" method="post" action="">
<div class="message"><?php if(isset($message)) echo $message; ?></div> 
<label>url</label>
<input type="text" name="url"  value="<?php if(isset($_POST['url'])) echo $_POST['url']; ?>"/>
<br>
<label>email</label>
<input type="text" name="email" value="<?php if(isset($_POST['email'])) echo $_POST['email']; ?>"/>
<br>
<label>int</label>
<input type="text" name="int"  value="<?php if(isset($_POST['int'])) echo $_POST['int']; ?>"/>
<br>
<input type="submit" name="submit" value="Submit">
</form>
</body>
</html>
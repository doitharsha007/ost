<?php
if($_POST)
{
$name = $_POST['name']; 
$email = $_POST['email']; 
$username = $_POST['username']; 
$password = $_POST['password']; 
$gender = $_POST['gender']; 
if (preg_match('/^[A-Za-z0-9 ]{3,20}$/',$name))  // Full Name
{
$valid_name=$name;
}
else
{ 
$error_name='Enter valid Name.'; 
}
if (preg_match('/^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.([a-zA-Z]{2,4})$/', $email))  // Email
{
$valid_email=$email; 
}
else
{ 
$error_email='Enter valid Email.'; 
}
if (preg_match('/^[A-Za-z0-9_]{3,20}$/',$username))  // Usename min 2 char max 20 char
{
$valid_username=$username;
}
else
{ 
$error_username='Enter valid Username min 3 Chars.'; 
}
if (preg_match('/^[A-Za-z0-9!@#$%^&*()_]{6,20}$/',$password)) 
{
$valid_password=$password;
}
else
{ 
$error_password='Enter valid Password min 6 Chars.'; 
}
if ($gender==0)  // Gender
{
$error_gender='Select Gender'; 
}
else
{ 
$valid_gender=$gender;
}
if(!isset($error_name) && !isset($error_email) && !isset($error_username) && !isset($error_password) && !isset($error_gender))
$success="validation successfull!!!";
} ?>

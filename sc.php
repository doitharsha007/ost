<?php
//creating a cookie
SetCookie("username","password",time()+60,"|");
echo"the cookie has been set for 60 sec";
?>
//Retrieving a cookie
<?php print_r($_COOKIE);?>
//Deleting a cookie
<?php SetCookie("username","password",time()-360,'|');?>
//Creating a session
<?php
Session_Start();
if(isset($_SESSION['page_count']))
$_SESSION['page_count']+=1;
else
$_SESSION['pagecount']=1;
echo "you are visitor number ".$_SESSION['page_count'];
?>
//Destroying a cookie
<?php
Session_destroy();
?>

<?php include("lvalidate.php");?>
<form align="center" name="frmUser" method="post" action="">
	<div class="message"><?php if($message!="") { echo $message; } ?></div>
		<table border="0" cellpadding="10" cellspacing="1" width="500" align="center" class="tblLogin">
			<tr class="tableheader" colspan="2">
			<td align="center" >Enter Login Details</td>
			</tr>
			<tr class="tablerow">
			<td>Username</td>
			<td>
			<input type="text" name="userName" placeholder="User Name" class="login-input"></td>  </tr>
			<tr class="tablerow">
			<td>Password</td>
			<td>
			<input type="password" name="password" placeholder="Password" class="login-input">  </td>  </tr>
			<tr class="tableheader">
			<td align="center" colspan="2"><input type="submit" name="submit" value="Submit" class="btnSubmit"></td>
			</tr>
		</table>
</form>

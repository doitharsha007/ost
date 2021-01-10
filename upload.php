
<?php
$msg = ""; 

// If upload button is clicked ... 
if (isset($_POST['upload']))
{ 

	$filename = $_FILES["uploadfile"]["name"]; 
	$tempname = $_FILES["uploadfile"]["tmp_name"];	 
		$folder = "img/".$filename; 
		
	$db = mysqli_connect("localhost", "root", "", "db1"); 

		// Get all the submitted data from the form 
		$sql = "INSERT INTO photos (filename) VALUES ('".$filename."')"; 

		// Execute query 
		mysqli_query($db, $sql); 
		// Now let's move the uploaded image into the folder: image 
		if(move_uploaded_file($tempname,$folder)) 
		{ 
			$msg = "Image moved successfully"; 
			echo $msg;
		}else
		{ 
			$msg = "Failed to move image"; 
			echo $msg;
		} 
} 
//$result = mysqli_query($db, "SELECT * FROM image"); 
?> 
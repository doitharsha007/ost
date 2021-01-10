<?php
$server="localhost";
$usr="root";
$pwd="";
$db="db1";
$conn=mysqli_connect($server,$usr,$pwd,$db);
if(!$conn)
die("connection failed".mysqli_connect_error());
$sql="select * from ost_b";
$res=mysqli_query($conn,$sql);
if(mysqli_num_rows($res)>0)
{
	echo "id   name   course"."<br>";
	while($row = mysqli_fetch_assoc($res))
	{
		echo $row['sno'].' '.$row['name'].' '.$row['course'].'<br>';
	}	
}
else
echo "0 results";
mysqli_close($conn);
?>
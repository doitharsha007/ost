<?php
$conn = mysqli_connect("localhost", "root", "", "db1");
if (!$conn) {
die("Connection failed: " . mysqli_connect_error());
}
$sql = "INSERT INTO students VALUES ('".$_POST["name"]."','".$_POST["rno"]."','".$_POST["branch"]."','".$_POST["age"]."','".$_POST["email"]."','".$_POST["phone"]."')";
if (mysqli_query($conn, $sql)) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
mysqli_close($conn);
?>
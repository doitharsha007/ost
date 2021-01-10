<html>
<head>
<style>
</style>
</head>
<body>

<?php
$q = intval($_GET['q']);

$con = mysqli_connect('localhost','root','','photos');
if (!$con) {
    die('Could not connect: ' . mysqli_error($con));
}

$sql="SELECT * FROM MyGuests WHERE id = '".$q."'";
$result = mysqli_query($con,$sql);

echo "<table>
<tr>
<th>id</th>
<th>Firstname</th>
<th>Lastname</th>
<th>email</th>
<th>date</th>
</tr>";
while($row = mysqli_fetch_array($result,MYSQLI_BOTH)) {
    echo "<tr>";
 echo "<td>" . $row['ID'] . "</td>";
    echo "<td>" . $row['FirstName'] . "</td>";
    echo "<td>" . $row['Lastname'] . "</td>";
    echo "<td>" . $row['Email'] . "</td>";
    echo "<td>" . $row['Date'] . "</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($con);
?>
</body>
</html>
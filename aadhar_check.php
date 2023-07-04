<?php
include 'db.php';
$aadhar=$_POST['aadhar'];

$sql="Select count(*) as found from sample_aadhar where aadhar_no='$aadhar'";



$test= $DB_con->query($sql);

//echo "<pre>"; 

//print_r($test);

while ($row = $test->fetch()) { echo $row['found'];}



?>

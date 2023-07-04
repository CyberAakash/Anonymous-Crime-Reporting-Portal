<?php
include 'db.php';
error_reporting(0);
    $content=file_get_contents('hash.txt');
    echo "<pre>"; print_r($content);

    $detail=file_get_contents('details.txt',false,null,0,12);
    
    $sql = "UPDATE `detail` SET `aadhar_hash`='$content' WHERE `aadhar_no`='$detail'";

//echo $sql;
   // use exec() because no results are returned
$test= $DB_con->exec($sql);

?>



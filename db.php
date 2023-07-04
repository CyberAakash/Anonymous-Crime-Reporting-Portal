<?php
/**$servername = "localhost";
$username = "root";
$password = "";
$dbname = "sih";
$link = new mysqli($servername, $username, $password, $dbname);
if ($link->connect_error) {
die('Connection failed: ' .$link->connect_error);
}else{
//echo "Database Connected successfully"; // in case of success
}**/

$DB_host = "localhost";
$DB_user = "root";
$DB_pass = "";
$DB_name = "sih";

try
{
$DB_con = new PDO("mysql:host={$DB_host};dbname={$DB_name}",$DB_user,$DB_pass);
$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

}
catch(PDOException $e)
{
echo $e->getMessage();
}

?>
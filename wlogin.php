<?php
    extract($_REQUEST);
    $file=fopen("../files/login.txt","w");
    fwrite($file, $aadhaar ."\n");
    fwrite($file, $password ."\n");
    fwrite($file, $role ."\n");
    fclose($file);

    $file1=fopen("../files/loginfront.txt","w");
    fwrite($file1, $aadhaar ."\n");
    fwrite($file1, $password ."\n");
    fwrite($file1, $role ."\n");
    fclose($file1);
    
    shell_exec("python3 blogin.py");
    if ($file = fopen("../files/login.txt", "r"))
    {
        while(!feof($file)) 
        {
            $line = fgets($file);
            if(strcmp($line,"YES\n")==0)
            {
                header("location:index.php");
                break;
            }
        }
        fclose($file);
    }
    else 
    {
        echo "Invalid Aadhaar or Password";
    }
 ?>
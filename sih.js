            function validateForm() {
                var x = document.forms["myForm"]["aadhar"].value;
                var y = document.forms["myForm"]["filename"].value;
                if (x == "" || x == null) {
                    alert("Name must be filled out");
                    return false;
                }
                else if (y == "" || y == null) {
                    alert("File Should be Uploaded");
                    return false;
                }
                else {
                    var regexp=/^[2-9]{1}[0-9]{3}\s{1}[0-9]{4}\s{1}[0-9]{4}$/;

                    if(regexp.test(x)) {
                        window.alert("Valid Aadhar no.");
                        return true;
                    }
                    else{ 
                        window.alert("Invalid Aadhar no.");
                        return False;
                    }
                }
                
            }








            
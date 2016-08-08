<?php
	$mysql_host = "localhost";
	$mysql_database = "self_explanatory_system";
	$mysql_user = "root"
	$mysql_password = "spaceman1236";

	if(mysql_connect($mysql_host,$mysql_user,$mysql_password)){
		print("success connection");
	}

	else{
		print("failed");
	}

	mysql_select_db($mysql_database);

	$cnt = mysql_num_rows(mysql_query("SELECT * FROM data"));
	print "number of rows:".$cnt

	$value =$POST["textarea"];

	if(isset($value) && $cnt == 0){

		$query = "INSERT INTO data VALUES('$value',now(),1)";
		if($result = mysql_query($query)){
			echo("successfully entered")
		}
	}
	else if(isset($value) && $cnt>0){
		
		$query = "UPDATE data SET speak='$value',time= now(),num='1' WHERE num = '1'";
		if($result = mysql_query($query)){
			echo("successfully entered")
		}
	}
	else
	   echo("failed");
?>
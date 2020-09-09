<?php 

	if (!isset($_SESSION)) session_start(); 
	if(!$_POST) exit;
	
	include dirname(__FILE__).'/settings/settings.php';
	include dirname(__FILE__).'/functions/emailValidation.php';	
	
	
	/* Current Date Year
	------------------------------- */		
	$currYear = date("Y");	
	
/*	---------------------------------------------------------------------------
	: Register all form field variables here
	--------------------------------------------------------------------------- */	
	$firstname = strip_tags(trim($_POST["firstname"]));	
	$lastname = strip_tags(trim($_POST["lastname"]));
	$emailaddress = strip_tags(trim($_POST["emailaddress"]));
	$company = strip_tags(trim($_POST["company"]));
	$telephone = strip_tags(trim($_POST["telephone"]));
	$department = strip_tags(trim($_POST["department"]));
	$products = strip_tags(trim($_POST["products"]));
	$support = strip_tags(trim($_POST["support"]));
	$response = strip_tags(trim($_POST["response"]));
	$comment = strip_tags(trim($_POST["comment"]));
	$improve = $_POST["improve"];
	if ($improve[0]!=""){
		$improve_list = implode( '<br/>', $improve);
		$improve_list_csv = implode( '&nbsp; ', $improve);
	}	
	
/*	----------------------------------------------------------------------
	: Prepare form field variables for CSV export
	----------------------------------------------------------------------- */	
	if($generateCSV == true){
		$csvFile = $csvFileName;	
		$csvData = array(
			"$firstname",
			"$lastname",
			"$emailaddress",
			"$company",
			"$telephone",
			"$department",
			"$products",
			"$support",
			"$response",
			"$improve_list_csv"				
		);
	}

/*	-------------------------------------------------------------------------
	: Prepare serverside validation 
	------------------------------------------------------------------------- */
	
	$errors = array();
	 //validate firstname
	if(isset($_POST["firstname"])){
			if (!$firstname) {
				$errors[] = "You must enter your  firstname.";
			} elseif(strlen($firstname) < 2)  {
				$errors[] = "Firstname must be at least 2 characters.";
			}
	}
	//validate email address
	if(isset($_POST["emailaddress"])){
		if (!$emailaddress) {
			$errors[] = "You must enter an email.";
		} else if (!validEmail($emailaddress)) {
			$errors[] = "Your must enter a valid email.";
		}
	}
	
	//validate mobile phone number
	if(isset($_POST["telephone"])){
			if (!$telephone) {
				$errors[] = "You must enter your mobile phone number.";
			} elseif(!preg_match('/^[0-9]+$/', $telephone))  {
				$errors[] = "Phone number must include numbers only";
			} elseif(strlen($telephone) < 10)  {
				$errors[] = "Phone number must not be less than 10 numbers";
			} elseif(strlen($telephone) > 12)  {
				$errors[] = "Phone number must not exceed 12 numbers";
			}
	}	
		
	//validate department
	if(isset($_POST["department"])){
			if (!$department) {
				$errors[] = "Please select a department.";
			}
	}
	
	//validate check boxes
	if($improve[0]==''){	
		$errors[] = "Please check at least one option.";
	}	
	
	//validate message / comment
	if(isset($_POST["comment"])){
		if (strlen($comment) < 10) {
			if (!$comment) {
				$errors[] = "Oops you forgot to comment.";
			} else {
				$errors[] = "Comment must be at least 10 characters.";
			}
		}
	}
	
	if ($errors) {
		//Output errors in a list
		$errortext = "";
		foreach ($errors as $error) {
			$errortext .= '<li>'. $error . "</li>";
		}
	
		echo '<div class="alert notification alert-error">The following errors occured:<br><ul>'. $errortext .'</ul></div>';
	
	} else{	
	
			include dirname(__FILE__).'/phpmailer/PHPMailerAutoload.php';
			include dirname(__FILE__).'/templates/smartmessage.php';
				
			$mail = new PHPMailer();	
			$mail->isSMTP();                                      
			$mail->Host = $SMTP_host;                    
			$mail->SMTPAuth = true;                              
			$mail->Username = $SMTP_username;               
			$mail->Password = $SMTP_password;               
			$mail->SMTPSecure = $SMTP_protocol;                            
			$mail->Port = $SMTP_port;
			$mail->IsHTML(true);
			$mail->From = $emailaddress;
			$mail->CharSet = "UTF-8";
			$mail->FromName = $firstname;
			$mail->Encoding = "base64";
			$mail->Timeout = 200;
			$mail->ContentType = "text/html";
			$mail->addAddress($receiver_email, $receiver_name);
			$mail->Subject = $receiver_subject;
			$mail->Body = $message;
			$mail->AltBody = "Use an HTML compatible email client";
							
			// For multiple email recepients from the form 
			// Simply change recepients from false to true
			// Then enter the recipients email addresses
			// echo $message;
			$recipients = false;
			if($recipients == true){
				$recipients = array(
					"address@example.com" => "Recipient Name",
					"address@example.com" => "Recipient Name"
				);
				
				foreach($recipients as $email => $name){
					$mail->AddBCC($email, $name);
				}	
			}
			
			if($mail->Send()) {
			
			/*	-----------------------------------------------------------------
				: Generate the CSV file and post values if its true
				----------------------------------------------------------------- */		
				if($generateCSV == true){	
					if (file_exists($csvFile)) {
						$csvFileData = fopen($csvFile, 'a');
						fputcsv($csvFileData, $csvData );
					} else {
						$csvFileData = fopen($csvFile, 'a'); 
						$headerRowFields = array(
							"First Name",
							"Last Name",
							"Email Address",
							"Company",
							"Telephone",
							"Department",
							"Products",
							"Support",
							"Response",
							"Improve"														
						);
						fputcsv($csvFileData,$headerRowFields);
						fputcsv($csvFileData, $csvData );
					}
					fclose($csvFileData);
				}	
				
			/*	---------------------------------------------------------------------
				: Send the auto responder message if its true
				--------------------------------------------------------------------- */
				if($autoResponder == true){
				
					include dirname(__FILE__).'/templates/autoresponder.php';
					
					$automail = new PHPMailer();	
					$automail->isSMTP();                                      
					$automail->Host = $SMTP_host;                    
					$automail->SMTPAuth = true;                              
					$automail->Username = $SMTP_username;               
					$automail->Password = $SMTP_password;               
					$automail->SMTPSecure = $SMTP_protocol;                            
					$automail->Port = $SMTP_port;
					$automail->From = $receiver_email;
					$automail->FromName = $receiver_name;
					$automail->isHTML(true);                                 
					$automail->CharSet = "UTF-8";
					$automail->Encoding = "base64";
					$automail->Timeout = 200;
					$automail->ContentType = "text/html";
					$automail->AddAddress($emailaddress, $firstname);
					$automail->Subject = "Thank you for contacting us";
					$automail->Body = $automessage;
					$automail->AltBody = "Use an HTML compatible email client";
					$automail->Send();	 
				}
				
				if($redirectForm == true){
					echo '<script>setTimeout(function () { window.location.replace("'.$redirectForm_url.'") }, 8000); </script>';
				}
							
			  	echo '<div class="alert notification alert-success">Message has been sent successfully!</div>';
			} 
			else {
			  	echo '<div class="alert notification alert-error">Message not sent - server error occured!</div>';				  
			}
	}
?>
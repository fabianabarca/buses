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
	/*------------------ STEP 1 ------------------*/	
	$firstname = strip_tags(trim($_POST["firstname"]));
	$lastname = strip_tags(trim($_POST["lastname"]));	
	$emailaddress = strip_tags(trim($_POST["emailaddress"]));
	$telephone = strip_tags(trim($_POST["telephone"]));
	$company = strip_tags(trim($_POST["company"]));
	$industry = strip_tags(trim($_POST["industry"]));
	$address1 = strip_tags(trim($_POST["address1"]));
	$address2 = strip_tags(trim($_POST["address2"]));
	$city = strip_tags(trim($_POST["city"]));
	$zip = strip_tags(trim($_POST["zip"]));	
	/*------------------ STEP 2 ------------------*/
	$project_title = strip_tags(trim($_POST["project_title"]));
	$contact_person = strip_tags(trim($_POST["contact_person"]));
	$services = strip_tags(trim($_POST["services"]));
	$bugdet = strip_tags(trim($_POST["bugdet"]));
	$start_date = strip_tags(trim($_POST["start_date"]));
	$end_date = strip_tags(trim($_POST["end_date"]));
	$website = strip_tags(trim($_POST["website"]));
	$goals = strip_tags(trim($_POST["goals"]));
	$projectdetails = strip_tags(trim($_POST["projectdetails"]));
	/*------------------ STEP 3 ------------------*/
	$extras = $_POST["extras"];
	if ($extras[0]!=""){
		$extras_list = implode( '<br/>', $extras);
		$extras_list_csv = implode( '&nbsp; ', $extras);
	}
		
    $captcha = strip_tags(trim($_POST["captcha"]));
	
/*	----------------------------------------------------------------------
	: Prepare form field variables for CSV export
	----------------------------------------------------------------------- */	
	if($generateCSV == true){
		$csvFile = $csvFileName;	
		$csvData = array(
			"$firstname",
			"$lastname",
			"$emailaddress",
			"$telephone",
			"$company",
			"$industry",
			"$address1",
			"$address2",
			"$city",
			"$zip",
			"$project_title",
			"$contact_person",
			"$services",
			"$bugdet",
			"$start_date",
			"$end_date",
			"$website",
			"$goals",
			"$extras_list_csv"						
		);
	}

/*	-------------------------------------------------------------------------
	: Prepare serverside validation 
	------------------------------------------------------------------------- */ 
	$errors = array();
	
	/* Validate First Name
	------------------------------------------------------- */
	if(isset($_POST["firstname"])){
			if (!$firstname) {
				$errors[] = "Please enter firstname";
			}
	}
	
	/* Validate Last Name
	------------------------------------------------------- */
	if(isset($_POST["lastname"])){
			if (!$lastname) {
				$errors[] = "Please enter lastname";
			}
	}

	
	/* Validate Email
	------------------------------------------------------- */
	if(isset($_POST["emailaddress"])){
		if (!$emailaddress) {
			$errors[] = "Please enter your email";
		} else if (!validEmail($emailaddress)) {
			$errors[] = "You must enter a VALID email";
		}
	}
	
	/* Validate Telephone
	------------------------------------------------------ */
	if(isset($_POST["telephone"])){
		if (!$telephone) {
			$errors[] = "Please enter your telephone";
		} elseif(!preg_match('/^[0-9]+$/', $telephone))  {
			$errors[] = "Please enter numbers only";
		}
	}		
		
	
	/* Validate project title
	------------------------------------------------------- */
	if(isset($_POST["project_title"])){
		if (!$project_title) {
			$errors[] = "Please enter the project title";
		}
	}
	
	/* Contact person
	------------------------------------------------------- */
	if(isset($_POST["contact_person"])){
		if (!$contact_person) {
			$errors[] = "Please enter contact person";
		}
	}
	
	/* Validate services
	------------------------------------------------------- */
	if(isset($_POST["services"])){
		if (!$services) {
			$errors[] = "Please select services";
		}
	}		
	
	/* Validate Budget
	------------------------------------------------------- */
	if(isset($_POST["budget"])){
		if (!$budget) {
			$errors[] = "Please select project budget";
		}
	}
	
	/* Validate CAPTCHA
	------------------------------------------------------- */
	if(isset($_POST["captcha"])){
		if (!$captcha) {
			$errors[] = "You must enter the captcha code";
		} else if (($captcha) != $_SESSION['gfm_captcha']) {
			$errors[] = "Captcha code is incorrect";
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
					"address@example.com" => "Recipient Name",
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
							"Email",
							"Telephone",
							"Company",
							"Industry",
							"Address1",
							"Address2",
							"Cirt",
							"Zip",
							"Project Title",
							"Contact Person",
							"Services",
							"Budget",
							"Start Date",
							"End Date",
							"Website",
							"Goals",
							"Extras"																							
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
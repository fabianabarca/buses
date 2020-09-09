<?php

	/* Enter your name or company name below
	 * You can also use your website URL
	--------------------------------------------- */
	$receiver_name = "My Company";
	
	/* Enter your message subject below
	 * This subject is the one you will see in your email
	------------------------------------------------------ */	
	$receiver_subject = "New Quotation Message";
	
	/* Form message will be sent to this email address
	 * For more than one email go to smartprocess.php then
	 * Add addresses to the recipients section
	------------------------------------------------------ */
	$receiver_email = "example@domain.com";
		
	/* If you want to redirect to another page after sending the form
	 * Change the $redirectForm option below from (false) to (true)
	 * Then add your redirect page URL replace - http://example.com/thankyou.php
	----------------------------------------------------------------------------- */	
	$redirectForm = false;
	$redirectForm_url = "http://example.com/thankyou.php";
	
	/* Powered BY
	 * You will use both your website NAME and URL
	 * By default its powered by SMARTFORMS - http://www.doptiq.com/smart-forms
	----------------------------------------------------------------------------- */
	$poweredby_name = "Smart Forms";
	$poweredby_url = "http://www.doptiq.com/smart-forms";	
	
	/* If you want to store all form data in a CSV file
	 * Change the generateCSV option from (false) to (true)
	------------------------------------------------------------ */
	$generateCSV = false;
	
	/* Name for generated CSV file 
	 * Please don't change this name unless you have to
	------------------------------------------------------------ */	
	$csvFileName = "formcsv.csv";
	
	/* If you want to automatically reply to the sender 
	 * Change the autoresponder option below from (false) to (true)
	-------------------------------------------------------------------- */	
	$autoResponder = false;
	
	/* Add your SMTP details below
	 * Please specify servers, username, password, encryption type and port
	---------------------------------------------------------------------------- */                     
	$SMTP_host = 'smtp1.example.com'; 			// SMTP servers 
	$SMTP_username = 'your-smtp-username'; 		// SMTP username       
	$SMTP_password = 'your-smtp-password';		// SMTP password
	$SMTP_protocol = 'ssl';						// SMTP encryption 'ssl' or 'tls' accepted	  
	$SMTP_port = 465;							// SMTP Port number e.g 25, 465, 587	
?>
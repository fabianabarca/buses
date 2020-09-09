
	$(function() {
			   
				function reloadCaptcha(){ $("#captchax").attr("src","php/captcha/captcha.php?r=" + Math.random()); }
				$('.captcode').click(function(e){
					e.preventDefault();
					reloadCaptcha();
				});
				
				function swapButton(){
					var txtswap = $(".form-footer button[type='submit']");
					if (txtswap.text() == txtswap.data("btntext-sending")) {
						txtswap.text(txtswap.data("btntext-original"));
					} else {
						txtswap.data("btntext-original", txtswap.text());
						txtswap.text(txtswap.data("btntext-sending"));
					}
				}				
			   
				/* @telephone number masking 
				---------------------------------- */
		  		$("#guestelephone").mask('(999) 999-999999', {placeholder:'X'});			   
		
				/* @ date range datepicker 
				---------------------------------- */
				$( "#checkin" ).datepicker({
					defaultDate: "+1w",
					changeMonth: false,
					numberOfMonths: 1,
					prevText: '<i class="fa fa-chevron-left"></i>',
					nextText: '<i class="fa fa-chevron-right"></i>',
					onClose: function( selectedDate ) {
						$( "#checkout" ).datepicker( "option", "minDate", selectedDate );
					}
				});
				
				$( "#checkout" ).datepicker({
					defaultDate: "+1w",
					changeMonth: false,
					numberOfMonths: 1,
					prevText: '<i class="fa fa-chevron-left"></i>',
					nextText: '<i class="fa fa-chevron-right"></i>',			
					onClose: function( selectedDate ) {
						$( "#checkin" ).datepicker( "option", "maxDate", selectedDate );
					}
				});
				
				/* @ validation and submition
				---------------------------------- */				
				$( "#smart-form" ).validate({
											
						errorClass: "state-error",
						validClass: "state-success",
						errorElement: "em",
						onkeyup: false,
						onclick: false,						
						rules: {
								guestname: {
										required: true,
										minlength: 2
								},		
								emailaddress: {
										required: true,
										email: true
								},
								adults: {
										required: true,
										number: true
								},								
								children: {
										required: true,
										number: true
								},
								checkin:{
										required:true	
								},
								checkout:{
										required:true	
								},
								comment:{
										required:true,
										minlength: 10
								},
								captcha:{
									required:true,
									remote:'php/captcha/process.php'
								}								
						},
						messages:{
								guestname: {
										required: 'Enter your name',
										minlength: 'Name must be at least 2 characters'
								},				
								emailaddress: {
										required: 'Enter your email address',
										email: 'Enter a VALID email address'
								},
								adults: {
										required: 'Enter the number of adult guests',
										number: 'Please enter a VALID number'
								},														
								children: {
										required: 'Confirm the number of child guests',
										number: 'Please enter a VALID number'
								},															
								checkin:{
										required: 'Please select checkin date'
								},
								checkout:{
										required:'Please select checkout date'
								},
								comment:{
										required:'Please enter your comments',
										minlength: 'Comment must be at least 10 characters'
								},
								captcha:{
										required: 'You must enter the captcha code',
										remote:'Captcha code is incorrect'
								}								
						},
						highlight: function(element, errorClass, validClass) {
								$(element).closest('.field').addClass(errorClass).removeClass(validClass);
						},
						unhighlight: function(element, errorClass, validClass) {
								$(element).closest('.field').removeClass(errorClass).addClass(validClass);
						},
						errorPlacement: function(error, element) {
						   if (element.is(":radio") || element.is(":checkbox")) {
									element.closest('.option-group').after(error);
						   } else {
									error.insertAfter(element.parent());
						   }
						},				
						submitHandler:function(form) {
							$(form).ajaxSubmit({
									target:'.result',			   
									beforeSubmit:function(){
											swapButton();
											$('.form-footer').addClass('progress');
									},
									error:function(){
											swapButton();
											$('.form-footer').removeClass('progress');
									},
									 success:function(){
										 	swapButton();
											$('.form-footer').removeClass('progress');
											$('.alert-success').show().delay(7000).fadeOut();
											$('.field').removeClass("state-error, state-success");
											if( $('.alert-error').length == 0){
												$('#smart-form').resetForm();
												reloadCaptcha();
											}
									 }
							  });
						}
						
				});		
		
	});				
    
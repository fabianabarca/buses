	$(function() {
			   
				function swapButton(){
					var txtswap = $(".form-footer button[type='submit']");
					if (txtswap.text() == txtswap.data("btntext-sending")) {
						txtswap.text(txtswap.data("btntext-original"));
					} else {
						txtswap.data("btntext-original", txtswap.text());
						txtswap.text(txtswap.data("btntext-sending"));
					}
				}				   
			   
				$( "#smart-form" ).validate({
				
						/* @validation states + elements 
						------------------------------------------- */
						errorClass: "state-error",
						validClass: "state-success",
						errorElement: "em",
						onkeyup: false,
						onclick: false,
						
						/* @validation rules 
						------------------------------------------ */
						rules: {
								firstname: {
										required: true,
										minlength: 2
								},		
								emailaddress: {
										required: true,
										email: true
								},
								telephone: {
										required: true,
										number: true,
										minlength: 10,
										maxlength: 12
								},								
								department: {
										required: true
								},								
								comment: {
										required: true,
										minlength: 10
								},
								'improve[]':{
										required:true
								}								
						},
						
						/* @validation error messages 
						---------------------------------------------- */
							
						messages:{
								firstname: {
										required: 'Enter your firstname',
										minlength: 'Firstname must at least be 2 characters'
								},				
								emailaddress: {
										required: 'Enter your email address',
										email: 'Enter a VALID email address'
								},
								telephone: {
										required: 'Enter your mobile phone number',
										number: 'Phone number must include numbers only',
										minlength: 'Phone number must not be less than 10 numbers',
										maxlength: 'Phone number must not exceed 12 numbers'										
								},								
								department: {
										required: 'Please select a department'
								},																
								comment: {
										required: 'Oops you forgot to comment',
										minlength: 'Comment must be at least 10 characters'
								},
								'improve[]':{
										required: 'Please check at least one option'
								}								
						},

						/* @validation highlighting + error placement  
						---------------------------------------------------- */	
						
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
						
						/* @ajax form submition 
						---------------------------------------------------- */						
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
											}
									 }
							  });
						}
						
				});		
		
	});				
    
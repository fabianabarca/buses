	$(function() {
			   
				var bar = $('.bar');
				var percent = $('.percent');
				
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
								sendername: {
										required: true,
										minlength: 2
								},		
								emailaddress: {
										required: true,
										email: true
								},
								orderservices: {
										required: true
								},
								orderbudget: {
										required: true
								},
								orderfiles:{
									required:true,
									extension:"jpeg|jpg|png"
								},								
								sendermessage: {
										required: true,
										minlength: 10
								},
								captcha:{
									required:true,
									remote:'php/captcha/process.php'
								}
						},
						
						/* @validation error messages 
						---------------------------------------------- */
						messages:{
								sendername: {
										required: 'Enter your name',
										minlength: 'Name must be at least 2 characters'
								},				
								emailaddress: {
										required: 'Enter your email address',
										email: 'Enter a VALID email address'
								},
								orderservices: {
										required: 'Please select a service'
								},
								orderbudget: {
										required: 'Choose your budget range'
								},								
								orderfiles:{
									required:'Browse to add some order files',
									extension:'Sorry, file format not supported'
								},								
								sendermessage: {
										required: 'Oops you forgot your message',
										minlength: 'Message must be at least 10 characters'
								},															
								captcha:{
										required: 'You must enter the captcha code',
										remote:'Captcha code is incorrect'
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
										var percentVal = '0%';
										bar.width(percentVal);
										percent.html(percentVal);
										$( ".progress-section" ).show();
										$('.form-footer').addClass('progress');
									},
									uploadProgress: function(event, position, total, percentComplete) {
										var percentVal = percentComplete + '%';
										bar.width(percentVal);
										percent.html(percentVal);
									},								
									error:function(){
										swapButton();
										$( ".progress-section" ).hide(500);
										$('.form-footer').removeClass('progress');
									},
									 success:function(){
										swapButton(); 
										var percentVal = '100%';
										bar.width(percentVal);
										percent.html(percentVal);
										$('.progress-section').show().delay(5000).fadeOut();											
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
    
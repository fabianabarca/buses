	$(function(){
			
			$("#smart-form").steps({
				bodyTag: "fieldset",
				headerTag: "h2",
				bodyTag: "fieldset",
				transitionEffect: "slideLeft",
				titleTemplate: "<span class='number'>#index#</span> #title#",
				labels: {
					finish: "Submit Form",
					next: "Continue",
					previous: "Go Back",
					loading: "Loading..." 
				},
				onStepChanging: function (event, currentIndex, newIndex){
					if (currentIndex > newIndex){return true; }
					var form = $(this);
					if (currentIndex < newIndex){}
					return form.valid();
				},
				onStepChanged: function (event, currentIndex, priorIndex){
				},
				onFinishing: function (event, currentIndex){
					var form = $(this);
					form.validate().settings.ignore = ":disabled";
					return form.valid();
				},
				onFinished: function (event, currentIndex){
					var form = $(this);
					$(form).ajaxSubmit({
							target:'.result',			   
							beforeSubmit:function(){ 
							},
							error:function(){
							},
							 success:function(){
									$('.alert-success').show().delay(7000).fadeOut();
									$('.field').removeClass("state-error, state-success");
									if( $('.alert-error').length == 0){
										$('#smart-form').resetForm();
										reloadCaptcha();
									}
							 }
					  });					
				}
			}).validate({
				errorClass: "state-error",
				validClass: "state-success",
				errorElement: "em",
				onkeyup: false,
				onclick: false,
				rules: {
					firstname: {
						required: true
					},
					lastname: {
						required: true
					},					
					emailaddress: {
						required: true,
						email: true
					},
					telephone: {
						required: true,
						number: true
					},
					project_title: {
						required: true
					},
					contact_person:{
						required: true
					},
					services:{
						required: true
					},
					bugdet:{
						required: true
					},					
					captcha:{
						required:true,
						remote:'php/captcha/process.php'
					}					
				},
				messages: {
					firstname: {
						required: "Please enter firstname"
					},
					lastname: {
						required: "Please enter lastname"
					},
					emailaddress: {
						required: 'Please enter your email',
						email: 'You must enter a VALID email'
					},
					telephone: {
						required: 'Please enter your telephone',
						number: 'Please enter numbers only'
					},					
					project_title: {
						required: "Please enter the project title"
					},
					contact_person:{
						required: 'Please enter contact person'
					},
					services:{
						required: 'Please select services'
					},
					bugdet:{
						required: 'Please select project budget'
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
				}
			
			});
			
			/* Reload Captcha
			----------------------------------------------- */	
			function reloadCaptcha(){ $("#captchax").attr("src","php/captcha/captcha.php?r=" + Math.random()); }
			$('.captcode').click(function(e){
				e.preventDefault();
				reloadCaptcha();
			});			
			
			/* Project datepicker range
			----------------------------------------------- */			
			$("#start_date").datepicker({
				defaultDate: "+1w",
				changeMonth: false,
				numberOfMonths: 1,
				prevText: '<i class="fa fa-chevron-left"></i>',
				nextText: '<i class="fa fa-chevron-right"></i>',
				onClose: function( selectedDate ) {
					$( "#end_date" ).datepicker( "option", "minDate", selectedDate );
				}
			});
			
			$("#end_date").datepicker({
				defaultDate: "+1w",
				changeMonth: false,
				numberOfMonths: 1,
				prevText: '<i class="fa fa-chevron-left"></i>',
				nextText: '<i class="fa fa-chevron-right"></i>',			
				onClose: function( selectedDate ) {
					$( "#start_date" ).datepicker( "option", "maxDate", selectedDate );
				}
			});
					
	}); 
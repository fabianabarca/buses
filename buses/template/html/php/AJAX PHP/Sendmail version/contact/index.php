<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Smart forms - contact form </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <link rel="stylesheet" type="text/css"  href="css/smart-forms.css">
        <link rel="stylesheet" type="text/css"  href="css/font-awesome.min.css">
        
        <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="js/jquery.form.min.js"></script>
        <script type="text/javascript" src="js/jquery.validate.min.js"></script>
        <script type="text/javascript" src="js/additional-methods.min.js"></script>
        <script type="text/javascript" src="js/smart-form.js"></script> 
        
        <!--[if lte IE 9]>
            <script type="text/javascript" src="js/jquery.placeholder.min.js"></script>
        <![endif]-->    
        
        <!--[if lte IE 8]>
            <link type="text/css" rel="stylesheet" href="css/smart-forms-ie8.css">
        <![endif]-->
    </head>
    
    <body class="woodbg">
        <div class="smart-wrap">
            <div class="smart-forms smart-container wrap-2">
            
                <div class="form-header header-primary">
                        <h4><i class="fa fa-comments"></i>Contact us</h4>
                </div><!-- end .form-header section -->
                
                <form method="post" action="php/smartprocess.php" id="smart-form">
                    <div class="form-body">
                    
                        <div class="section">
                            <label class="field prepend-icon">
                                <input type="text" name="sendername" id="sendername" class="gui-input" placeholder="Enter name">
                                <span class="field-icon"><i class="fa fa-user"></i></span>  
                            </label>
                        </div><!-- end section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <input type="email" name="emailaddress" id="emailaddress" class="gui-input" placeholder="Email address">
                                <span class="field-icon"><i class="fa fa-envelope"></i></span>
                            </label>
                        </div><!-- end section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <input type="text" name="sendersubject" id="sendersubject" class="gui-input" placeholder="Enter subjec">
                                <span class="field-icon"><i class="fa fa-lightbulb-o"></i></span>
                            </label>
                        </div><!-- end section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <textarea class="gui-textarea" id="sendermessage" name="sendermessage" placeholder="Enter message"></textarea>
                                <span class="field-icon"><i class="fa fa-comments"></i></span>
                                <span class="input-hint"> <strong>Hint:</strong> Please enter between 80 - 300 characters.</span>   
                            </label>
                        </div><!-- end section -->
                        
                        <div class="section">
                            <div class="smart-widget sm-left sml-120">
                                <label class="field">
                                    <input type="text" name="captcha" id="captcha" class="gui-input sfcode" maxlength="6" placeholder="Enter CAPTCHA">
                                </label>
                                <label class="button captcode">
                                    <img src="php/captcha/captcha.php?<?php echo time();?>" id="captchax" alt="captcha">
                                    <span class="refresh-captcha"><i class="fa fa-refresh"></i></span>
                                </label>
                            </div><!-- end .smart-widget section --> 
                        </div><!-- end section -->
                        
                       <div class="result"></div><!-- end .result  section --> 
                                                                                                                    
                    </div><!-- end .form-body section -->
                    <div class="form-footer">
                        <button type="submit" data-btntext-sending="Sending..." class="button btn-primary">Submit</button>
                        <button type="reset" class="button"> Cancel </button>
                    </div><!-- end .form-footer section -->
                </form>
            </div><!-- end .smart-forms section -->
        </div><!-- end .smart-wrap section -->
    </body>
</html>

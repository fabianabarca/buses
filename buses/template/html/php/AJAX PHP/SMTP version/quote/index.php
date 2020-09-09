<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Smart forms - Quotation form </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <link rel="stylesheet" type="text/css"  href="css/smart-forms.css">
        <link rel="stylesheet" type="text/css"  href="css/font-awesome.min.css">
        
        <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="js/jquery-ui-custom.min.js"></script>
        <script type="text/javascript" src="js/jquery-ui-touch-punch.min.js"></script>    
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
                    <h4><i class="fa fa-comments"></i>Get A Quote</h4>
              </div><!-- end .form-header section -->
                
                <form method="post" action="php/smartprocess.php" id="smart-form">
                    <div class="form-body">
                       <div class="spacer-b40">
                            <div class="tagline"><span>Your Details </span></div><!-- .tagline -->
                        </div>                 
                    
                        <div class="frm-row">
                        
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="text" name="sendername" id="sendername" class="gui-input" placeholder="Name / company name">
                                    <span class="field-icon"><i class="fa fa-user"></i></span>  
                                </label>
                            </div><!-- end section --> 
                            
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="email" name="emailaddress" id="emailaddress" class="gui-input" placeholder="Email address">
                                    <span class="field-icon"><i class="fa fa-envelope"></i></span> 
                                </label>
                            </div><!-- end section -->
                        
                        </div><!-- end frm-row section -->
                        
                        <div class="frm-row">
                        
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="tel" name="telephone" id="telephone" class="gui-input" placeholder="Telephone">
                                    <span class="field-icon"><i class="fa fa-phone-square"></i></span> 
                                </label>
                            </div><!-- end section -->                    
                            
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="url" name="senderwebsite" id="senderwebsite" class="gui-input" placeholder="Website URL">
                                    <span class="field-icon"><i class="fa fa-globe"></i></span> 
                                </label>
                            </div><!-- end section -->
                        
                        </div><!-- end frm-row section -->
                        
                        <div class="spacer-t20 spacer-b40">
                            <div class="tagline"><span> Project Details </span></div><!-- .tagline -->
                        </div>
                        
                        <div class="frm-row">
                        
                                 <div class="section colm colm6">
                                    <label class="field select">
                                        <select id="services" name="services">
                                            <option value="">Select a service...</option>
                                            <option value="webdesign">Complete Website Design</option>
                                            <option value="csshtml">HTML / CSS Coding Only</option>
                                            <option value="wordpress">Wordpress Customization</option>
                                            <option value="logo">Logo Design</option>
                                            <option value="identity">Corporate Identity</option>
                                            <option value="cms">Custom CMS</option>
                                        </select>
                                        <i class="arrow double"></i>                    
                                    </label>  
                                </div><!-- end section -->
                                
                                <div class="section colm colm6">
                                   <label class="field select">
                                       <select id="timeframe" name="timeframe">
                                            <option value="">Choose Timeframe</option>
                                            <option value="Right Away">Right Away</option>
                                            <option value="Within 1 Month">Within 1 Month</option>
                                            <option value="Within 2 Months">Within 2 Months</option>
                                            <option value="Within 3 Months">Within 3 Months</option>
                                            <option value="Within 6 Months">Within 6 Months</option>
                                            <option value="Don't Know Yet">Don't Know Yet</option>
                                       </select>
                                       <i class="arrow double"></i>                    
                                   </label>  
                               </div><!-- end section -->   
      
                        </div><!-- end frm-row section -->
                        
                        
                        <div class="section spacer-b30">
                            <div class="spacer-b15">
                                <label for="budget">Project budget:</label>
                                <input type="text" id="budget" name="budget" class="slider-input" value="$15000"> 
                            </div><!-- end .spacer -->                   
                            <div class="slider-wrapper">
                                <div id="budget-slider"></div>
                            </div><!-- end .slider-wrapper -->
                        </div><!-- end section -->                    
    
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <textarea class="gui-textarea" id="details" name="details" placeholder="Tell us more about your idea..."></textarea>
                                <span class="field-icon"><i class="fa fa-comments"></i></span>
                                <span class="input-hint"> <strong>NOTE:</strong> Be as detailed as possible for an accurate quote.</span>   
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
                        <button type="submit" data-btntext-sending="Sending..." class="button btn-primary">Submit Request</button>
                        <button type="reset" class="button"> Cancel </button>
                    </div><!-- end .form-footer section -->
                </form>
            </div><!-- end .smart-forms section -->
        </div><!-- end .smart-wrap section -->
    </body>
</html>

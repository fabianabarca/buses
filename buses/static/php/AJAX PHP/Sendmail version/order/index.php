<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Smart forms - order form </title>
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
                    <h4><i class="fa fa-comments"></i>Make an order</h4>
              </div><!-- end .form-header section -->
                
                <form method="post" action="php/smartprocess.php" id="smart-form" enctype="multipart/form-data">
                    <div class="form-body">
                    
                       <div class="spacer-b40">
                            <div class="tagline"><span>Your Details </span></div><!-- .tagline -->
                        </div>                 
                    
                        <div class="frm-row">
                        
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="text" name="sendername" id="sendername" class="gui-input" placeholder="Enter name">
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
                            <div class="tagline"><span> Order Details </span></div><!-- .tagline -->
                        </div>
                        
                        <div class="frm-row">
                        
                                 <div class="section colm colm6">
                                    <label class="field select">
                                        <select id="orderservices" name="orderservices">
                                            <option value="">Select a service...</option>
                                            <option value="webdesign">Webdesign</option>
                                            <option value="wordpress">Wordpress customization</option>
                                            <option value="identity">Corporate identity</option>
                                            <option value="cms">Custom CMS</option>
                                        </select>
                                        <i class="arrow double"></i>                    
                                    </label>  
                                </div><!-- end section -->
                                
                                <div class="section colm colm6">
                                    <label class="field select">
                                        <select id="orderbudget" name="orderbudget">
                                            <option value="">Choose a budget</option>
                                            <option value="500-1000"> $500 - $1000 </option>
                                            <option value="1000-2000"> $1000 - $2000 </option>
                                            <option value="2000-4000"> $2000 - $4000 </option>
                                            <option value="5000+"> $5000+ </option>
                                        </select>
                                        <i class="arrow double"></i>                    
                                    </label>  
                                </div><!-- end section -->                     
                                          
                        </div><!-- end frm-row section -->
                        
                       <div class="section colm colm6">
                           <label class="field select">
                               <select id="ordertimeframe" name="ordertimeframe">
                                   <option value="">Select order timeframe</option>
                                   <option value="1week"> 1 Week </option>
                                   <option value="2weeks"> 2 Weeks </option>
                                   <option value="3weeks"> 3 Weeks </option>
                                   <option value="1month"> 1 Month </option>
                                   <option value="2month+"> 2 Month </option>
                               </select>
                               <i class="arrow double"></i>                    
                           </label>  
                       </div><!-- end section --> 
                        
                        <div class="section">
                            <label class="field prepend-icon file">
                                <span class="button btn-primary"> Choose File </span>
                                <input type="file" class="gui-file" name="orderfiles" id="orderfiles" 
                                onChange="document.getElementById('orderupload').value = this.value;">
                                <input type="text" class="gui-input" id="orderupload" placeholder="upload sample files" readonly>
                                <span class="field-icon"><i class="fa fa-upload"></i></span>
                            </label>
                            <span class="small-text block spacer-t10 fine-grey"> Allowed file formats jpg or png images only - Maximum of 2MB </span> 
                        </div><!-- end  section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <textarea class="gui-textarea" id="sendermessage" name="sendermessage" placeholder="Order details"></textarea>
                                <span class="field-icon"><i class="fa fa-comments"></i></span>
                                <span class="input-hint"> <strong>NOTE:</strong> Be as detailed as possible for better feedback.</span>   
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
                        
                        <div class="result spacer-b10"></div><!-- end .result  section -->                     
                        
                        <div class="section progress-section">
                            <div class="progress-bar progress-animated bar-primary">
                                <div class="bar"></div>
                                <div class="percent">0%</div>
                            </div>
                        </div><!-- end progress section --> 
                                                                                                                    
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

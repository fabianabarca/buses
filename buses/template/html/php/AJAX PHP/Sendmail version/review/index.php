<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Smart Forms - Feedback Form </title>
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
            <div class="smart-forms smart-container wrap-3">
            
                <div class="form-header header-primary">
                    <h4><i class="fa fa-rocket"></i>Your feedback</h4>
              </div><!-- end .form-header section -->
                
                <form method="post" action="php/smartprocess.php" id="smart-form">
                    <div class="form-body">
                    
                        <div class="frm-row">
                        
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="text" name="firstname" id="firstname" class="gui-input" placeholder="First name...">
                                    <span class="field-icon"><i class="fa fa-user"></i></span>  
                                </label>
                            </div><!-- end section -->
                            
                            <div class="section colm colm6">
                                <label class="field prepend-icon">
                                    <input type="text" name="lastname" id="lastname" class="gui-input" placeholder="Last name...">
                                    <span class="field-icon"><i class="fa fa-user"></i></span>  
                                </label>
                            </div><!-- end section --> 
                                                                       
                        </div><!-- end frm-row section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <input type="text" name="company" id="company" class="gui-input" placeholder="Company">
                                <span class="field-icon"><i class="fa fa-building-o"></i></span>  
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
                                <input type="tel" name="telephone" id="telephone" class="gui-input" placeholder="Telephone contact">
                                <span class="field-icon"><i class="fa fa-phone-square"></i></span>  
                            </label>
                        </div><!-- end section --> 
                        
                        <div class="section">
                            <label class="field select">
                                <select id="department" name="department">
                                    <option value="">Select a department...</option>
                                    <option value="Administration">Administration</option>
                                    <option value="Marketing">Marketing &amp; Sales</option>
                                    <option value="Technical">Technical</option>
                                    <option value="other">Other</option>
                                </select>
                                <i class="arrow double"></i>                    
                            </label>  
                        </div><!-- end section -->
                        
                        <div class="section">
                            <label class="field prepend-icon">
                                <textarea class="gui-textarea" id="comment" name="comment" placeholder="Feedback message"></textarea>
                                <span class="field-icon"><i class="fa fa-comments"></i></span>
                                <span class="input-hint"> <strong>Hint:</strong> Please enter between 80 - 300 characters.</span>   
                            </label>
                        </div><!-- end section -->
                        
                        <div class="spacer spacer-b20"></div> 
                        
                        <div class="section">
                        
                            <div class="rating block">
                                <span class="lbl-text">Rate our products</span>
                                <div class="rating-wrapper">
                                    <input class="rating-input" id="five-stars" type="radio"  name="products" value="5">
                                    <label class="rating-star" for="five-stars"><i class="fa fa-star"></i><span>Excellent</span></label>
                                    <input class="rating-input" id="four-stars" type="radio"  name="products" value="4">
                                    <label class="rating-star" for="four-stars"><i class="fa fa-star"></i><span>Good</span></label>
                                    <input class="rating-input" id="three-stars" type="radio"  name="products" value="3" checked>
                                    <label class="rating-star" for="three-stars"><i class="fa fa-star"></i><span>Tried</span></label>
                                    <input class="rating-input" id="two-stars" type="radio"  name="products" value="2">
                                    <label class="rating-star" for="two-stars"><i class="fa fa-star"></i><span>Fair</span></label>
                                    <input class="rating-input" id="one-star" type="radio"  name="products" value="1">
                                    <label class="rating-star" for="one-star"><i class="fa fa-star"></i><span>Poor</span></label>
                                </div>
                            </div><!-- end rating section -->
                            
                            <div class="rating block">
                                <span class="lbl-text">Rate support team</span>
                                <div class="rating-wrapper">
                                    <input class="rating-input" id="5stars" type="radio"  name="support" value="5">
                                    <label class="rating-star" for="5stars"><i class="fa fa-star"></i><span>Excellent</span></label>
                                    <input class="rating-input" id="4stars" type="radio"  name="support" value="4">
                                    <label class="rating-star" for="4stars"><i class="fa fa-star"></i><span>Good</span></label>
                                    <input class="rating-input" id="3stars" type="radio"  name="support" value="3">
                                    <label class="rating-star" for="3stars"><i class="fa fa-star"></i><span>Tried</span></label>
                                    <input class="rating-input" id="2stars" type="radio"  name="support" value="2" checked>
                                    <label class="rating-star" for="2stars"><i class="fa fa-star"></i><span>Fair</span></label>
                                    <input class="rating-input" id="1star" type="radio"  name="support" value="1">
                                    <label class="rating-star" for="1star"><i class="fa fa-star"></i><span>Poor</span></label>
                                </div>
                            </div><!-- end rating section -->
                            
                            <div class="rating block">
                                <span class="lbl-text">Rate our response</span>
                                <div class="rating-wrapper">
                                    <input class="rating-input" id="5s" type="radio"  name="response" value="5">
                                    <label class="rating-star" for="5s"><i class="fa fa-star"></i><span>Excellent</span></label>
                                    <input class="rating-input" id="4s" type="radio"  name="response" value="4">
                                    <label class="rating-star" for="4s"><i class="fa fa-star"></i><span>Good</span></label>
                                    <input class="rating-input" id="3s" type="radio"  name="response" value="3">
                                    <label class="rating-star" for="3s"><i class="fa fa-star"></i><span>Tried</span></label>
                                    <input class="rating-input" id="2s" type="radio"  name="response" value="2">
                                    <label class="rating-star" for="2s"><i class="fa fa-star"></i><span>Fair</span></label>
                                    <input class="rating-input" id="1s" type="radio"  name="response" value="1" checked>
                                    <label class="rating-star" for="1s"><i class="fa fa-star"></i><span>Poor</span></label>
                                </div>
                            </div><!-- end rating section -->                        
                                                           
                        </div><!-- end  section -->
                        
                        <div class="spacer spacer-b25"></div> 
                        
                        <div class="spacer-b20">
                            <label class="field-label">Which areas require further improvement?</label>
                        </div>
                        
                        <div class="frm-row">
                            <div class="option-group field">
                                <div class="section colm colm6">
                                
                                    <label class="option block spacer-b10">
                                        <input type="checkbox" name="improve[]" value="response">
                                        <span class="checkbox"></span> Response time                  
                                    </label>
                                    
                                    <label class="option block spacer-b10">
                                        <input type="checkbox" name="improve[]" value="support">
                                        <span class="checkbox"></span> Customer support               
                                    </label>
                                    
                                    <label class="option block">
                                        <input type="checkbox" name="improve[]" value="updates">
                                        <span class="checkbox"></span> Product updates                 
                                    </label>                                                        
                                                            
                                </div><!-- end section -->
                                <div class="section colm colm6">
                                
                                    <label class="option block spacer-b10">
                                        <input type="checkbox" name="improve[]" value="invoicing">
                                        <span class="checkbox"></span> Timely invoicing                  
                                    </label>
                                    
                                    <label class="option block spacer-b10">
                                        <input type="checkbox" name="improve[]" value="social">
                                        <span class="checkbox"></span> Social features             
                                    </label>
                                    
                                    <label class="option block">
                                        <input type="checkbox" name="improve[]" value="reports">
                                        <span class="checkbox"></span> Reports &amp; analytics                
                                    </label> 
                                                            
                                </div><!-- end section -->
                            </div><!-- end option-group section -->
                        </div><!-- end .frm-row section -->
                        <div class="result"></div><!-- end .result  section -->
                    </div><!-- end .form-body section -->
                    <div class="form-footer">
                        <button type="submit" data-btntext-sending="Sending..." class="button btn-primary">Submit Feedback</button>
                        <button type="reset" class="button"> Cancel </button>
                    </div><!-- end .form-footer section -->
                </form>
            </div><!-- end .smart-forms section -->
        </div><!-- end .smart-wrap section -->
    </body>
</html>

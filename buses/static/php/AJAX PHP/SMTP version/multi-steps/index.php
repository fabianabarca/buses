<!DOCTYPE html>
<html lang="en">
  <head>
    <title> Smart forms - multi-steps form </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" type="text/css"  href="css/smart-forms.css">
    <link rel="stylesheet" type="text/css"  href="css/smart-addons.css">
    <link rel="stylesheet" type="text/css"  href="css/font-awesome.min.css">
    
    <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
    <script type="text/javascript" src="js/jquery.steps.min.js"></script>
    <script type="text/javascript" src="js/jquery-ui-custom.min.js"></script>
    <script type="text/javascript" src="js/jquery.validate.min.js"></script>
    <script type="text/javascript" src="js/additional-methods.min.js"></script>    
    <script type="text/javascript" src="js/jquery.form.min.js"></script>
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
    	<div class="smart-forms smart-container wrap-1">
        
            	<div class="form-body smart-steps stp-three">
                 <form method="post" action="php/smartprocess.php" id="smart-form">
                            <h2>Personal Details</h2>
                            <fieldset>
                            
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="firstname" id="firstname" class="gui-input" placeholder="First name">
                                            <span class="field-icon"><i class="fa fa-user"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="lastname" id="lastname" class="gui-input" placeholder="Last name">
                                            <span class="field-icon"><i class="fa fa-user"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                </div><!-- end .frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="email" name="emailaddress" id="emailaddress" class="gui-input" placeholder="Email address">
                                            <span class="field-icon"><i class="fa fa-envelope"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="tel" name="telephone" id="telephone" class="gui-input" placeholder="Telephone number">
                                            <span class="field-icon"><i class="fa fa-phone-square"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                </div><!-- end .frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="company" id="company" class="gui-input" placeholder="Company or business name">
                                            <span class="field-icon"><i class="fa fa-lightbulb-o"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field select">
                                            <select id="industry" name="industry">
                                                <option value=''>Select Industry...</option>
                                                <option value='Accounting/Finance' >Accounting/Finance</option>
                                                <option value='Advertising/Public Relations' >Advertising/Public Relations</option>
                                                <option value='Aerospace/Aviation' >Aerospace/Aviation</option>
                                                <option value='Arts/Entertainment/Publishing' >Arts/Entertainment/Publishing</option>
                                                <option value='Automotive' >Automotive</option>
                                                <option value='Banking/Mortgage' >Banking/Mortgage</option>
                                                <option value='Business Development' >Business Development</option>
                                                <option value='Business Opportunity' >Business Opportunity</option>
                                                <option value='Clerical/Administrative' >Clerical/Administrative</option>
                                                <option value='Construction/Facilities' >Construction/Facilities</option>
                                                <option value='Consumer Goods' >Consumer Goods</option>
                                                <option value='Customer Service' >Customer Service</option>
                                                <option value='Education/Training' >Education/Training</option>
                                                <option value='Energy/Utilities' >Energy/Utilities</option>
                                                <option value='Engineering' >Engineering</option>
                                                <option value='Government/Military' >Government/Military</option>
                                                <option value='Green' >Green</option>
                                                <option value='Healthcare' >Healthcare</option>
                                                <option value='Hospitality/Travel' >Hospitality/Travel</option>
                                                <option value='Human Resources' >Human Resources</option>
                                                <option value='Installation/Maintenance' >Installation/Maintenance</option>
                                                <option value='Insurance' >Insurance</option>
                                                <option value='Internet' >Internet</option>
                                                <option value='Job Search Aids' >Job Search Aids</option>
                                                <option value='Law Enforcement/Security' >Law Enforcement/Security</option>
                                                <option value='Legal' >Legal</option>
                                                <option value='Management/Executive' >Management/Executive</option>
                                                <option value='Manufacturing/Operations' >Manufacturing/Operations</option>
                                                <option value='Marketing' >Marketing</option>
                                                <option value='Non-Profit/Volunteer' >Non-Profit/Volunteer</option>
                                                <option value='Pharmaceutical/Biotech' >Pharmaceutical/Biotech</option>
                                                <option value='Professional Services' >Professional Services</option>
                                                <option value='QA/Quality Control' >QA/Quality Control</option>
                                                <option value='Real Estate' >Real Estate</option>
                                                <option value='Restaurant/Food Service' >Restaurant/Food Service</option>
                                                <option value='Retail' >Retail</option>
                                                <option value='Sales' >Sales</option>
                                                <option value='Science/Research' >Science/Research</option>
                                                <option value='Skilled Labor' >Skilled Labor</option>
                                                <option value='Technology' >Technology</option>
                                                <option value='Telecommunications' >Telecommunications</option>
                                                <option value='Transportation/Logistics' >Transportation/Logistics</option>
                                                <option value='Other' >Other</option>
                                            </select>
                                            <i class="arrow double"></i>                             
                                        </label>
                                    </div><!-- end section -->
                                </div><!-- end .frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="address1" id="address1" class="gui-input" placeholder="Street Address">
                                            <span class="field-icon"><i class="fa fa-map-marker"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="address2" id="address2" class="gui-input" placeholder="Address Line 2">
                                            <span class="field-icon"><i class="fa fa-map-marker"></i></span>   
                                        </label>
                                    </div><!-- end section -->
                                </div><!-- end .frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="city" id="city" class="gui-input" placeholder="City">
                                            <span class="field-icon"><i class="fa fa-building"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="zip" id="zip" class="gui-input" placeholder="Zip">
                                            <span class="field-icon"><i class="fa fa-bullseye"></i></span>   
                                        </label>
                                    </div><!-- end section -->
                                </div><!-- end .frm-row section -->                                                                                                 

                            </fieldset>
            
                            <h2>Project Overview </h2>
                            <fieldset>
                            
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="project_title" id="project_title" class="gui-input" placeholder="Project title">
                                            <span class="field-icon"><i class="fa fa-check-circle"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                	
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="contact_person" id="contact_person" class="gui-input" placeholder="Contact person">
                                            <span class="field-icon"><i class="fa fa-male"></i></span>  
                                        </label>
                                    </div><!-- end section -->               
                                </div><!-- end frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field select">
                                            <select id="services" name="services">
                                                <option value="">Services needed</option>
                                                <option value="E-commerce">E-commerce</option>
                                                <option value="Content Management System">Content Management System</option>
                                                <option value="Content Copyrighting">Content Copyrighting</option>
                                                <option value="Online Community">Online Community</option>
                                                <option value="Systems Integration">Systems Integration</option>
                                                <option value="Performance Tuning">Performance Tuning</option>
                                                <option value="Mobile Application">Mobile Application</option>
                                                <option value="Data Visualization">Data Visualization</option>
                                                <option value="Other">Other</option>
                                            </select>
                                            <i class="arrow double"></i>                             
                                        </label>
                                    </div><!-- end section -->
                                    
                                    <div class="section colm colm6">
                                        <label class="field select">
                                          <select id="bugdet" name="bugdet">
                                              <option value="">Project Budget</option>
                                              <option value="$5,000 - $15,0000">$5,000 - $15,0000</option>
                                              <option value="$15,000 - $30,000">$15,000 - $30,000</option>
                                              <option value="$30,000 - $50,000">$30,000 - $50,000</option>
                                              <option value="$50,000 - $100,000">$50,000 - $100,000</option>
                                              <option value="More than $100,000">More than $100,000</option>
                                              <option value="Not sure">Not sure</option>
                                          </select>
                                          <i class="arrow double"></i>                   
                                        </label>
                                    </div><!-- end section -->                
                                </div><!-- end frm-row section -->                                
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="start_date" id="start_date" class="gui-input" placeholder="Project start date" readonly>
                                            <span class="field-icon"><i class="fa fa-calendar"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                	
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="end_date" id="end_date" class="gui-input" placeholder="Project end date" readonly>
                                            <span class="field-icon"><i class="fa fa-calendar-o"></i></span>  
                                        </label>
                                    </div><!-- end section -->               
                                </div><!-- end frm-row section -->
                                
                                <div class="frm-row">
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="url" name="website" id="website" class="gui-input" placeholder="Current website">
                                            <span class="field-icon"><i class="fa fa-globe"></i></span>  
                                        </label>
                                    </div><!-- end section -->
                                	
                                    <div class="section colm colm6">
                                        <label class="field prepend-icon">
                                            <input type="text" name="goals" id="goals" class="gui-input" placeholder="Project goals">
                                            <span class="field-icon"><i class="fa fa-bar-chart"></i></span>  
                                        </label>
                                    </div><!-- end section -->               
                                </div><!-- end frm-row section --> 
                                
                                <div class="section">
                                    <label class="field prepend-icon">
                                        <textarea class="gui-textarea" id="projectdetails" name="projectdetails" 
                                        placeholder="Quick summary of the project"></textarea>
                                        <span class="field-icon"><i class="fa fa-comments"></i></span>
                                        <span class="input-hint"> 
                                            <strong>Project Details:</strong> add more project specific details
                                        </span>   
                                    </label>
                                </div><!-- end section -->                                                                                               
                                
                            </fieldset>
                            
                            <h2>Project Extras</h2>
                            <fieldset>
                            	<div class="section spacer-t10">
                                	<p class="small-text fine-grey"> Please choose project extras </p>
                                </div>
                                <div class="frm-row">
                                	<div class="option-group field">
                                        <div class="section colm colm4">
                                            <label class="option block">
                                                <input type="checkbox" name="extras[]" value="Domain Name">
                                                <span class="checkbox"></span> Domain Name          
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Yearly Hosting">
                                                <span class="checkbox"></span> Yearly Hosting             
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Discussion Forum">
                                                <span class="checkbox"></span> Discussion Forum            
                                            </label>                                            
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Newsletter">
                                                <span class="checkbox"></span> Newsletter            
                                            </label>     
                                        </div><!-- end section -->
                                        
                                        <div class="section colm colm4">
                                            <label class="option block">
                                                <input type="checkbox" name="extras[]" value="Video Integration">
                                                <span class="checkbox"></span> Video Integration            
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Events Calendar ">
                                                <span class="checkbox"></span> Events Calendar            
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Display Adverts">
                                                <span class="checkbox"></span> Display Adverts               
                                            </label>                                            
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Social Media">
                                                <span class="checkbox"></span> Social Media               
                                            </label>        
                                        </div><!-- end section -->                                        
                                        
                                        <div class="section colm colm4">
                                            <label class="option block">
                                                <input type="checkbox" name="extras[]" value="Photo galleries">
                                                <span class="checkbox"></span> Photo Galleries           
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Membership">
                                                <span class="checkbox"></span> Membership             
                                            </label>
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Podcasting">
                                                <span class="checkbox"></span> Podcasting            
                                            </label>                                            
                                            <label class="option block spacer-t10">
                                                <input type="checkbox" name="extras[]" value="Blogging">
                                                <span class="checkbox"></span> Blogging            
                                            </label>        
                                        </div><!-- end section -->
                                    </div><!-- .option-group -->                
                                </div><!-- end frm-row section --> 
                                
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
                                 
                            </fieldset>
                    </form>                                                                                   
                </div><!-- end .form-body section -->
            
        </div><!-- end .smart-forms section -->
    </div><!-- end .smart-wrap section -->

</body>
</html>

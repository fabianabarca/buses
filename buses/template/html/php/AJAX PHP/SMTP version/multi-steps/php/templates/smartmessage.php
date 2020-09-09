<?php  
$message = '
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Smart forms - Email message template </title>    
</head>

<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">
    <center>
        <table style="padding:30px 10px;background:#F4F4F4;width:100%;font-family:arial" cellpadding="0" cellspacing="0">
                
                <tbody>
                    <tr>
                        <td>
                        
                            <table style="max-width:540px;min-width:320px" align="center" cellspacing="0">
                                <tbody>
                                
                                    <tr>
                                        <td style="background:#fff;border:1px solid #D8D8D8;padding:30px 30px" align="center">
                                        
                                            <table align="center">
                                                <tbody>
                                                
                                                    <tr>
                                                        <td style="border-bottom:1px solid #D8D8D8;color:#666;text-align:center;padding-bottom:30px">
                                                            
                                                            <table style="margin:auto" align="center">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="color:#005f84;font-size:22px;font-weight:bold;text-align:center;font-family:arial">
                                                                
                                                                            PROJECT QUOTATION DETAILS
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    
                                                    <tr>
                                               <td style="color:#666;padding:15px; padding-bottom:0;font-size:14px;line-height:20px;font-family:arial;text-align:left">
                                    
                                                    <div style="font-style:normal;padding-bottom:15px;font-family:arial;line-height:20px;text-align:left">
													
														<p style="font-size:12px;color:#3397CD;letter-spacing:2px;margin-bottom:3px;">PERSONAL DETAILS</p>
														<p style="border-bottom:1px solid #fff; height:0; margin:0; color:#666;text-align:center;padding:0"></p>
                                                        
                                                        <p><span style="font-weight:bold;font-size:16px">First name:</span> '.$firstname.'</p>
														<p><span style="font-weight:bold;font-size:16px">Last name:</span> '.$lastname.'</p>
                                                        <p><span style="font-weight:bold;font-size:16px">Email address:</span> '.$emailaddress.'</p>
                                                        <p><span style="font-weight:bold;font-size:16px">Telephone:</span> '.$telephone.'</p>
														<p><span style="font-weight:bold;font-size:16px">Company name:</span> '.$company.'</p>
														<p><span style="font-weight:bold;font-size:16px">Industry:</span> '.$industry.'</p>
														<p><span style="font-weight:bold;font-size:16px">Line address 1:</span> '.$address1.'</p>
														<p><span style="font-weight:bold;font-size:16px">Line address 2:</span> '.$address2.'</p>
                                                        <p><span style="font-weight:bold;font-size:16px">City:</span> '.$city.'</p>
														<p><span style="font-weight:bold;font-size:16px">Zip:</span> '.$zip.'</p>
														
														<p style="font-size:12px;color:#3397CD;letter-spacing:2px;margin-bottom:3px;">PROJECT OVERVIEW</p>
														<p style="border-bottom:1px solid #fff; height:0; margin:0; color:#666;text-align:center;padding:0"></p>
														
														<p><span style="font-weight:bold;font-size:16px">Project title:</span> '.$project_title.'</p>
														<p><span style="font-weight:bold;font-size:16px">Contact person:</span> '.$contact_person.'</p>
														<p><span style="font-weight:bold;font-size:16px">Services:</span> '.$services.'</p>
														<p><span style="font-weight:bold;font-size:16px">Bugdet:</span> '.$bugdet.'</p>
														<p><span style="font-weight:bold;font-size:16px">Start date:</span> '.$start_date.'</p>
														<p><span style="font-weight:bold;font-size:16px">End date:</span> '.$end_date.'</p>
														<p><span style="font-weight:bold;font-size:16px">Website:</span> '.$website.'</p>
														<p><span style="font-weight:bold;font-size:16px">Goals:</span> '.$goals.'</p>
														<p><span style="font-weight:bold;font-size:16px;">Project summary:</span> </p>
                                                        <p style="margin-bottom:0;"> '.nl2br($projectdetails).' </p>
														
														<p style="font-size:12px;color:#3397CD;letter-spacing:2px;margin-bottom:3px;">PROJECT EXTRAS</p>
														<p style="border-bottom:1px solid #fff; height:0; margin:0; color:#666;text-align:center;padding:0"></p>
														
														<p><span style="font-weight:bold;font-size:16px">Extras:</span> <br/><br/> '.$extras_list.'</p>
                                                        
                                                        
                                                      </div>
                                                            
                                                        </td>
                                                    </tr>
                                                    
                                                </tbody>
                                            </table>
                                            
                                        </td>
                                    </tr>
                                    
                                    <tr>
                                        <td style="background:#f9f9f9;border:1px solid #D8D8D8;border-top:none;padding:24px 10px" align="center">
                                            
                                            <table style="width:100%;max-width:650px" align="center">
                                                <tbody>
                                                    <tr>
                                                        <td style="font-size:20px;line-height:27px;text-align:center;max-width:650px">
                                                            <a href="'.$poweredby_url.'" style="text-decoration:none;color:#69696c" target="_blank">
                                                                <span style="color:#00ce00;font-weight:bold;max-width:180px">POWERED BY:</span> 
                                                                '.$poweredby_name.'
                                                            </a>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            
                                        </td>
                                    </tr>
                                    
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    
                    <tr>
                        <td>
                            <table style="max-width:650px" align="center">
                                <tbody>
                                    <tr>
                                        <td style="color:#b4b4b4;font-size:11px;padding-top:10px;line-height:15px;font-family:arial">
                                            <span> &copy; ELFLAIRE 2014 - '.$currYear.' - ALL RIGHTS RESERVED </span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
            </tbody>
        </table>
    </center>
</body>
</html>';
?>
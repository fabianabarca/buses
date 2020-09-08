function showTime(){
    let date = new Date();
    let h = date.getHours(); 
    let m = date.getMinutes(); 
    let s = date.getSeconds(); 
    let session = "AM";
    
    if(h == 0){
        h = 12;
    }        
    else if(h > 12){
        h = h - 12;
        session = "PM";
    }

    if((m == 00 || m == 15 || m == 30 || m == 45) && s == 00){
        location.reload();  // Recargar la página en estos minutos a cualquier hora
                            // y así tener los datos actualizados
                            // Mejor cambiarlo a algo como AJAX para no recargar toda la página 
    } 
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    let time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("DigitalCLOCK").innerText = time;
    setTimeout(showTime, 1000);
}

showTime();
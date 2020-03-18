var current_date = new Date();
var timer_finish;

function timer_start(finish){
    timer_finish = new Date(finish);
    next_second();
    setInterval(next_second, 1000);
}

function next_second(){
    current_date = new Date();
    var miliseconds = timer_finish.getTime()-current_date.getTime();
    if(miliseconds<0){
        widnow.location.reload();
    }
    var seconds=Math.floor((miliseconds/1000) % 60);
    var minutes = Math.floor(((miliseconds/1000)-seconds)/60 % 60);
    var hours = Math.floor(((((miliseconds/1000)-seconds)/60)-minutes)/60 % 24);
    var days = Math.floor((((((miliseconds/1000)-seconds)/60)-minutes)/60 - hours) / 24);
    document.getElementById("clock").innerHTML= days + " d " + hours + ":" + minutes + ":" + seconds;
}
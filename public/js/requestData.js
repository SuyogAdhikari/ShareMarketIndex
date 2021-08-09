fart = new Fart({
default_sound: farts.toot,
loop: false,
volume: 100
}); 

function sendNotification(){
    alert("Sorry, This feature is under construction");
    fart.play(farts.windy);
}
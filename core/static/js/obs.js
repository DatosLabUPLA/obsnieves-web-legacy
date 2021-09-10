var end = new Date('11/24/2020 3:15 PM');

var _second = 1000;
var _minute = _second * 60;
var _hour = _minute * 60;
var _day = _hour * 24;
var timer;

function showRemaining() {
    var now = new Date();
    var distance = end - now;
    if (distance < 0) {

        clearInterval(timer);
        document.getElementById('countdown').innerHTML = 'Empezó el Seminario! <a class="btn btn-danger blob" href="https://youtu.be/c0gQofRHoxg" target="_blank">Seminario en Vivo</a>';
        document.getElementById('countdown-pre').innerHTML = '';

        document.getElementById('countdown2').innerHTML = 'Empezó el Seminario! <a class="btn btn-danger blob" href="https://youtu.be/c0gQofRHoxg" target="_blank">Seminario en Vivo</a>';
        document.getElementById('countdown-pre2').innerHTML = '';

        return;
    }
    var days = Math.floor(distance / _day);
    var hours = Math.floor((distance % _day) / _hour);
    var minutes = Math.floor((distance % _hour) / _minute);
    var seconds = Math.floor((distance % _minute) / _second);

    document.getElementById('countdown').innerHTML = days + ' dias, ';
    document.getElementById('countdown').innerHTML += hours + ' horas, ';
    document.getElementById('countdown').innerHTML += minutes + ' minutos y ';
    document.getElementById('countdown').innerHTML += seconds + ' segundos';

    document.getElementById('countdown2').innerHTML = days + ' dias, ';
    document.getElementById('countdown2').innerHTML += hours + ' horas, ';
    document.getElementById('countdown2').innerHTML += minutes + ' minutos y ';
    document.getElementById('countdown2').innerHTML += seconds + ' segundos';
}

timer = setInterval(showRemaining, 1000);


// Javascript Image Zoom On Click
// Example of use
// <div class="value-img">
//   <img id="img-default" src="img/journey_start_thumbnail.jpg" data-action="zoom" data-original="img/journey_start.jpg"
//     alt="journey_start_thumbnail" />
// </div>
new Zooming().listen('img')


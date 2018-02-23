
var months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
var year = "2005"

var weekDays = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]


var date = new Date();
var current_year = date.getFullYear();
var current_month = date.getMonth();
var current_day = date.getDate();


// Month is 1-indexed (January is 1, February is 2, etc).
function daysInMonth (month, year) {
    return new Date(year, month, 0).getDate();
}

function print(s) {
    console.log(s);
}

function doubleDigit(n) {
    if (n.length == 1) {
        return '0' + n;
    }
    return n
}

function removeChilds(myNode) {
    while (myNode.lastChild) {
        myNode.removeChild(myNode.lastChild);
    }
}


function clickableDay(day) {
    day.addEventListener('click', function() {
        // daySelected(day);
        // save date
        document.getElementById('dateinput').value = makeDate(year, month + 1, day.innerHTML);
        // saveLastDate(day.innerHTML);
        // download(day);
        showModal();
    });
}

function getMonthName(n) {
    if (n < 0) {
        n = 12 + n;
    }
    if( n >= 12 ) {
        n = n - 12;
    }
    // print(n);
    // print('blabla');
    return months[n];
}

function postToUrl(path, params, method) {
    method = method || "post";

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}

function makeDate(year, month, day) {
    return year + '-' + month + '-' + day;
}

function blur(element, n) {
    element.style['-webkit-filter'] =  'blur(' + n + ')';
    element.style['-moz-filter'] =  'blur(' + n + ')';
    element.style['-o-filter'] =  'blur(' + n + ')';
    element.style['-ms-filter'] =  'blur(' + n + ')';
    element.style['filter'] =  'blur(' + n + ')';
}

function showModal() {
    // url = '/download-ppt';
    // date_string = makeDate(year, month + 1, day.innerHTML)
    // params = {date: date_string, title: 'Título'};
    // post_to_url(url, params, 'get');
    var modal = document.getElementById('myModal');
    modal.style.display = "block";
    var all = document.getElementById('all');
    blur(all, '8px');
}   


function makeCalendar(date, current) {

    year = date.getFullYear();
    month = date.getMonth();
    // day = date.getDate();
    document.getElementById("month").childNodes[0].nodeValue = getMonthName(month)//.toUpperCase()
    // document.getElementById("month").innerHTML = getMonthName(month)//.toUpperCase()
    document.getElementById("year").innerHTML = year

    var calendar = document.getElementById("calendar");



    var initialWeekday  = new Date(year, month, 1).getDay(); // to be changed to real date
    var numberDaysPastMonth = daysInMonth(month, year);
    // var a = 31;
    var numberDaysMonth = daysInMonth(month+1, year);

    var calendarHeaders = document.getElementById("calendar_headers");
    var calendar = document.getElementById("calendar");
    removeChilds(calendarHeaders);
    removeChilds(calendar);

    var firstWeek = document.createElement('div');
    firstWeek.classList.add('week');
    calendar.appendChild(firstWeek);

    // print(initialWeekday);
    // print(numberDaysPastMonth);
    // days of the past month
    var n = numberDaysPastMonth - initialWeekday + 1;
    var cont = 0;
    for( i = n + 1; i <= numberDaysPastMonth; i++ ) {
        var dayPastMonth = document.createElement("div");
        dayPastMonth.classList.add("day", "not_available");
        dayPastMonth.textContent = i;
        firstWeek.appendChild(dayPastMonth);
        // add the day_names and the dotted lines under them
        var weekDay = document.createElement("div");
        weekDay.classList.add("week_day");
        weekDay.innerHTML = weekDays[cont];
        var dottedLine = document.createElement("span");
        dottedLine.classList.add("dotted_line");
        weekDay.appendChild(dottedLine);
        calendarHeaders.appendChild(weekDay);
        // console.log('blablabla')
        cont++;
    }


    var week = firstWeek;
    var dayNumber = 1;
    var weekDay = initialWeekday;
    var i = 0;
    var reseted = false;
    
    var endGrid = false;
    while( endGrid === false ) {
        var dayMonth = document.createElement("div");
        dayMonth.classList.add("day");
        // var text = document.createElement("span");
        // dayMonth.appendChild(text)
        if ( !reseted ) {
            dayMonth.classList.add("day", "available");
            clickableDay(dayMonth);
        } else {
            dayMonth.classList.add("day", "not_available");
        }
        if( cont <= 6 ) {
            // add the day_names and the dotted lines under them
            var weekDay = document.createElement("div");
            weekDay.classList.add("week_day");
            weekDay.innerHTML = weekDays[cont];
            var dottedLine = document.createElement("span");
            dottedLine.classList.add("dotted_line_bold");
            weekDay.appendChild(dottedLine);
            calendarHeaders.appendChild(weekDay);
        }
        // current day of different color
        if ( month === current_month && dayNumber===current_day && year===current_year) {
            dayMonth.style.color = 'var(--main_color)';
            dayMonth.style.fontWeight = 'bold';
        }
        dayMonth.textContent = doubleDigit(dayNumber.toString());
        week.appendChild(dayMonth);
        dayNumber++;
        cont++;
        if( dayNumber > numberDaysMonth ) {
            dayNumber = 1;
            reseted = true;
        }

        if( cont % 7 === 0 ) {
            var week = document.createElement('div');
            week.classList.add('week');
            calendar.appendChild(week);
            i == 0;
            if( reseted ) {
                endGrid = true;
            }
        }
    }

}

        // console.log('ejeem')
// window.onload = makeCalendar;

function buttons() {
    inputElement = document.getElementById('past_month');
    inputElement.addEventListener('click', function() {
        month = date.getMonth() - 1;
        year = date.getFullYear();
        date = new Date(year, month, 1);
        makeCalendar(date, 0);
    });

    inputElement = document.getElementById('next_month');
    inputElement.addEventListener('click', function() {
        month = date.getMonth() + 1;
        year = date.getFullYear();
        date = new Date(year, month, 1);
        makeCalendar(date, 0);
    });
    // var span = document.getElementById("close");
    // span.addEventListener('click', function() {
    //     var modal = document.getElementById('myModal');
    //     modal.style.display = "none";
    //     var all = document.getElementById('all');
    //     blur(all, '0px');  
    // });
}

function daySelected(day) {
    var lastDaySelected = day;
    var days_available = document.getElementsByClassName("available");
    //Remove the past day selected
    for (var n = 0; n < days_available.length; n++) {
        if (days_available[n].classList.contains("selected")) {
            days_available[n].classList.remove("selected");
        }
    }
    //Add the selected class to the date
    // var day = document.getElementById(event.target.id);
    lastDaySelected.classList.add("selected");
    // lastDaySelected = event.target.id;
    //Add the value to the form-input
}

function saveLastDate(day) {
    var input = document.getElementById('dateinput');
    // var dateSelected = document.getElementById("date");
    // date_string = makeDate(year, month + 1, day.innerHTML)
    input.value = makeDate(year, month + 1, day);

    //Then show next step
    // let step2 = document.getElementsByClassName("step2")
    // for (i = 0; i < step2.length; i++) {
    //     step2[i].style.visibility = "visible";
    //     step2[i].style.opacity = "1";
// }
}

window.onload = function() {
    makeCalendar(date, 1);
    buttons();
};

window.onclick = function(event) {
    var modal = document.getElementById('myModal');
    if (event.target == modal) {
        var all = document.getElementById('all');
        blur(all, '0px');
        modal.style.display = "none";
    }
}


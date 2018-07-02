
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
        document.getElementById('dateinput').value = makeDate(year, month + 1, day.innerHTML);
        showModal();
    });
}

function getMonthName(n) {
    if( n < 0 ) {
        n = 12 + n;
    }
    if( n >= 12 ) {
        n = n - 12;
    }
    return months[n];
}

function postToUrl(path, params, method) {
    // Not used, but very useful function
    // example of use:
        // url = '/download-ppt';
        // date_string = makeDate(year, month + 1, day.innerHTML)
        // params = {date: date_string, title: 'Título'};
        // post_to_url(url, params, 'get');
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
    // n is a valid css measure (Ej: 5px, 2em)
    element.style['-webkit-filter'] =  'blur(' + n + ')';
    element.style['-moz-filter'] =  'blur(' + n + ')';
    element.style['-o-filter'] =  'blur(' + n + ')';
    element.style['-ms-filter'] =  'blur(' + n + ')';
    element.style['filter'] =  'blur(' + n + ')';
}

function showModal() {
    // shows the prompt asking for the ppt title
    var modal = document.getElementById('myModal');
    modal.style.display = "block";
    var all = document.getElementById('all');
    blur(all, '8px');
}   

function wrapperWeekDay(weekDay) {
    // moves the js days to our day index standard
    // 0 1 2 3 4 5 6 -> 6 0 1 2 3 4 6
    return (weekDay + 6) % 7

}
function makeCalendar(date, current) {

    year = date.getFullYear();
    month = date.getMonth();

    document.getElementById("month").childNodes[0].nodeValue = getMonthName(month)
    document.getElementById("year").innerHTML = year

    var calendar = document.getElementById("calendar");

    var initialWeekday  = new Date(year, month, 1).getDay(); // to be changed to real date
    var numberDaysPastMonth = daysInMonth(month, year);

    var numberDaysCurrentMonth = daysInMonth(month+1, year);

    var calendarHeaders = document.getElementById("calendar_headers");
    var calendar = document.getElementById("calendar");
    removeChilds(calendarHeaders);
    removeChilds(calendar);

    var firstWeek = document.createElement('div');
    firstWeek.classList.add('week');
    calendar.appendChild(firstWeek);

    // days of the past month
    var n = numberDaysPastMonth - wrapperWeekDay(initialWeekday);
    // this cont keep track of the number of days appended to the calendar
    let cont = 0;
    for( let i = n; i < numberDaysPastMonth; i++ ) {
        // add the days of the past month
        var dayPastMonth = document.createElement("div");
        dayPastMonth.classList.add("day", "not_available");
        dayPastMonth.textContent = i + 1;
        firstWeek.appendChild(dayPastMonth);
        // add the day_names and the dotted lines under them
        var weekDay = document.createElement("div");
        weekDay.classList.add("week_day");

        weekDay.innerHTML = weekDays[cont];

        var dottedLine = document.createElement("span");
        dottedLine.classList.add("dotted_line");
        weekDay.appendChild(dottedLine);
        calendarHeaders.appendChild(weekDay);
        cont += 1;
    }


    var week = firstWeek;
    var dayNumber = 1;
    // var weekDay = initialWeekday;
    var i = 0;
    var renderingMonth = month
    // reseted is true when the current months is appended completely
    var reseted = false;
    
    var endGrid = false;
    while( endGrid === false ) {
        var dayMonth = document.createElement("div");
        dayMonth.classList.add("day");
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
        if ( renderingMonth === current_month && dayNumber===current_day && year===current_year) {
            dayMonth.style.color = 'var(--main_color)';
            dayMonth.style.fontWeight = 'bold';
        }

        dayMonth.textContent = doubleDigit(dayNumber.toString());
        week.appendChild(dayMonth);

        dayNumber += 1;
        cont += 1;
        if( dayNumber > numberDaysCurrentMonth ) {
            dayNumber = 1;
            renderingMonth += 1;
            reseted = true;
        }

        if( cont % 7 === 0 ) {
            // end of the week
            var week = document.createElement('div');
            week.classList.add('week');
            calendar.appendChild(week);
            if( reseted ) {
                // if it is the new month and the week ends, we finish adding days
                endGrid = true;
            }
        }
    }

}



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

// function daySelected(day) {
//     // function not used yet
//     var lastDaySelected = day;
//     var days_available = document.getElementsByClassName("available");
//     //Remove the past day selected
//     for (var n = 0; n < days_available.length; n++) {
//         if (days_available[n].classList.contains("selected")) {
//             days_available[n].classList.remove("selected");
//         }
//     }
//     //Add the selected class to the date
//     // var day = document.getElementById(event.target.id);
//     lastDaySelected.classList.add("selected");
//     // lastDaySelected = event.target.id;
//     //Add the value to the form-input
// }

function saveLastDate(day) {
    var input = document.getElementById('dateinput');
    input.value = makeDate(year, month + 1, day);
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


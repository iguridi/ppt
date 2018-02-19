
var months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
var year = "2005"

var weekDays = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]


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
}

function clickableDay(day) {
    day.addEventListener('click', function() {
        download(day);
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

function post_to_url(path, params, method) {
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

function download(day) {
    url = '/download-ppt';
    date_string = makeDate(year, month + 1, day.innerHTML)
    params = {date: date_string, title: 'Título'};
    post_to_url(url, params, 'get');
}   


function makeCalendar(date, current) {

    year = date.getFullYear();
    month = date.getMonth();
    // day = date.getDate();

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

    document.getElementById("month").innerHTML = getMonthName(month)//.toUpperCase()
    document.getElementById("year").innerHTML = year
}

        // console.log('ejeem')
// window.onload = makeCalendar;

window.onload = function() {
    makeCalendar(date, 1);
    buttons();
    var i = document.createElement("img");
    i.src = "/download-ppt?date=2018-02-02";

};

// function makeCalendar(_, selectedMonth = "current") {


//     if (selectedMonth == "current") {
//         pastMonth.startWeekDay = firstDayMonth(month-1, year);
//         pastMonth.monthLength = daysInMonth(month-1, year); 
//         pastMonth.monthNumber = month - 1;

//         displayMonth.startWeekDay = firstDayMonth(month, year);
//         displayMonth.monthLength = daysInMonth(month, year);
//         displayMonth.monthNumber = month;
//     }
//     else if (selectedMonth == "next") {
//         pastMonth.startWeekDay = firstDayMonth(month, year);
//         pastMonth.monthLength = daysInMonth(month, year);
//         pastMonth.monthNumber = month;

//         displayMonth.startWeekDay = firstDayMonth(month+1, year),
//         displayMonth.monthLength = daysInMonth(month+1, year)
//         displayMonth.monthNumber = month + 1;


//     }
//     // setting month and year
//     document.getElementById("month_year").innerHTML = months[displayMonth.monthNumber] + ' ' + year

//     //Setting dates 
//     var daysContainer = document.getElementById("day_nums");
//     daysContainer.innerHTML = '';

//     var n = pastMonth.monthLength - displayMonth.startWeekDay + 2;// Days of the past month to show
//     var a = displayMonth.startWeekDay + n - 1;
//     //console.log(n)
//     for (i = n; i < a; i++) {
//         var dayPastMonth = document.createElement("div");
//         dayPastMonth.classList.add("day");
//         dayPastMonth.textContent = i;
//         daysContainer.appendChild(dayPastMonth);
//     }
//     for (i = 1; i <= displayMonth.monthLength; i++) {
//         var currentMonthDay = document.createElement("button");
//         currentMonthDay.setAttribute("id", i);
//         currentMonthDay.classList.add("day", "available");
//         currentMonthDay.addEventListener("click", daySelected);
//         currentMonthDay.textContent = i;
//         daysContainer.appendChild(currentMonthDay);
//     }
// };
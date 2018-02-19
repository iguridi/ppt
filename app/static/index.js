var date = new Date();
var year = date.getFullYear();
var month = date.getMonth();

//To back-end
function makeDate(day, m){
    realMonth = m + 1
    return year + '-' + realMonth + '-' + day;
}

//Front-end
var months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];

function daysInMonth(m, y) {
    if (m == 1){
        return new Date(y, m, 28).getDate();
    }
    return new Date(y, m, 0).getDate();
}


function firstDayMonth(m, y) {
    var dateObj = new Date();
    dateObj.setFullYear(y);
    dateObj.setMonth(m);
    dateObj.setDate(1);
    var first_day = dateObj.getDay();
    return first_day;
}

var pastMonth = new Object();
var displayMonth = new Object();

function makeCalendar(_, selectedMonth = "current") {
    if (selectedMonth == "current") {
        pastMonth.startWeekDay = firstDayMonth(month-1, year);
        pastMonth.monthLength = daysInMonth(month-1, year); 
        pastMonth.monthNumber = month - 1;

        displayMonth.startWeekDay = firstDayMonth(month, year);
        displayMonth.monthLength = daysInMonth(month, year);
        displayMonth.monthNumber = month;
    }
    else if (selectedMonth == "next") {
        pastMonth.startWeekDay = firstDayMonth(month, year);
        pastMonth.monthLength = daysInMonth(month, year);
        pastMonth.monthNumber = month;

        displayMonth.startWeekDay = firstDayMonth(month+1, year),
        displayMonth.monthLength = daysInMonth(month+1, year)
        displayMonth.monthNumber = month + 1;


    }
    // setting month and year
    document.getElementById("month_year").innerHTML = months[displayMonth.monthNumber] + ' ' + year

    //Setting dates 
    var daysContainer = document.getElementById("day_nums");
    daysContainer.innerHTML = '';

    var n = pastMonth.monthLength - displayMonth.startWeekDay + 2;// Days of the past month to show
    var a = displayMonth.startWeekDay + n - 1;
    //console.log(n)
    for (i = n; i < a; i++) {
        var dayPastMonth = document.createElement("div");
        dayPastMonth.classList.add("day");
        dayPastMonth.textContent = i;
        daysContainer.appendChild(dayPastMonth);
    }
    for (i = 1; i <= displayMonth.monthLength; i++) {
        var currentMonthDay = document.createElement("button");
        currentMonthDay.setAttribute("id", i);
        currentMonthDay.classList.add("day", "available");
        currentMonthDay.addEventListener("click", daySelected);
        currentMonthDay.textContent = i;
        daysContainer.appendChild(currentMonthDay);
    }
};

window.onload = makeCalendar;

function nextMonth() {
    makeCalendar('_', "next");
    //SHOW return button and HIDE    next button
    var nextButton = document.getElementById("next-month");
    nextButton.style.display = 'none';
    var previousButton = document.getElementById("previous-month");
    previousButton.style.display = 'inline-block';

}

function previousMonth() {
    makeCalendar('a', "current");
    //HIDE return button and SHOW next button
    var nextButton = document.getElementById("next-month");
    nextButton.style.display = 'inline-block';
    var previousButton = document.getElementById("previous-month");
    previousButton.style.display = 'none';
}

function daySelected(event) {
    var lastDaySelected;
    var days_available = document.getElementsByClassName("available");
    //Remove the past day selected
    for (var n = 0; n < days_available.length; n++) {
        if (days_available[n].classList.contains("selected")) {
            days_available[n].classList.remove("selected");
        }
    }
    //Add the selected class to the date
    var day = document.getElementById(event.target.id);
    day.classList.add("selected");
    lastDaySelected = event.target.id;
    //Add the value to the form-input
    var dateSelected = document.getElementById("date");
    dateSelected.value = makeDate(event.target.id, displayMonth.monthNumber, year);
    //Then show next step
    let step2 = document.getElementsByClassName("step2")
    for (i = 0; i < step2.length; i++) {
        step2[i].style.visibility = "visible";
        step2[i].style.opacity = "1";
    }
}

function displayCheckWarning() {
    var warning = document.getElementById("check-presentation-warning");
    warning.style.visibility = "visible";
    warning.style.opacity = "1";
}








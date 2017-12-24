function daysInMonth(month, year) {
    return new Date(year, month, 0).getDate() + 1;
}
var months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
function firstDayMonth(date, month, year) {
    var dateObj = new Date();
    dateObj.setFullYear(year);
    dateObj.setMonth(month);
    dateObj.setDate(1);
    var first_day = dateObj.getDay();
    return first_day;
}
var lastDaySelected;
window.onload = function makeCalendar() {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth();
    //Set set year
    var html_year = document.getElementById("month").innerHTML = year;
    //Setting month
    var html_month = document.getElementById("month").innerHTML = months[month];
    //Setting dates
    firstDay = firstDayMonth("1", month, year);
    var daysContainer = document.getElementById("day_nums");
    for (i = 28; i < firstDay + 27; i++) {
        var dayPastMonth = document.createElement("div");
        dayPastMonth.classList.add("day");
        dayPastMonth.textContent = i;
        daysContainer.appendChild(dayPastMonth);
    }
    month_length = daysInMonth(month, year);
    for (i = 1; i <= month_length; i++) {
        var currentMonthDay = document.createElement("button");
        currentMonthDay.setAttribute("id", i);
        currentMonthDay.classList.add("day", "available");
        currentMonthDay.addEventListener("click", daySelected);
        currentMonthDay.textContent = i;
        daysContainer.appendChild(currentMonthDay);
    }
};
function daySelected(event) {
    var days_available = document.getElementsByClassName("available");
    for (var n = 0; n < days_available.length; n++) {
        if (days_available[n].classList.contains("selected")) {
            days_available[n].classList.remove("selected");
            var day = document.getElementById(event.target.id);
            day.classList.add("selected");
            lastDaySelected = event.target.id;
            return;
        }
    }
    //Add the selected class to the date
    var day = document.getElementById(event.target.id);
    day.classList.add("selected");
    lastDaySelected = event.target.id;
    //Add the value to the form-input
    var dateSelected = document.getElementById("date");
    dateSelected.value = event.target.id;

    //Then show next step
    let step2 = document.getElementsByClassName("step2")
    for (i = 0; i < step2.length; i++) {
        step2[i].style.visibility = "visible";
        step2[i].style.opacity = "1";
    }

}

function titleSelected() {
    let titleInput = document.getElementById("title-input");
    if (titleInput.value === "") {
        window.alert("Es obligatorio escribir un título.")
    }
    else {
        let step3 = document.getElementsByClassName("step3")
        console.log(step3)
        for (i = 0; i < step3.length; i++) {
            step3[i].style.visibility = "visible";
            step3[i].style.opacity = "1";
        }
    }
    return false;
}

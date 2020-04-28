var months = [
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre",
];
var year = "2005";

var weekDays = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"];

var date = new Date();
var currentYear = date.getFullYear();
var currentMonth = date.getMonth();
var currentDay = date.getDate();

// Month is 1-indexed (January is 1, February is 2, etc).
function daysInMonth(month, year) {
  return new Date(year, month, 0).getDate();
}

function print(s) {
  console.log(s);
}

function doubleDigit(n) {
  if (n.length == 1) {
    return "0" + n;
  }
  return n;
}

function removeChilds(myNode) {
  while (myNode.lastChild) {
    myNode.removeChild(myNode.lastChild);
  }
}

function clickableDay(day) {
  day.addEventListener("click", function () {
    document.getElementById("dateinput").value = makeDate(
      year,
      month + 1,
      day.innerHTML
    );
    showModal();
  });
}

function getMonthName(n) {
  if (n < 0) {
    n = 12 + n;
  }
  if (n >= 12) {
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

  for (var key in params) {
    if (params.hasOwnProperty(key)) {
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
  return year + "-" + month + "-" + day;
}

function blur(element, n) {
  // n is a valid css measure (Ej: 5px, 2em)
  const blurGrade = "blur(" + n + ")";
  element.style["-webkit-filter"] = blurGrade;
  element.style["-moz-filter"] = blurGrade;
  element.style["-o-filter"] = blurGrade;
  element.style["-ms-filter"] = blurGrade;
  element.style["filter"] = blurGrade;
}

function showModal() {
  // shows the prompt asking for the ppt title
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
  var all = document.getElementById("all");
  blur(all, "8px");
}

function wrapperWeekDay(weekDay) {
  // moves the js days to our day index standard
  // 0 1 2 3 4 5 6 -> 6 0 1 2 3 4 6
  return (weekDay + 6) % 7;
}

function makeCalendar(date) {
  year = date.getFullYear();
  month = date.getMonth();

  document.getElementById("month").childNodes[0].nodeValue = getMonthName(
    month
  );
  document.getElementById("year").innerHTML = year;

  var calendar = document.getElementById("calendar");

  var calendarHeaders = document.getElementById("calendar_headers");
  var calendar = document.getElementById("calendar");
  removeChilds(calendarHeaders);
  removeChilds(calendar);

  var firstWeek = document.createElement("div");
  firstWeek.classList.add("week");
  calendar.appendChild(firstWeek);

  // days of the past month
  var numberDaysPastMonth = daysInMonth(month, year);
  var n =
    numberDaysPastMonth - wrapperWeekDay(new Date(year, month, 1).getDay());
  // this index keep track of the number of days added to the calendar

  let index = 0;
  for (let i = n; i < numberDaysPastMonth; i++) {
    // add the days of the past month
    addDayPastMonth(i);
    // add the day_names and the dotted lines under them
    const weekDay = document.createElement("div");
    addDayName(weekDay, index);
    addDottedLine(weekDay, "dotted_line");
    calendarHeaders.appendChild(weekDay);
    index += 1;
  }

  let week = firstWeek;
  let monthDay = 1;
  var renderingMonth = month;
  // monthEnd is true when the current month is appended completely
  let monthEnd = false;
  while (1) {
    const dayMonth = document.createElement("div");
    if (monthEnd) {
      dayMonth.classList.add("day", "not_available");
    } else {
      dayMonth.classList.add("day", "available");
      clickableDay(dayMonth);
    }

    if (index <= 6) {
      // add the day_names and the dotted lines under them
      const weekDay = document.createElement("div");
      addDayName(weekDay, index);
      addDottedLine(weekDay, "dotted_line_bold");
      calendarHeaders.appendChild(weekDay);
    }

    // current day of different color
    if (
      renderingMonth === currentMonth &&
      monthDay === currentDay &&
      year === currentYear
    ) {
      dayMonth.style.color = "var(--main_color)";
      dayMonth.style.fontWeight = "bold";
    }

    dayMonth.textContent = doubleDigit(monthDay.toString());
    week.appendChild(dayMonth);

    monthDay += 1;
    index += 1;
    const endCurrentMonth = monthDay > daysInMonth(month + 1, year);
    if (endCurrentMonth) {
      monthDay = 1;
      renderingMonth += 1;
      monthEnd = true;
    }

    const endWeek = index % 7 === 0;
    if (endWeek) {
      week = document.createElement("div");
      week.classList.add("week");
      calendar.appendChild(week);
    }
    if (monthEnd && endWeek) {
      // if it is the new month and the week ends, we finish adding days
      break;
    }
  }

  function addDayName(weekDay, index) {
    weekDay.classList.add("week_day");
    weekDay.innerHTML = weekDays[index];
    return weekDay;
  }

  function addDottedLine(weekDay, cssClass) {
    const dottedLine = document.createElement("span");
    dottedLine.classList.add(cssClass);
    weekDay.appendChild(dottedLine);
  }

  function addDayPastMonth(i) {
    var day = document.createElement("div");
    day.classList.add("day", "not_available");
    day.textContent = i + 1;
    firstWeek.appendChild(day);
  }
}

function buttons() {
  inputElement = document.getElementById("past_month");
  inputElement.addEventListener("click", function () {
    month = date.getMonth() - 1;
    year = date.getFullYear();
    date = new Date(year, month);
    makeCalendar(date);
  });

  inputElement = document.getElementById("next_month");
  inputElement.addEventListener("click", function () {
    month = date.getMonth() + 1;
    year = date.getFullYear();
    date = new Date(year, month);
    makeCalendar(date);
  });
}

window.onload = function () {
  year = date.getFullYear();
  month = date.getMonth();
  date = new Date(year, month);
  makeCalendar(date);
  buttons();
};

window.onclick = function (event) {
  var modal = document.getElementById("myModal");
  if (event.target == modal) {
    var all = document.getElementById("all");
    blur(all, "0px");
    modal.style.display = "none";
  }
};

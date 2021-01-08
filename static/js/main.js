function mainMenu() {
$('.dropdown-toggle').dropdown();
}

$(document).ready(function() {
  $("#myButton").click(function() {
    $("#myButton").after('<input type="text" id="textInput" value="">');
  });
});

$(document).ready(mainMenu);
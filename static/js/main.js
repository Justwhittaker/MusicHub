$(document).ready(function() {
$('.dropdown-toggle').dropdown();
});

$(document).ready(function() {
$('#dropdownCat').dropdown();
});

$(document).ready(function() {
  $("#myButton").click(function() {
    $("#myButton").after('<input type="text" id="textInput" value="">');
  });
});

$(document).ready(function() {
  $("#myButton2").click(function() {
    $("#myButton2").after('<input type="text" id="textInput" value="">');
  });
});

$(document).ready(mainMenu);


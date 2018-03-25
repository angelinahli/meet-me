$(document).ready(function() {
    $("#datepicker").datepicker();
  });


 var startdate = $(".start").datepicker("getDate()");
 console.log(startdate);
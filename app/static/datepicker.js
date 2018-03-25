$(document).ready(function() {
    $("#start").datepicker();
  });


 var startdate = $("#start").datepicker("getDate()");
 console.log(startdate);
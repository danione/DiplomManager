var steps = 1;

$(".next").click(function()
{
  $(".step-" + steps).css('display','none');
  steps++;
  $(".step-" + steps).css('display','block');
  if(steps == 4)
  {
    $(".next").css('display', 'none');
    $(".submit").css('display', 'block');
  }
});


$("#automatic").click(function() {
  $(".hide-seek").css('opacity', '0');
  $(".hide-seek").css('height', '0');
    if(this.checked)
    {
      $(".automatic-date").css('display', 'block');
      $(".manual-date").css('display', 'none');
      $(".step-"+steps).css('display','block');
    }
});

$("#manual").click(function() {
    $(".hide-seek").css('opacity', '0');
    $(".hide-seek").css('height', '0');
    if(this.checked)
    {
      $(".automatic-date").css('display', 'none');
      $(".manual-date").css('display', 'block');
    }
});

$( function() {
   $( "#datepicker" ).datepicker();
 } );

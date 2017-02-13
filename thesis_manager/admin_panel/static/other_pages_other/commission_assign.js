function exists(value, array)
{
  if(jQuery.inArray(value.val(),array) != -1)
    return true;
  return false;
}
$( function() {
   $( "#datepicker" ).datepicker(
     {
      dateFormat: "dd-mm-yy",
      onClose:function(date_selected)
      {
        if(date_selected)
        {
          if(jQuery.inArray(date_selected,dates) == -1)
            $(".date-selected").append("<div class=\"date-chosen\">" + date_selected + "<span class=\"delete\">X</span></div>")
        }
        $(this).val('');
      }
     });
 } );


  var dates = [];
  var people = [];
  $("body").on('click', '.date-chosen',function(){
    var value = $(this).html().split('<')[0];
    $("#datepicker").val(value);
    if(!exists($("#datepicker"), dates))
    {
      dates.push($("#datepicker").val());
      var day =
      {
        val: value,
        morning: true,
        afternoon: false
      }
      if(day.morning == true)
      {
        $("#check1").prop('checked', true);
      }

    }
  });

  $("body").on('click', '.delete',function(e){
    e.stopPropagation();
    data = this;
    dates = jQuery.grep(dates, function(value) {
      return value != $(data).parent().val().split('<')[0];
    });
    $(this).parent().remove();
    $("#datepicker").val('');
  });



 $(".member").autocomplete({
   source: members_
 });


 var steps = 0;
 var max_steps = parseInt($(".steps").children().last().attr('class').split('-')[1]);

 function hide_components()
 {
   $(".hide-seek").css('display', 'none');
   $(".section").css('display', 'none');
   $(".prev").css('display', 'inline');
 }

function update_value(value)
{
  $(value).css('display', 'inline');
  $(value).css('float', 'right');
  $(value).css('width','49%');
}

function fix_value(value)
{
  $(value).css('display', 'block');
  $(value).css('float', '');
  $(value).css('width','');
}


var current_selections = [];

 $(".next").click(function()
 {
   if(steps == 0)
   {
     var submitting = true;

    //  if(current_selections.length != $("#new-form .member").length)
    //  {
    //    $("#new-form .member").each(function()
    //    {
    //      if(!exists($(this),current_selections) && exists($(this), members_))
    //      {
    //        $(this).css('border-color','green');
    //        $('.error-msg').css('display', 'none');
    //        current_selections.push($(this).val());
    //      }
    //      else
    //      {
    //        $(this).css('border-color','red');
    //        $('.error-msg').css('display', 'inline');
    //        current_selections = [];
    //        submitting = false;
    //      }
    //    });
    //  }
     if(submitting)
     {

       if($("#Place").val())
       {
         if($("#automatic").is(":checked"))
         {
           $(".heading").css('color', '');
           steps++;
           update_value($(this));
           hide_components();
           $(".automatic-date").css('display', 'block');
           $(".manual-date").css('display', 'none');
           $(".step-"+steps).css('display','block');
         }
         else if($("#manual").is(":checked"))
         {
           $(".heading").css('color', '');
           hide_components();
           $(".automatic-date").css('display', 'none');
           $(".manual-date").css('display', 'block');
         }
         else
         {
           $(".heading").css('color', 'red');
         }
      }
      else
      {
        $("#Place").css('border-color', 'red');
      }

     }
   }
   else
   {
     $(".step-" + steps).css('display','none');
     steps++;
     $(".step-" + steps).css('display','block');
     if(steps == max_steps)
     {
       $(this).css('display', 'none');
       update_value($('.submit'));
     }
   }
 });

$(".prev").click(function()
{
  $(".step-" + steps).css('display','none');
  steps--;
  if( steps == 0)
  {
    $(".section").css('display', 'block');
    $(".hide-seek").css('display', 'block');
    fix_value($(".next"));
    $(this).css('display', 'none');
    return;
  }
  else if(steps == max_steps - 1)
  {
    fix_value($(".submit"));
    update_value($(".next"));
    $(".submit").css('display', 'none');
  }
  $(".step-" + steps).css('display','block');
});



$(".submit").click(function()
{
  $(this).closest("form").submit();
});

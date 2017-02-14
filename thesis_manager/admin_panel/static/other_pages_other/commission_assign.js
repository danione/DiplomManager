function exists(value, array)
{
  if(jQuery.inArray(value.val(),array) != -1)
    return true;
  return false;
}

var dates = [];



 $(".member").autocomplete({
   source: members_
 });


 var steps = 0;

 $( function() {
     $( ".datepicker" ).datepicker(
       {
        dateFormat: "dd-mm-yy",
        onClose:function(date_selected)
        {
          if(date_selected)
          {
            if(jQuery.inArray(date_selected,dates) == -1)
              $('.step-' + steps + ' > .date-selected').append("<div class=\"date-chosen\">" + date_selected + "<span class=\"delete\">X</span></div>");
          }
          $(this).val('');
        }
       });

  } );

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


function get_person(getter)
{
  return getter.parent().parent().attr('class').split('-')[1];
}

function exists_dict(value, array)
{
  var is_in_array = false;
  $.each(array,function(index,obj)
  {
    if(obj.val == value)
    {
      is_in_array = true;
      return false;
    }
  });
  if(is_in_array)
    return true;
  else
    return false;
}


var current_selections = [];
var people = [];

$("body").on('click', '.date-chosen',function(){
  var value = $(this).html().split('<')[0];
  // .closest
  var datepicker = $('#' + steps);
  datepicker.val(value);
  if(!exists_dict(datepicker.val(), dates))
  {
    var day =
    {
      val: value,
      morning: false,
      afternoon: false
      // person: current_selections[get_person($(this)) - 1]
    }

    dates.push(day.val);
  }
  else
  {
    var day = {};
    $.each(dates,function(index,obj)
    {
      if(obj.val == datepicker.val())
      {
        day =
        {
          val: obj.val,
          morning: obj.morning,
          afternoon: obj.afternoon
        }
        return false;
      }
    });
    widow.alert("hello");
    if(day.morning == true)
      $(this).parent().closest('.morning').prop('checked', true);
    else
      $(this).parent().closest('.morning').prop('checked', false);
    if(day.afternoon == true)
      $(this).parent().closest('.afternoon').prop('checked', true);
    else
      $(this).parent().closest('.afternoon').prop('checked', false);
  }
});

$(".morning").click(function()
{
  var value = $('#' + steps);

  $.each(dates, function(index, obj)
  {
    if(obj.val == value.val())
    {
      obj.morning = true;
      return false;
    }
  });
});

$(".afternoon").click(function()
{
  var value = $('#' + steps);

  $.each(dates, function(index, obj)
  {
    if(obj.val == value.val())
    {
      obj.afternoon = true;
      return false;
    }
  });
});

$("body").on('click', '.delete',function(e){
  e.stopPropagation();
  data = this;
  dates = jQuery.grep(dates, function(value) {
    return value.val != $(data).parent().val().split('<')[0];
  });
  $(this).parent().remove();
  $(".datepicker").val('');
  window.alert(dates);
});



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
    //   }
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


$(document).ready(function(){


  if($("#document tr").length == 1)
  {
    $(".document").css('display', 'none');
    $("#document-header").css('display', 'none');
  }

  if($("#assignment tr").length == 1)
  {
    $("#assignment-header").css('display', 'none');
    $(".assignment").css('display', 'none');

  }

  if($("#reviewer tr").length == 1)
  {
    $(".reviewer").css('display', 'none');
    $("#reviewer-header").css('display', 'none');
  }

  if($("#commission tr").length == 1)
  {
    $(".commission").css('display', 'none');
    $("#commission-header").css('display', 'none');
  }

});

var clicked = false;
$('body').on('click','img',function()
{
  var name = "#" + $(this).attr('class') + "-search";
  if(!clicked)
  {
    $(name).css('width', '7em');
    $(name).css('padding-left', '0.5em');
    clicked = true;
  }
  else
  {
    $(name).css('width', '0');
    $(name).css('padding-left', '0');
    clicked = false;

  }
});


function filter_function(element)
{
  var current_value_element = $(element).val().toLowerCase();
  var current
  var current_id = $(element).attr('id');
  var table_id = "#" + current_id.split('-')[0];
  var is_first = true;
  $(table_id).find(' > tbody > tr').each(function()
  {
    if (is_first)
    {
      is_first = false;
      return true;
    }
    else
    {
      var td = $(this).find("td");
      if(td.html().toLowerCase().indexOf(current_value_element) > -1)
      {
        $(this).show();
      }
      else
      {
        $(this).hide();
      }
    }
  });

}

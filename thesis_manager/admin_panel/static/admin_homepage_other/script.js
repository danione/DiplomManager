
$(document).ready(function(){


  if($("#document tr").length > 1)
  {
    $(".document-search").css('display', 'inline-block');
    $(".document").css('display', 'table');
    $("#document-header").css('display', 'block');
  }

  if($("#assignment tr").length > 1)
  {
    $(".assignment-search").css('display', 'inline-block');
    $(".assignment").css('display', 'table');
    $("#assignment-header").css('display', 'block');
  }

  if($("#documentation tr").length > 1)
  {
    $(".documentation-search").css('display', 'inline-block');
    $(".documentation").css('display', 'table');
    $("#documentation-header").css('display', 'block');
  }

  if($("#reviewer tr").length > 1)
  {
    $(".reviewer-search").css('display', 'inline-block');
    $(".reviewer").css('display', 'table');
    $("#reviewer-header").css('display', 'block');
  }

  if($("#commission tr").length > 1)
  {
    $(".commission-search").css('display', 'inline-block');
    $(".commission").css('display', 'table');
    $("#commission-header").css('display', 'block');
  }

});

var clicked;
$('body').on('click','img',function()
{
  var name = "#" + $(this).attr('class');
  if(clicked != name)
  {
    $('.hide').css('height', '0');
    $(name).css('width', '7em');
    $(name).css('padding-left', '0.5em');
    $(clicked).css('width', '0');
    $(clicked).css('padding-left', '0');
    clicked = name;
  }
  else
  {
    $(name).css('width', '0');
    $(name).css('padding-left', '0');
  }
});


function filter_function(element)
{
  var current_value_element = $(element).val().toLowerCase();
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

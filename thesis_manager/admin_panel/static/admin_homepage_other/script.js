
$(document).ready(function(){

  function display(name)
  {
    var id = "#" + name;
    var class_ = "." + name;
    if($(id + " tr").length > 1)
    {
      $(id + "-pointer").css('display', "inline-block");
      $(class_ + "-search").css('display', 'inline-block');
      $(class_).css('display', 'inline-table');
      $(id + "-header").css('display', 'block');
    }
  }
  $("table").each(function(index, object)
  {
    if(index % 2 != 0)
    {
      display($(object).attr('id'));
    }

  });
});

var clicked;
$('body').on('click','img',function()
{
  var name = "#" + $(this).attr('class');
  if(clicked != name)
  {
    $(name).css('width', '7em');
    $(name).css('margin-right', '0.2em')
    $(name).css('padding-left', '0.5em');
    $(clicked).css('width', '0');
    $(clicked).css('padding-left', '0');
    clicked = name;
  }
  else
  {
    $(name).css('width', '0');
    $(name).css('padding-left', '0');
    $(name).css('margin-right', '0');
    clicked = "";
  }
});


function filter_function(element)
{
  var current_value_element = $(element).val().toLowerCase();
  var current_id = $(element).attr('id');
  var table_id = "#" + current_id.split('-')[0];
  var is_first = true;
  $(table_id + ' tbody tr').each(function()
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
  });
}

$('.pointer').click(function()
{
  var value = $(this).css('transform');
  if( value != "none")
  {
    var values = value.split('(')[1].split(')')[0].split(',');
    var a = values[0];
    var b = values[1];
    var angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
    angle -= 180;
    if(angle < 0)
    {
      angle += 360;
    }
    value = angle;
  }
  else
    value = 180;
  $(this).css('-webkit-transform', 'rotate('+ value +'deg)');
  $(this).css('-moz-transform', 'rotate('+ value +'deg)');
  $(this).css('-ms-transform', 'rotate('+ value +'deg)');
  $(this).css('-o-transform', 'rotate('+ value +'deg)');
  $(this).css('transform', 'rotate('+ value +'deg)');


  var table = "#" + $(this).attr('id').split('-')[0];
  $(table + ' thead').parent().next('div').slideToggle();
});

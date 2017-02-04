var previous;
var previous_content;
var has_previous = false;

function click_change(content, prev, previous)
{
  $(content).css('background-color', '#fff');
  $(content).css('color', '#002240');
  $(content).css('border','1px solid #002240');
  if(!prev)
    return true;
  else
  {
    $(previous).css('background-color', '#002240');
    $(previous).css('color', '#fff');
    $(previous).css('border','1px solid black');
  }
  return true;
}

function find_name(current_name)
{
  var done = false;
  var current = "." + current_name;
  while(!done)
  {
      if($(current).parent().attr('id'))
      {
        done = true;
        return $(current).parent().attr('id').toLowerCase();
      }
      else
        current = $(current).parent().get(0).tagName;
  }
}

$(".table td").click(function()
  {
    if(has_previous)
    {
      $(previous_content).css('visibility', 'hidden');
      $(previous_content).css('opacity', '0');
    }
    content = this;
    has_previous = click_change(content, has_previous, previous);

    var current_class = $(this).children().attr('class');
    var appearing_content = "." + current_class + "-" + find_name(current_class);
    $(appearing_content).css('visibility', 'visible');
    $(appearing_content).css('opacity', '1');
    previous = content;
    previous_content = appearing_content;
  }
);

var has_previous_vol_2 = false;
var previous_vol_2;

$(".simple-table td").click(function()
{
  $(this).addClass('selected').siblings().removeClass('selected');
  $(this).css('background-color', '#002240');
  $(this).css('color', '#fff');
  if(!has_previous_vol_2)
    has_previous_vol_2 = true;
  else
  {
    $(previous_vol_2).css('background-color', '#fff');
    $(previous_vol_2).css('color', '#002240');
  }
  previous_vol_2 = this;
});

$(".submit").click(function()
{
  $.validate({
    modules : 'file'
  });
  var error_naming = false;
  if($(this).closest("form").attr('id') == 'not-simple-form')
  {
    $(".hide").val($('.selected').html());
  }
  else if($(this).closest("form").attr('id') == 'saving-form')
  {
    $("#not-simple-form td").each(function()
    {
      if($(this).html().split(".")[0] == $('#SaveYear').val())
      {
        error_naming = true;
        $(".error_msg").css('display', 'inline')
        return
      }
    });
  }
  if( error_naming == false)
    $(this).closest("form").submit();
});

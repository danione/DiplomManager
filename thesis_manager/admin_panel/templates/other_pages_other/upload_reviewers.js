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


$(".table td").click(function()
{
  if(has_previous)
  {
    $(previous_content).css('visibility', 'hidden');
    $(previous_content).css('opacity', '0');
  }
  content = this;
  has_previous = click_change(content, has_previous, previous);

  var appearing_content ="." + $(this).children().attr('class') + "-a-reviewer";
  $(appearing_content).css('visibility', 'visible');
  $(appearing_content).css('opacity', '1');
  previous = content;
  previous_content = appearing_content;
});

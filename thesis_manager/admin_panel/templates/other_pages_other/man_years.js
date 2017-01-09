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

  var appearing_content ="." + $(this).children().attr('class') + "-a-year";
  $(appearing_content).css('visibility', 'visible');
  $(appearing_content).css('opacity', '1');
  previous = content;
  previous_content = appearing_content;
});


$(".submit").click(function()
{
  if(!$("#year").val())
  {
    $("#year").css('border', '1px solid red');
  }
  else
  {
    $("#year").css('border', '1px solid black');
    $("#year").val("");
  }
});

 var has_previous_vol_2 = false;
 var previous_vol_2;


$(".simple-table td").click(function()
{
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

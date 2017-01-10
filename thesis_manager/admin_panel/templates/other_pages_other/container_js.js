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

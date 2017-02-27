var clicked = null;

$(".simple-table td").click(function()
{
  $('.load-field').val($(this).attr('id'));
  clicked = true;
});


$(".submit-load").click(function()
{
  if(clicked != null)
    $(this).closest("form").submit();
});

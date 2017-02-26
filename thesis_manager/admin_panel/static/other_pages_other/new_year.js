$(".tick").click(function()
{
  $.validate();
  $(this).closest('form').submit();
});

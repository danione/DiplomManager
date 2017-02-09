$(".submit-thesis").click(function()
{
  $.validate({
    modules : 'file'
  });

  if(jQuery.inArray($("#ThesisDescription").val(),thesis_topics) == -1)
    $(this).closest("form").submit();
});



$("#Supervisor").autocomplete({
    source: supervisors
});

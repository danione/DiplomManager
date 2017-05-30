$(".thesis").autocomplete({
  source: thesis_topics,
  minLength: 0
}).bind('focus', function(){ $(this).autocomplete("search"); } );

function exists(value, array)
{
  if(jQuery.inArray(value.val(),array) != -1)
    return true;
  return false;
}

var current_selections = [];

$(".submit-standard").click(function()
{
  var submitting = true;

  if(current_selections.length != $("#standard-form .thesis").length)
  {
    $("#standard-form .thesis").each(function()
    {
      if(!exists($(this),current_selections) && exists($(this), thesis_topics))
      {
        $(this).css('border-color','green');
        $('.error-msg').css('display', 'none');
        current_selections.push($(this).val());
      }
      else
      {
        $(this).css('border-color','red');
        $('.error-msg').css('display', 'inline');
        current_selections = [];
        submitting = false;
      }
    });
  }

  if(submitting)
  {
    $.validate();
    $(this).closest("form").submit();
  }

});

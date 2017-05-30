$(".tick").click(function()
{
  $.validate();
  $(this).closest('form').submit();
});

$('form').submit(function(e){

  $.post('/admin_panel/graduate/', $(this).serialize(), function(data){
    var parser = $.parseJSON(data);
    if(parser.message == 'Success')
    {
      $(".message").css('color', 'green');
      window.location.replace("/admin_panel");

    }
    $('.message').html(parser.message);
  });
  e.preventDefault();

});

// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


$('form').submit(function(e){
    $.post('/auth', $(this).serialize(), function(data){
      var parser = $.parseJSON(data);
      if(parser.message == 'Success')
        window.location.replace("/admin_panel");
      $('.message').html(parser.message);
    });
    e.preventDefault();
});

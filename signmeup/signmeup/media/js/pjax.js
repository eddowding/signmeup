// $(document).pjax('a[data-pjax]')



// Validators

jQuery.validator.addMethod("postcode", function(value, element) { 
  return checkPostCode(value)
}, "Please enter a valid UK postcode");


$("#postcode_form input").labelify({text: "label"});
// $("#join1010 form label").css({display: "none"});
$("#postcode_form").validate({
    rules: {
        postcode: {
            required: true,
            postcode: true
        }
    },
    submitHandler: function(form) {
        $('#top_layer').fadeOut(500, function() {
            $.pjax({
              url: '/postcode/' + $('#id_postcode').val() + '/',
              container: '#content',
            })
        })
        return false
    }
});

function handle_pjax(t, e) {
    postcode = $(t).find('#id_postcode').val()
    if (postcode) {
        // We have a postcode, we can move the map
        move_to_postcode(postcode)
    }

    home = $(t).find('body#home')
    if (home) {
        setHomeView();
    }
}

$(document).on('pjax:beforeSend', function(e) { handle_pjax(this, e) })
$(document).on('pjax:end', function(e) {     $('#top_layer').fadeIn(500) })







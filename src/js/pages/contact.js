//
// Contact Form Js
//

const { reset } = require("browser-sync");


function validateForm() {
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    var comments = document.forms["myForm"]["comments"].value;
    document.getElementById("error-msg").style.opacity = 0;
    document.getElementById('error-msg').innerHTML = "";
    if (name == "" || name == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-danger error_message'><i  data-feather='home' class='icon-sm align-middle me-2'></i> Please enter a name</div>";
        fadeIn();
        return false;
    }
    else if (email == "" || email == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-danger error_message'><i  data-feather='alert-triangle' class='icon-sm align-middle me-2'></i> Please enter a email</div>";
        fadeIn();
        return false;
    }
    else if (comments == "" || comments == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-danger error_message'><i class='mdi mdi-alert'></i> Please enter a Message</div>";
        fadeIn();
        return false;
    }

    else{
        document.getElementById("submit").disabled = true;
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-success error_message'>Your Message sent successfully.</div>";
        fadeIn();
    }
}
function fadeIn() {
    var fade = document.getElementById("error-msg");
    var opacity = 0;
    var intervalID = setInterval(function () {
        if (opacity < 1) {
            opacity = opacity + 0.5
            fade.style.opacity = opacity;
        } else {
            clearInterval(intervalID);
        }
    }, 200);
}
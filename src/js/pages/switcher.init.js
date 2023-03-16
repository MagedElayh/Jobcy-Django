//
/********************* Swicher js ************************/
//

function toggleSwitcher() {
  var i = document.getElementById("style-switcher");
  if (i.style.left === "-165px") {
    i.style.left = "-0px";
  } else {
    i.style.left = "-165px";
  }
}

function setColor(theme) {
  document.getElementById('bootstrap-style').href = '../static/css/bootstrap-' + theme + '.min.css';
  document.getElementById('app-style').href = '../static/css/app-' + theme + '.min.css';
  window.localStorage.removeItem('color');
  window.localStorage.setItem("color", theme);
};

function setColorGreen() {
  document.getElementById('bootstrap-style').href = '../static/css/bootstrap.min.css';
  document.getElementById('app-style').href = '../static/css/app.min.css';

};

// Set Default  Color
defaultColor();
function defaultColor(e) {
    if (window.localStorage.getItem('color') == null) {
        color = 'green'
    }else{
        color = window.localStorage.getItem('color');
    }
    if (color == 'green'){
      document.getElementById('bootstrap-style').href = '../static/css/bootstrap.min.css';
      document.getElementById('app-style').href = '../static/css/app.min.css';
    }
    else{
      document.getElementById('bootstrap-style').href = '../static/css/bootstrap-' + color + '.min.css';
      document.getElementById('app-style').href = '../static/css/app-' + color + '.min.css';
    }
};

// Set Default Mode
defaultMode();
function defaultMode(e) {
    if (window.localStorage.getItem('mode') == null) {
        var mode = 'light'
    }else{
        var mode = window.localStorage.getItem('mode');
    }
​
​
    if (mode == "light") {
      document.body.removeAttribute("data-layout-mode");
      localStorage.setItem("theme", "light");
    }else{
      document.body.setAttribute("data-layout-mode", "dark");
      localStorage.setItem("theme", "dark");
    }    
}
//
/********************* light-dark js ************************/
//

var btn = document.getElementById("mode");
btn.addEventListener("click", function (e) {
  var theme = localStorage.getItem("theme");
  if (theme == "light" || theme == "") {
    document.body.setAttribute("data-layout-mode", "dark");
    localStorage.setItem("theme", "dark");
    window.localStorage.removeItem('mode');
    window.localStorage.setItem("mode", 'dark');
  } else {
    document.body.removeAttribute("data-layout-mode");
    localStorage.setItem("theme", "light");
    window.localStorage.removeItem('mode');
    window.localStorage.setItem("mode", 'light');
  }
});

//
/********************* scroll top js ************************/
//

var mybutton = document.getElementById("back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

//
/********************* Page Load js ************************/
//

var preloader = document.getElementById("preloader");

window.addEventListener("load", function () {
  preloader.style.opacity = "0";
  preloader.style.visibility = "hidden";
});

// Favourite btn
var favouriteBtn = document.getElementsByClassName("bookmark-btn");
for (var i = 0; i < favouriteBtn.length; i++) {
  var favouriteBtns = favouriteBtn[i];
  favouriteBtns.onclick = function () {
    favouriteBtns.classList.toggle("active");
  };
}
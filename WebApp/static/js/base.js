function settingdropdown() {
  document.getElementById("setting-dropdown").classList.toggle("set-show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.setting-class')) {
    var set_dropdowns = document.getElementsByClassName("setting-dropdown-content");
    var i;
    for (i = 0; i < set_dropdowns.length; i++) {
      var openDropdown = set_dropdowns[i];
      if (openDropdown.classList.contains('set-show')) {
        openDropdown.classList.remove('set-show');
      }
    }
  }
}

function notifdropdown() {
  document.getElementById("notif-dropdown").classList.toggle("not-show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.notif-class')) {
    var not_dropdowns = document.getElementsByClassName("notif-dropdown-content");
    var j;
    for (i = 0; i < not_dropdowns.length; i++) {
      var openDropdown = not_dropdowns[i];
      if (openDropdown.classList.contains('not-show')) {
        openDropdown.classList.remove('not-show');
      }
    }
  }
}
document.getElementById("myBtn").addEventListener("click", toggleNav());
function toggleNav() {
  navSize = document.getElementById("mySidenav").style.width;
  if (navSize === 250) {
    document.getElementById('mySidenav').style.width = '0px';
  }
  else {
    document.getElementById('mySidenav').style.width = '250px';
  }
}

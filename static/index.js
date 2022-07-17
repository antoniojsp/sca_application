    var input = document.querySelector("#telephone");
    window.intlTelInput(input, {utilsScript: "build/js/utils.js",
    });

   function showStuff(element) {
      var el = document.getElementById(element);
      if (el.style.display === "none") {
        el.style.display = "block";
      } else {
        el.style.display = "none";
      }
    }
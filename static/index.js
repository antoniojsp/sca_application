   function showStuff(element) {
      var el = document.getElementById(element);
      if (el.style.display === "none") {
        el.style.display = "block";
      } else {
        el.style.display = "none";
      }
    }

    function hide_if_selected(input, hide, option){
        var elem = document.getElementById(hide);
        if(input == option){
            elem.style.display = "None";
        }else{
            elem.style.display = "block";
        }
    }

    function show_if_selected(input, hide, option){
        var element = document.getElementById(hide);
        if(input != option){
            element.style.display = "None";
        }else{
            element.style.display = "block";
        }
    }
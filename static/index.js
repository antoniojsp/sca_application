   function showStuff(element) {
      var el = document.getElementById(element);
      if (el.style.display === "none") {
        el.style.display = "block";
      } else {
        el.style.display = "none";
      }
    }

    function hide_if_selected(selection, element_to_hide, if_selected){
        var elem = document.getElementById(element_to_hide);
        if(selection == option){
            elem.style.display = "None";
        }else{
            elem.style.display = "block";
        }
    }

    function show_if_selected(selection, element_to_hide, if_selected){
        var element = document.getElementById(element_to_hide);
        if(selection != option){
            element.style.display = "None";
        }else{
            element.style.display = "block";
        }
    }

    function current_date(){
        console.log("hola");
        const dateInput = document.getElementById('today_date');
        dateInput.value = new Date().toISOString().split('T')[0];
//        var one_minute = 60000; //to set to default  the min input  time to the current time plus one minute
//        var diff_hours_to_utc = (new Date()).getTimezoneOffset() * one_minute;
//        var localISOTime = (new Date(Date.now() - diff_hours_to_utc + one_minute)).toISOString().slice(0, -1);
//        const dateInput = today_date;
//        dateInput.min = localISOTime.split('.')[0].slice(0, -3);
//        dateInput.value = localISOTime.split('.')[0].slice(0, -3);
    };
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
        if(selection != if_selected){
            element.style.display = "None";
        }else{
            element.style.display = "block";
        }
    }

    function current_date(){
        $("#today_date").val(new Date().toISOString().split('T')[0]);
    };

$(document).ready ( function () {
    $('.btnNext').click(function(){
        console.log($('.nav-tabs > .active').next('li').find('a'))
      $('.nav-tabs > .nav-item > .active').parent().next('li').find('a').trigger('click');
    });


     $('.btnPrevious').click(function(){
     console.log("dfd")
      $('.nav-tabs > .nav-item > .active').parent().prev('li').find('a').trigger('click');
    });

    });

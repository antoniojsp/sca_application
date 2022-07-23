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

        console.log(selection)

        if(selection == if_selected){
            elem.style.display = "None";
        }else{
            elem.style.display = "block";
        }
    }

    function show_if_selected(selection, element_to_hide, if_selected){
        var element = document.getElementById(element_to_hide);

                console.log(selection)


        if(selection != if_selected){
            element.style.display = "None";
        }else{
            element.style.display = "block";
        }
    }

   function current_date(){
        var year = new Date().getYear() + 1900;

        $("#move_in_year").attr({
           "min" : year,        // substitute your own
           "value" : year          // values (or variables) here
        });

        $("#today_date").val(new Date().toISOString().split('T')[0]);
    };

// Previous and Next buttons
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


$(document).ready ( function () {
    $('#submit_form').click(function(){

       var classes = ['cover', 'agreement']
       var cover = document.getElementsByClassName('cover');
       var agreement = document.getElementsByClassName('agreement');


       var information_package = {}
       for (let i = 0; i < cover.length; i++) {
          information_package[cover[i].id] = cover[i].value
        }

        console.log(information_package)
//
//
//
//        var submit_data = {"data":JSON.stringify(information_package)}
//            $.getJSON( "/_submit",
//                submit_data,
//                function(data) {
//                }
//             );
    });
});



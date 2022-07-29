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

        var date = new Date().toISOString().split('T')[0];
        $("#today_date").attr({
           "min" : date,        // substitute your own
           "value" : date          // values (or variables) here
        });


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

function input_dict(name){
    var information_package = {}
    var cover = document.getElementsByClassName(name);

    for (let i = 0; i < cover.length; i++) {
      if (cover[i].type == "checkbox"){
        information_package[cover[i].id] = cover[i].checked
      }else{
        information_package[cover[i].id] = cover[i].value
      }
    }

    return information_package
};

$(document).ready ( function () {
    $('#submit_form').click(function(){

       var classes = ['cover', 'agreement', "checklist", 'form-control personal', "essay", "auto", "range", "reference"]

        var data_dict = {}

        for (var i = 0; i<classes.length; i++){
            data_dict[classes[i]] = input_dict(classes[i])
        }

        var alarma = ""

//        cover tab
        if (data_dict['cover'].full_name == ""){
            alarma += "Missing Full name\n";
        }
        if (data_dict['cover'].today_date == ""){
            alarma += "Missing Today's date\n";
        }

//        agreement tab
        for ( i in data_dict['agreement']){
            if (data_dict['agreement'][i] == ""){
                alarma += "Check initials (Agreement Terms' tab)\n"
                break
            }
        }

//        personal information tab
   // essay tab

        for (i in data_dict['essay']){
            console.log(data_dict['essay'][i])
        }

        if (alarma != ""){
            alert(alarma);
        }

        var submit_data = {"data":JSON.stringify(data_dict)}

            $.getJSON( "/_submit",
                submit_data,
                function(data) {
                }
             );
    });
});



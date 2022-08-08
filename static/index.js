function showStuff(element, attr_list) {
      var el = document.getElementById(element);

      if (el.style.display === "none") {
        el.style.display = "block";
        change_attr(attr_list, true);
      } else {
        el.style.display = "none";
        change_attr(attr_list, false);
      }
};

function change_attr(attr_list, new_attr){
        for (var i = 0; i < attr_list.length; i++){
            var el = document.getElementById(attr_list[i])
            el.required = new_attr;
    }
};

// for type of student section
function hide_if_selected(selection, element_to_hide, if_selected){
        var elem = document.getElementById(element_to_hide);

        if(selection == if_selected){
            elem.style.display = "None";
        }else{
            elem.style.display = "block";
        }
    }
//for where you hear from us section
function show_if_selected(selection, element_to_show, if_selected){
        var element = document.getElementById(element_to_show);
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
// creates dictionary that needs to be checked by js it is legal before being sent to the backend
function input_dict(name){
    var information_package = {}
    var cover = document.getElementsByClassName(name);

    for (let i = 0; i < cover.length; i++) {

      if (cover[i].type == "checkbox"){
        information_package[cover[i].id] = [cover[i].checked, cover[i].required]
      }else{
        information_package[cover[i].id] = [cover[i].value, cover[i].required]
      }
    }

    return information_package
};
// checks if all the data needed us complete, if not, creates a string with the data missing
function check_inputs(data_dict, tab, message){
        for ( i in data_dict[tab]){
            if (data_dict[tab][i] == ""){
                return message + "\n"
            };
        };

        return ""
};
$(document).ready (function (){
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
    $('#submit_form').click(function(){

       var classes = ['cover', 'agreement', "checklist", 'form-control personal', "essay", "auto", "range", "reference"]
//
        var data_dict = {}

        for (var i = 0; i<classes.length; i++){
            data_dict[classes[i]] = input_dict(classes[i]);
        }


           console.log(data_dict['form-control personal'])
//        var cover = data_dict['cover']
//
//
//        var alarma = "";
//
//        alarma += check_inputs(data_dict, classes[0], "Check cover page tab");
//        alarma += check_inputs(data_dict, classes[1], "Check agreement tab");
//
//        var personal = data_dict['form-control personal'];
//        console.log(personal.full_legal_name);
//
//
//        alarma += check_inputs(data_dict, classes[4], "Check essay tab");
//        alarma += check_inputs(data_dict, classes[5], "Check essay tab");
//
//
//        if (alarma != ""){
//            alert(alarma);
//
//        }
//
//        var submit_data = {"data":JSON.stringify(data_dict)}

//            $.getJSON( "/_submit",
//                submit_data,
//                function(data) {
//                console.log("Data sent")
//                }
//             );
    });
});



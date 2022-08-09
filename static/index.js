//hides or show blocks with extra inputs in the page and changes attributes to those extra inputs from "required" input or back.
function show_hide_extra_inputs(element, attr_list) {
      var el = document.getElementById(element);
      if (el.style.display === "none") {
        el.style.display = "block";
        change_required_attributes(attr_list, true);
      } else {
        el.style.display = "none";
        change_required_attributes(attr_list, false);
      }
};
function change_required_attributes(attr_list, new_attr){
        for (var i = 0; i < attr_list.length; i++){
            var el = document.getElementById(attr_list[i])
            el.required = new_attr;
    }
};
// for type of student section
function hide_if_selected(selection, element_to_hide, if_selected, attr_list){
        var elem = document.getElementById(element_to_hide);

        if(selection != if_selected){
            elem.style.display = "block";
            change_required_attributes(attr_list, true);
        }else{
            elem.style.display = "none";
            change_required_attributes(attr_list, false);
        }
    }
//for where you hear from us section
function show_if_selected(selection, element_to_show, if_selected, attr_list){
        var element = document.getElementById(element_to_show);
        if(selection == if_selected){
            element.style.display = "block";
            change_required_attributes(attr_list, true);
        }else{
            element.style.display = "none";
            change_required_attributes(attr_list, false);
        }
    }
function highlight_missing_input(data_dict){

    var is_data_missing = false
    for( var i = 0; i<data_dict.length; i++){
        if (data_dict[i][1] == false){
            var elem = document.getElementById(data_dict[i][0]);
            elem.style.background="yellow";
            is_data_missing = true;
        }
    }

    return is_data_missing
};
function clean_all_inputs(data_dict){
    for( var i = 0; i<data_dict.length; i++){
        var elem = document.getElementById(data_dict[i][0]);
        elem.style.background="white";
        elem.value= "";
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
function check_inputs(data_dict){
    var missing_input = []
    for (var i = 0; i < data_dict.length; i++){
        for (let j in data_dict[i]){
            var input_value = data_dict[i][j][0]
            var is_required = data_dict[i][j][1]
            if (input_value == "" && is_required == true){
                missing_input.push([j, false]);
            }else{
                missing_input.push([j, true]);

            }
        }
    };

    return missing_input
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
        var data_dict = []
        var submit_dictionary = {}
        for (var i = 0; i<classes.length; i++){
            data_dict.push(input_dict(classes[i]));
            submit_dictionary[classes[i]] = input_dict(classes[i])
        }

        var missing_data = check_inputs(data_dict);

        if (highlight_missing_input(missing_data)){
            console.log("vacio")
            return
        }

        var submit_data = {"data":JSON.stringify(submit_dictionary)}

            $.getJSON( "/_submit",
                submit_data,
                function(data) {
                console.log("Data sent")
                clean_all_inputs(missing_data)

                }
             );
    });
});



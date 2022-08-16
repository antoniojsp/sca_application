// hide and show elements functions/
function show_hide_extra_inputs(element, attr_list) {
      var element_display = document.getElementById(element);
      if (element_display.style.display === "none") {
        element_display.style.display = "block";
        change_required_attributes(attr_list, true);
      } else {
        element_display.style.display = "none";
        change_required_attributes(attr_list, false);
      }
};
function change_required_attributes(attr_list, new_attr){
        for (var i = 0; i < attr_list.length; i++){
            var el = document.getElementById(attr_list[i])
            el.required = new_attr;
    }
};
function hide_if_selected(selection, element_to_hide, if_selected, attr_list){
// if certain option (selection)is selected (if_selected) then all the elements in the attr_list are hidden and vice versa
        var elem = document.getElementById(element_to_hide);

        if(selection != if_selected){
            elem.style.display = "block";
            change_required_attributes(attr_list, true);
        }else{
            elem.style.display = "none";
            change_required_attributes(attr_list, false);
        }
    }
function show_if_selected(selection, element_to_show, if_selected, attr_list){
// if certain option (selection) is selected (if_selected) then all the elements in the attr_list are shown and vice versa

        var element = document.getElementById(element_to_show);
        if(selection == if_selected){
            element.style.display = "block";
            change_required_attributes(attr_list, true);
        }else{
            element.style.display = "none";
            change_required_attributes(attr_list, false);
        }
    }


//copy text from input to another
function copy_input(input, from, to){
    if (input.checked){
         $(to).val($(from).val());
    }else{
         $(to).val("");
    }
};

// highlight and clear inputs  depending if they are missing or not
function highlight_missing_input(data_dict){

    var is_data_missing = false
    for( var i = 0; i<data_dict.length; i++){
        if (data_dict[i][1] == false){
            var elem_input = document.getElementById(data_dict[i][0]);
            elem_input.style.background="yellow";
            is_data_missing = true;

            var elem_bar = document.getElementById(data_dict[i][2]);
            elem_bar.style.background="yellow";
        }
    }

    return is_data_missing
};
function clear_highlight(elem){
  elem.style.background="white";
};

// checks if emails are valid. Display warning message if it's not valid. It also return false and can prevent submiting data if email is note legal
function valid_email(input){
    var re = /\S+@\S+\.\S+/;
    return re.test(input);
};
function if_email_valid(input, response){
    var email = input.value;
    if (valid_email(email) || email == ""){
        $(response).text("")
    }else{
        $(response).text("This email is not legal.")
    };
};

// checks if applicant is at least 18 years old.
// returns the closest date of birth for the applicant to be legal age
function dob_legal_age(legal_age){
  var soonest_date = new Date();
  soonest_date.setFullYear(soonest_date.getFullYear() - legal_age);
  return soonest_date
};
function is_underage(input){
    var dob = new Date(input.value);
    if (dob > dob_legal_age(18)){
        $('#is_underage').text("You need to  be at least 18 years of age to apply. Please, call the office before sending the application.")
    }else{
        $('#is_underage').text("")
    }
}

function current_date(){
        var year = new Date().getYear() + 1900;

        // set the move_in_year to this one, at least
        $("#move_in_year").attr({
           "min" : year,
           "value" : year
        });

        var date = new Date().toISOString().split('T')[0];
        $("#today_date").attr({
           "min" : date,
           "value" : date
        });

        // leave the dob empty to force user to add it manually. CHeck with client if underage may apply in some circunstances
        var min_date = dob_legal_age(18).toISOString().split('T')[0];
        $("#dob").attr({
           "max" : date
        });
};

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
    var sections = ["coverpage-tab","agreement-tab","checklist-tab","personal-information-tab","short-essay-tab","autobiographical-tab",
    "scale-tab", "references-tab"]
    const mySet1 = new Set()
    for (var i = 0; i < data_dict.length; i++){

        for (let j in data_dict[i]){
            var input_value = data_dict[i][j][0]
            var is_required = data_dict[i][j][1]
            if (input_value == "" && is_required == true){
                mySet1.add(sections[i])
                missing_input.push([j, false, sections[i]]);
            }else{
                missing_input.push([j, true, "None"]);

            }
        }
    };
    return missing_input
};

$(document).ready (function (){
$('#submit_form').click(function(){

   var classes = ['cover', 'agreement', "checklist", 'form-control personal', "essay", "auto", "range", "reference"]
//   var sections = ["coverpage-tab","agreement-tab","checklist-tab","personal-information-tab","short-essay-tab","autobiographical-tab",
//    "scale-tab", "references-tab"]
    var dict_check_complete = []
//    var dict_submit_server = {}
    for (var i = 0; i<classes.length; i++){
        dict_check_complete.push(input_dict(classes[i]));
//        dict_submit_server[sections[i]] = input_dict(classes[i])
    }

    console.log(dict_check_complete)
    var missing_data = check_inputs(dict_check_complete);


    //TODO
    var dob = new Date($("#dob").val());
    if (dob < get_min_date(18)){
        console.log("mayor")
    }else{
        console.log("Menor")
    }


    if (highlight_missing_input(missing_data)){
        alert("Please, review the form. Pages with missing info are highlighted.")
        return
    }

    if (get_min_date(18)){
       alert("Please, review your DOB. If you are underage, please contact the office.")
       return
    }



    var submit_data = {"data":JSON.stringify(dict_check_complete)}

        $.getJSON( "/_submit",
            submit_data,
            function(data) {
            console.log("Data sent")
             window.location.reload();
            }
         );
    });
});


// next and prev buttons
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
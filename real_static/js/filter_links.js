var update_content = function (real_str)
{
    // window.history.pushState(null, null, real_str);
    window.location.href = real_str;
}
// var filter_change_event = function (type, value, clean_all)
var filter_change_event = function (obj, clean_all, updating, url_clean)
{
    // obj = {};
    // obj[type] = value;

    _mode = 0
    if (clean_all)
    {
        // _old_obj = $.deparam.querystring()
        // if (_old_obj[type] != value)
        // {
        //     // remove all other args
        //     _mode = 2
        // }
        _mode = 2
    }

    if (url_clean) {
        url_base = "/"
    }else {
        url_base = window.location.href
    }

    real_str = $.param.querystring(
        url_base, obj, _mode
    );

    if (updating) {
        update_content(real_str);
    }
}

var clean_type = function (str) {
    position = str.indexOf("_0");
    if (position == -1){
        return str
    }else{
        return str.substring(0,position);
    }
}

var show_hide_array = function (arr, type){
    $.each(arr, function (i, el){
        // $("[name='"+el+"']").{type}();
        if (type== "show"){
            $("[name='"+el+"']").show();
        }else if (type == "hide")
            $("[name='"+el+"']").hide();
        })
}

$(function (){
    function urlCheck(){
        if ( window.location.pathname == "/" || window.location.pathname.indexOf('commercial')>-1 || window.location.pathname.indexOf('living')>-1 ){
            filter_submit_button(_obj);
            $('html,body').animate({scrollTop: $("#realty-calc").offset().top},'slow');
        }else if ( window.location.pathname == "/favorite-cards" ){
            favorites_submit();
        }else if ( window.location.pathname == "/user-profile" ){
            if ( current_status == 'my-favorites'){
                favorites_submit();
            }else if ( current_status == 'my-cards'){
                my_cards_submit();
            }
        }else if ( String(window.location.pathname).indexOf("/agency-page") >-1 ){
            agency_submit();
        }


    }

    $(".filter_submit_button").on("click", function (e){
        e.preventDefault();
        _obj["page"]=1;
        filter_submit_button(_obj);
        $('html,body').animate({scrollTop: $("#realty-calc").offset().top},'slow');
    });

    $(".with_photo").on("click", function (){
        if ( $(this).find(".checkbox").attr("checked") ) {
            _obj["with_photo"] = "yes";
            $(".with_photo").find(".checkbox").attr("checked","checked");
        }else {
            delete _obj["with_photo"];
            $(".with_photo").find(".checkbox").removeAttr("checked");
        } 
    });

    if (typeof _obj == "undefined"){
        _obj = {
            "group": "living",
            "cat_tab": "flat",
            "action_type": "sale",
            "cat_type": "flat",
            "number_of_rooms": [],
        };
        side_obj = _obj;
    }

    $(".select").on("change", function (){
        if ( $(this).data("type") == "region_0" ){
            $(".remove_region").css("display","inline");
            $("#side-filter #id_region_0").css("width","230px");
            var text = $(this).find('span').text();
            $.each($('[name="region_0"]'),function(index,value){
                $(value).find('span').text(text);
            });

            $.each($('[name="region2_0"]'),function(index,value){
                $(value).children().first().children().text('');
            });

            // delete _obj['region2'];

            ajaxGet("/ajax/get_region_autocomplete2", {'region' : $(this).children().first().text() }, function (data){
            // ajaxPost("{% url 'get_cat_types' %}", {}, function (data){

                $.each($('[name="region2_0"]'),function(index,value){
                    $(value).find("ul").empty();
                    $.each(data, function (i, el){
                        $(value).find("ul").append(
                            $("<li/>", {
                                text: el, 
                                "data-value": el, 
                                class: "option"
                                }
                            )
                        );
                    });
                });
                // $($('#id_region2_0 > ul').children()[1]).click();

                $('[name="region2_0"] li[data-value="Брестский"]').css('font-weight','bold');
                $('[name="region2_0"] li[data-value="Витебский"]').css('font-weight','bold');
                $('[name="region2_0"] li[data-value="Гомельский"]').css('font-weight','bold');
                $('[name="region2_0"] li[data-value="Гродненский"]').css('font-weight','bold');
                $('[name="region2_0"] li[data-value="Минский"]').css('font-weight','bold');
                $('[name="region2_0"] li[data-value="Могилевский"]').css('font-weight','bold');
            });
        }

        if ( $(this).data("type") == "currency_0" ) {
            var text = $(this).find('span').text();
            $.each($('[name="currency_0"]'),function(index,value){
                $(value).find('span').text(text);
            });
            return
        }

        if ( $(this).data("type") == "region2_0" ) {
            $(".remove_region2").css("display","inline");
            $("#side-filter #id_region2_0").css("width","230px");
            var text = $(this).find('span').text();
            $.each($('[name="region2_0"]'),function(index,value){
                $(value).find('span').text(text);
            });
            _obj['region2'] = text;
            return
        }

        if ( $(this).data("type") == "cat_type" ){
            _obj['cat_type'] = $(this).parent().find('ul').find('li:contains(' + $(this).find('span').text() + ')').data("value")
            if ( $(this).parent().parent().attr("name") == "cat_type_filter" ) {
                $($("li:contains('" +  $(this).children().first().text() + "')")[1]).trigger("click");
            }else if (  $(this).parent().parent().attr("name") == "cat_type_side") {
                $($("li:contains('" +  $(this).children().first().text() + "')")[0]).trigger("click");
            }else if ( $(this).attr("name") == "type_of_building_filter" ) {
                $($("li:contains('" +  $(this).children().first().text() + "')")[1]).trigger("click");
            }else if (  $(this).attr("name") == "type_of_building_side") {
                $($("li:contains('" +  $(this).children().first().text() + "')")[0]).trigger("click");
            }
            return
        }

        _obj[clean_type($(this).data('type'))] = $(this).data('selected');
    });

    $("#sort_order_id").on("change", function (){
        _obj[$(this).data('type')] = $(this).data('selected');
        filter_submit_button(_obj);
        $('html,body').animate({scrollTop: $("#realty-calc").offset().top},'slow');
    });

    $(".switcher").on("change", function (){
        if ( $(this).attr("name") == "sell_rent_filter" ) {
            $("[name='sell_rent_side']").find("div[data-type='" + $(this).find(".active").data("type") + "']").removeClass("active");
            $("[name='sell_rent_side']").find("div[data-value='" + $(this).find(".active").data("value") + "']").addClass("active");
        }else if (  $(this).attr("name") == "sell_rent_side") {
            $("[name='sell_rent_filter']").find("div[data-type='" + $(this).find(".active").data("type") + "']").removeClass("active");
            $("[name='sell_rent_filter']").find("div[data-value='" + $(this).find(".active").data("value") + "']").trigger("click");
        }
        _obj[clean_type($(this).find("div.active").data('type'))] = $(this).find("div.active").data('value');
    });

    // $("div.checkbox").on("click", function (){
    //     if ( $(this).attr("id") == "search2_1" ) {
    //         // $("[name='sell_rent_side']").find("div[data-value='" + $(this).find(".active").data("value") + "']").trigger("click");
    //     }else if (  $(this).attr("id") == "side2_1") {
    //         // $("[name='sell_rent_filter']").find("div[data-value='" + $(this).find(".active").data("value") + "']").trigger("click");
    //     }
    //     _obj[clean_type($(this).find("div.active").data('type'))] = $(this).find("div.active").data('value');
    // });

    $("#realty-calc #action_type_0_rent").on("click", function (){
        $($($("[name='search2_1']")[0]).children()[0]).hide();
        $($($("[name='search2_1']")[0]).children()[1]).show();
        $($($("[name='search2_1']")[1]).children()[0]).hide();
        $($($("[name='search2_1']")[1]).children()[1]).show();
        if ( $(".month").first().find(".checkbox").attr("checked") != "checked" ){ $(".month").first().find(".checkbox").trigger("click"); }
        delete _obj["exchange"];
    });

    $("#realty-calc #action_type_0_sale").on("click", function (){
        $($($("[name='search2_1']")[0]).children()[0]).show();
        $($($("[name='search2_1']")[0]).children()[1]).hide();
        $($($("[name='search2_1']")[1]).children()[0]).show();
        $($($("[name='search2_1']")[1]).children()[1]).hide();
        $("[name='search2_1'] .checkbox").removeAttr("checked");
        delete _obj["exchange"];
        delete _obj["period"];
    });

    $("#currency.sort-text").on("change", function (){
        _obj[$(this).data("type")] = $(this).find(".active").data("value");
        urlCheck();
    });

    // $(".button-chooser").click(function () {
    //     if ( $(this).children().hasClass("showR") ) {
    //         _obj[ clean_type($(this).children().filter( ".showR" ).data("type")) ] = $(this).children().filter( ".showR" ).data("value");
    //     }
    //     else {
    //         delete _obj[ "number_of_rooms" ];
    //     }
    // });

    $("[name='number_of_rooms'] .room").on("click", function (){
        if ( !$(this).hasClass("showR") ){
            $("[name='number_of_rooms']").find('buttons[data-value="' +  $(this).data("value") + '"]').addClass("showR");
            _obj[ "number_of_rooms" ].push($(this).data("value"));
        }else {
            $("[name='number_of_rooms']").find('buttons[data-value="' +  $(this).data("value") + '"]').removeClass("showR");
            var index = _obj[ "number_of_rooms" ].indexOf($(this).data("value"));
            _obj[ "number_of_rooms" ].splice(index, 1);
        }
    });

    function sync_checkboxes(element, obj_label, rm){
        if (element.find("span").find("div").attr("checked") == "checked"){
            $("." + element.attr("class")).find("span").find("div").attr("checked","checked");
            $(rm).find("span").find("div").removeAttr("checked");
            _obj[obj_label] = element.attr("class");
        }else {
            $("." + element.attr("class")).find("span").find("div").removeAttr("checked");
                delete _obj[obj_label];    
        }
    }

    $.each([ ".exchange", ".day", ".month" ], function( index, value ) {
        $(value).on("click", function(){
            if ( value == ".day" ){
                sync_checkboxes($(this), "period", ".month");
            }else if ( value == ".month" ){
                sync_checkboxes($(this), "period", ".day");
            }else {
                sync_checkboxes($(this), "exchange");
            }
        });
    });

    $(".filter-link").on("click", function (){
        if ( $(this).data("type") == "cat_tab" ){
            if ( $(this).parent().attr("id") == "calc-tabs" ) {
                $($("div[data-value=" +  $(this).data("value") + "]")[1]).parent().children().removeClass("active");
                $($("div[data-value=" +  $(this).data("value") + "]")[1]).addClass("active");
            }else if (  $(this).parent().attr("id") == "side-filter-menu") {
                $($("div[data-value=" +  $(this).data("value") + "]")[0]).parent().children().removeClass("active");
                $($("div[data-value=" +  $(this).data("value") + "]")[0]).addClass("active");
            }
        }

        type = $(this).data("type")
        value   = $(this).data("value")
        _obj[type] = value
        
        if ($(this).attr("id")=="big-icon"){
            $("#adverts_list").show();
            $("#adverts_grid").hide();
        }else if ($(this).attr("id")=="small-icon"){
            $("#adverts_list").hide();
            $("#adverts_grid").show();
        }

        if ($(this).attr("data-type")=="cat_tab"){
            // Reset _obj
            new_obj = {};
            new_obj["cat_tab"] = $(this).data("value");

            $.each(["group",
                    "action_type",
                    "region", 
                    "region2", 
                    "with_photo", 
                    "period", 
                    "exchange", 
                    "number_of_rooms",
                    "convert_currency_to",
                    "sort_order"], function( index, value ) {
                        if ( value in _obj ) {
                            new_obj[value] = _obj[value];
                        }
            });

            delete _obj;
            _obj = new_obj;
            delete new_obj;

            //  Clean filter fields
            $("input").val("");
            $("[name='number_of_rooms'] .checkbox").removeAttr("checked");
            // $("div#realty-calc #region_0_id").children().text("Выбор региона, города");
            // $("div#side-filter #region_0_id").children().text("Выбор региона, города");

            var buttons = document.getElementsByName("search-buttons");
            for (i = 0; i < 8; i++) { 
                buttons[i].style.display="none";
            }

            if ( $(this).data("value") == "flat" ){
                // _obj['cat_type'] = "flat";
                // $("[name='search-total_area']").css("display", "none")
                show_hide_array([
                    "plot_size_in_acros",
                    "price",
                    "type_of_building",
                    "total_area",
                    "living_area",
                    "price",
                    "search2_1_rent",
                    "plot_size_in_acros",
                    "price3",
                    "empty"], "hide");
                show_hide_array([
                    "cat_type_filter",
                    'cat_type',
                    "number_of_rooms",
                    "price2",
                    "search2_1",
                    'another',
                    ], "show");
                // $("#search2_1").show();
                // $("#search2_1_rent").hide();
                buttons[0].style.display="block";
                buttons[4].style.display="block";

            }else if ( $(this).data("value") == "house" ){
                show_hide_array([
                    
                    "price",
                    "type_of_building",
                    "number_of_rooms",
                    "total_area",
                    "empty",
                    "price",
                    "price2",
                    "search2_1_rent",
                    "total_area",
                    'another',
                    ],"hide");

                show_hide_array([
                    "plot_size_in_acros",
                    "cat_type",
                    "living_area",
                    "price3",
                    "search2_1",
                    ], "show");

                // $("#search2_1").show();
                // $("#search2_1_rent").hide();
                buttons[1].style.display="block";                  
                buttons[5].style.display="block";                  

            }else if ( $(this).data("value") == "area" ){
                show_hide_array([
                    "plot_size_in_acros",
                    "cat_type",
                    "type_of_building",
                    "number_of_rooms",
                    "price2",
                    "plot_size_in_acros",
                    "living_area",
                    "search2_1",
                    "price3",
                    ], "hide");
                show_hide_array([
                    "price",
                    "total_area",
                    "empty",
                    'another',
                    ], "show");
                // $("#search2_1").hide();
                buttons[2].style.display="block";
                buttons[6].style.display="block";

            }else if ( $(this).data("value") == "liv_misc" ){
                show_hide_array([
                    "plot_size_in_acros",
                    "price",
                    "plot_size_in_acros",
                    "number_of_rooms",
                    "living_area",
                    "search2_1",
                    "price3",
                    "empty",
                    ], "hide");
                show_hide_array([
                    "type_of_building",
                    "cat_type",
                    "total_area",
                    "price2",
                    'another',
                    ], "show");
                // $("#search2_1").hide();
                buttons[3].style.display="block";
                buttons[7].style.display="block";

            }else {

                show_hide_array([
                    'plot_size_in_acros',
                    'cat_type_filter',
                    'type_of_building',
                    'with_photo',
                    'number_of_rooms',
                    'total_area',
                    'price',
                    'price2',
                    "price3",
                    'living_area',
                    'empty',
                    'another',
                    'search2_1'], "hide");

                if ( $(this).data("value") == "building" ){
                    show_hide_array([
                        'price2',
                        'cat_type',
                        'cat_type_filter',
                        'empty',
                        'another',
                        'with_photo'], "show");
                    // $("#search2_1").hide();
                    buttons[3].style.display="block";
                    buttons[7].style.display="block";
                }else if ( $(this).data("value") == "premise" ){
                    show_hide_array([
                        'price2',
                        'cat_type',
                        'cat_type_filter',
                        'empty',
                        'another',
                        'with_photo'], "show");
                    // $("#search2_1").hide();
                    buttons[3].style.display="block";
                    buttons[7].style.display="block";
                }else if ( $(this).data("value") == "land" ){
                    show_hide_array([
                        'price',
                        'empty',
                        'another',
                        'with_photo'], "show");
                    // $("#search2_1").hide();
                    buttons[3].style.display="block";
                    buttons[7].style.display="block";
                }else if ( $(this).data("value") == "business" ){
                    show_hide_array([
                        'price2',
                        'cat_type',
                        'cat_type_filter',
                        'empty',
                        'another',
                        'with_photo'], "show");
                    // $("#search2_1").hide();
                    buttons[3].style.display="block";
                    buttons[7].style.display="block";
                }
            }



            if ( _obj["action_type"] == "rent" && _obj["period"] == "day" ) {
                $("#action_type_0_rent").trigger("click");
                if ( $(".day").first().find(".checkbox").attr("checked") != "checked" ){ $(".day").first().find(".checkbox").trigger("click"); }
            }else if ( _obj["action_type"] == "rent" ) {
                $("#action_type_0_rent").trigger("click");                
            }
        }
    });

    function scrollTo(id)
    {
      // Scroll
      $('html,body').animate({scrollTop: $("#"+id).offset().top},'slow');
    }

    function search_region(place){
        $($("#region_0_id").next().find( "li:contains("+ place +")" )[0]).trigger("click");
        filter_submit_button(_obj);
        scrollTo("content");
    }

    $('[name="belarus"]').on("click", function (){
        var place = $("#bel-map").find(".hover").data("value");
        $("#region_0_id").next().find( "li:contains("+ place +")" ).trigger("click");
        filter_submit_button(_obj);
        scrollTo("content");
    });

    $(".city-menu-content").on("click", function (e){
        var place = $(this).find("a").text();
        search_region(place);       
    });

    $(".map-capital")
        .on("click", function (e){
            var place = $(this).children().first().text();
            search_region(place);
        })       
        .mouseenter(function() {
            var pos_top = parseInt($(this).css("top"));
            pos_top = pos_top - 10;
            $(this).css("top","" + pos_top + "px");
            $(this).children().first().css("margin-bottom","10px");
            $(this).find("img").attr("src","/static/images/capital1.png");
            $(this).find("img").css("width","20px");
            $(this).find("img").css("height","20px");
        })

        .mouseleave(function() {
            var pos_top = parseInt($(this).css("top"));
            pos_top = pos_top + 10;
            $(this).css("top","" + pos_top + "px");
            $(this).children().first().css("margin-bottom","0px");
            $(this).find("img").attr("src","/static/images/capital.png");
            $(this).find("img").css("width","7px");
            $(this).find("img").css("height","7px");
        });

    $(".sort-direction").on("click", function(){
        _obj[$(this).data("type")] = $(this).data("value");
        $("#sort_order").children().children().css( "color", "rgb(84, 84, 84)" );
        $(this).css( "color", "rgb(255, 84, 66)" );
        urlCheck();
    });

    $(".sort-kind").on("click", function(){
        if ( $(this).next().css("color") == "rgb(255, 84, 66)" ) {
            $(this).next().next().trigger("click");
        } else {
            $(this).next().trigger("click");
        }
    });

    $(".remove_region").on("click", function(){
        $(".remove_region").hide();
        delete _obj["region"];
        $($(".remove_region")[0]).prev().prev().children().children().first().text("Выбор региона, города");
        $($(".remove_region")[1]).prev().prev().children().children().first().text("Выбор региона, города");
        $("#side-filter #id_region_0").css("width","250px");
        $(".remove_region2").click();
        $('[name="region2_0"] li').remove();
        $.each($('[name="region2_0"]'),function(index,value){
                $(value).children().first().children().text('');
            });

        delete _obj['region2'];

    });

    $(".remove_region2").on("click", function(){
        $(".remove_region2").hide();
        delete _obj["region2"];
        $("#side-filter #id_region2_0").css("width","250px");
        $.each($('[name="region2_0"]'),function(index,value){
                $(value).children().first().children().text('');
            });
    });

});

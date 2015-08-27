$(document).ready(function() {
    //--------
    newPercent();
    //--------
    // one_card();
    
    add_favorite();

    paginator_click();

    dont_close_dropdown = false

    if (typeof file_lists == "undefined"){
        // if( localStorage["images"] ){
        //     images = JSON.parse(localStorage["images"]);
        //     image_names = JSON.parse(localStorage["image_names"]);
        // }else{
            file_lists = new Array();
            images = new Array();
            uniqueImgNames = new Array();
            stored_imgs = new Array();
        // }
    }
    
    $(document).ready(function() {
        $(".feedback").click(function () {
            s = ".feedback-" + $(this).attr("review-id")
            $(s).toggle('slow');
            // alert($(this).attr("review-id")); 
        });
    });

    $(window).scroll(function () { // Показывает кнопку "Вверх"
        if ($(document).scrollTop() != 0) {
            $("#upButton").css("display", "block");
        }
        else {
            $("#upButton").css("display", "none");
        }
    })
    $(".checkbox").on("mousedown",function () { // Нужно для отключения выделения CHECKBOX'ов
        return false;
    });
    $(document).ready(function() {
    $(".checkbox").click(function (e) { // Работа с CHECKBOX'ом
        e.preventDefault();
        if ($(this).attr("checked")) {
            $(this).removeAttr("checked");
            $(this).find("input").removeAttr("checked");
        }
        else {
            $(this).attr("checked", "");
            $(this).find("input").prop("checked", "checked"); 
        }

        // if ( $(this).find("input").attr("id") == "id_day" ){
        //     $("#id_month").parent().removeAttr("checked")
        // }else if ($(this).find("input").attr("id") == "id_month" ){
        //     $("#id_day").parent().removeAttr("checked")
        // }

    });
    });
    // $(document).on("click", function (event) {
    $("*").click(function (event) { // Обработкакликов для скрытия SELECT'ов
        // var elem = $(event.target);
        if ( !dont_close_dropdown ){

            var elem = $(this);
            
            
            while (elem.get(0) != document) {
                if (elem.parent().find(">ul").eq(0).hasClass("show"))  return;
                elem = elem.parent();
            }

            $(".show").removeClass("show").prev().css("z-index", 2);
        }
    });
    

    // $("#rooms .room, #side-rooms .room,.rooms-filter .room").click(function () { // Кнопки количества комнат
    //     if ($(this).hasClass("showR")) {
    //         $(this).removeClass("showR");
    //         delete _obj["number_of_rooms"];
    //         return;
    //     }
    //     // $(this).parents().find(".room").removeClass("showR");
    //     $(this).addClass("showR");
    // });

    $("#realty-type div").click(function () { // Переключение типов недвижимости (Жилая/коммерческая)
        if ($(this).hasClass("active")) return;
        $("#realty-type div").removeClass("active");
        $(this).addClass("active");
    });
    $("#calc-tabs .calc-tab").click(function () {  // Переключение вкладок меню
        if ($(this).hasClass("active")) return;
        $("#calc-tabs .calc-tab").removeClass("active");
        $(this).addClass("active");
    });
    // $(".select-wrap > .select").click(function (event){
    // $(".select-wrap > .select").on("click", function (event){
    //     $(this).css("z-index", ($(this).css("z-index")==4)?2:4).parent().find("ul").eq(0).toggleClass("show");
    //     // event.stopPropagation();
    // });
    // Работа с SELECT'ом
    $(".select-wrap > .select").click(function (event){
        var oldHeight = $(this).parent().find("ul").height();
        $(this).parent().find("ul").toggleClass("show");
        var newHeight = $(this).parent().find("ul").height();
        $(this).parent().find("ul").addClass("show");
        if(newHeight > oldHeight) {
            $(this).css("z-index", 4)
        }
        $(this).parent().find("ul").css("height", oldHeight).animate({height: newHeight}, 100, function () {
            $(this).parent().find("ul").css("height", "");
            if(newHeight < oldHeight) {
                $(this).parent().find("ul").removeClass("show");
                $(this).parent().find(".select").css("z-index", 2);
            }
        })
        // $(this).css("z-index", ($(this).css("z-index")==4)?2:4)
        //     .parent()
        //     .find("ul")
        //     .toggleClass("show");
        event.stopPropagation();
    });
    $(document).on("click", ".option", function(event) {
        $.proxy(function (event){    
            var nowContent = $(this).parents(".select-wrap").find(".select span").html();

            $(this).parents(".select-wrap").find(".select span").html($(this).html());
            $(this).parent().prev().css("z-index", 2);

            var newContent = $(this).parents(".select-wrap").find(".select span").html();
            $(this).parent().prev().css("z-index", 2)
            if (nowContent != newContent) {
                /* событие change */ //alert("change");
                $(this).parent().prev().data("selected", $(this).data("value"));
                $(this).parent().prev().trigger("change");
            }
        }, event.target)(event);
    });
    $("#sell-rent-switch").find("div").click(function () { // Переключение Аренда/Продажа/Обмен
        if ($(this).hasClass("active")) return;
        $(this).parent().find(".active").removeClass("active");
        $(this).addClass("active");
    });
    $("#sort-icon > div").click(function() { // Переключение иконок сортировки
        if ($(this).hasClass("active")) return;
        $("#sort-icon div").removeClass("active");
        $(this).addClass("active").find("div").addClass("active");
    });
    $("#currency > span").click(switchCurrency);
    $(".switcher > div").click(function () {
        if ($(this).hasClass("active")) return;
        $(this).parent(".switcher").find("div").removeClass("active");
        $(this).addClass("active");

        $(this).parent().trigger("change");

    });
    $(".show-phone").click(function () {
        $(".show-phone").after("555-12-34").remove();
    });



    // ВРЕМЕННЫЕ ФУНЦИИ И ОБРАБОТЧИКИ
        $("#temp_progress button").click(function (event) {
            newPercent(parseInt(event.target.innerHTML));
        });
        // --------
    // });

    function fadeInWindow() { // Затемнение
        $("body").css("overflow", "hidden");
        $("#fade").css("display", "block");
    }
    function fadeOutWindow() { // Убрать затемнение
        $("body").css("overflow", "auto");
        $("#fade").css("display", "none");
    }
    function showRegistWindow() { // Открыть окно регистрации
        closeAuthorWindow();
        fadeInWindow();
        $("#regist_window").eq(0).css("display", "block");
    }
    function closeRegistWindow() { // Скрыть окно регистрации
        fadeOutWindow();
        $("#regist_window").eq(0).css("display", "none");
    }
    function showAuthorWindow() { // Открыть окно авторизации
        closeRegistWindow();
        fadeInWindow();
        $("#author_window").eq(0).css("display", "block");
    }
    function closeAuthorWindow() { // Скрыть окно авторизации
        fadeOutWindow();
        $("#author_window").eq(0).css("display", "none");
    }
    function newPercent(p) { // Изменение цвета прогрессбара (удалить некоторые строки)
        var oldp = parseInt($("#percent").text());
        if (p) {
            var newp = oldp + p;
            if (newp > 100) newp = 100;
            if (newp < 0) newp = 0;
        }
        else {
            newp = oldp;
        }
        $("#percent").html(newp+"%");
        $("#progress").css("width", newp+"%").css("background-color", "hsl("+newp+",60%,50%)");
    }


    /* script single */
    $(document).ready(function() {
        $("#show-filter").click(function () {
            $("#realty-calc").slideToggle("slow");
            // var oldHeight = $("#inner-single-calc").height();
            // $("#inner-single-realty-calc").toggle();
            // var newHeight = $("#inner-single-calc").height();
            // $("#inner-single-realty-calc").toggle(true);
            // $("#inner-single-calc").css("height", oldHeight).animate({height: newHeight}, function () {
            //     $("#inner-single-calc").css("height", "");
            //     if (newHeight < oldHeight) {
            //         $("#inner-single-realty-calc").toggle(false);
            //     }
            // });
            $("#show-filter").toggleClass("show-filter");
            $("#show-filter").html(($("#show-filter").html() == "Показать фильтр") ? "Спрятать фильтр" : "Показать фильтр");
        });
    });

    // function showSingleFullCalc() {
    //     $("#inner-single-realty-calc").animate({
    //         height: ($("#inner-single-realty-calc").height() == "200") ? "720px" : "200px"
    //     });
    // }
    function showSingleFullCalc() { // Показать/скрыть расширенный фильтр
        var oldHeight = $("#inner-single-realty-calc").height();
        $("#search3-wrap").toggle();
        var newHeight = $("#inner-single-realty-calc").height();
        $("#search3-wrap").toggle(true);
        $("#inner-single-realty-calc").css("height", oldHeight).animate({
            height: newHeight
        }, function () {
            $("#inner-single-realty-calc").css("height", "");
            if (newHeight < oldHeight) {
                $("#search3-wrap").toggle(false);
            }
        });
    }

    /* script realty */
    $(document).ready(function() {
        $("#side-filter").on("mouseenter", function () {
            showSideFilter();
        });
        $("#side-filter").on("mouseleave", function () {
            hideSideFilter();
        });
        $("#side-filter-menu > div").click(function () { // Переключение вкладок меню бокового фильтра
            if ($(this).hasClass("active")) return;
            $("#side-filter-menu").find("div").removeClass("active");
            $(this).addClass("active");
        });

        $("#sort-icon > div").click(function() { // Переключение иконок сортировки
            if ($(this).hasClass("active")) return;
            $("#sort-icon div").removeClass("active");
            $(this).addClass("active").find("div").addClass("active");
        });
        $("#currency > span").click(function () { // Переключение валют
            if ($(this).hasClass("active")) return;
            $("#currency span").removeClass("active");
            $(this).addClass("active");
        });
        $("area").hover(function () { // Событие мыши над регионом
            var pos_top = parseInt($("#capital_" + $(this).attr("city")).css("top"));
            pos_top = pos_top - 10;
            $("#capital_" + $(this).attr("city")).css("top","" + pos_top + "px");
            $("#capital_" + $(this).attr("city")).children().first().css("margin-bottom","10px");
            $("#capital_" + $(this).attr("city")).find("img").attr("src","/static/images/capital2.png");
            $("#capital_" + $(this).attr("city")).find("img").css("width","20px");
            $("#capital_" + $(this).attr("city")).find("img").css("height","20px");
            $("#capital_" + $(this).attr("city")).css("z-index","1");
            $("#capital_" + $(this).attr("city")).css("cursor","pointer");
            $("#bel-map").find("#"+$(this).attr("city")).addClass("hover");
            $("."+$(this).attr("city")+"-list").clearQueue().delay(500).fadeIn(200);
        }, function (event) {
            var pos_top = parseInt($("#capital_" + $(this).attr("city")).css("top"));
            pos_top = pos_top + 10;
            $("#capital_" + $(this).attr("city")).css("top","" + pos_top + "px");
            $("#capital_" + $(this).attr("city")).children().first().css("margin-bottom","0px");
            $("#capital_" + $(this).attr("city")).find("img").attr("src","/static/images/capital1.png");
            $("#capital_" + $(this).attr("city")).find("img").css("width","7px");
            $("#capital_" + $(this).attr("city")).find("img").css("height","7px");
            $("#bel-map").find("#"+$(this).attr("city")).removeClass("hover");
            $("."+$(this).attr("city")+"-list").clearQueue().delay(200).fadeOut(100);
        });
        $(".city-menu").hover(function() { // Всплывающее меню над регионом
            $(this).clearQueue();
        }, function () {
            $(this).clearQueue().delay(200).fadeOut(100);
        });
        $("#pagin .pagin-wrap, .next:not('.inactive'), .prev:not('.inactive')").click(pagination); // Пагинация
    }); // Конец READY




    $("area").hover(function () {
        $("#bel-map").find("#"+$(this).attr("city")).addClass("hover");
        $("."+$(this).attr("city")+"-list").clearQueue().delay(500).fadeIn(200);
    }, function (event) {
        $("#bel-map").find("#"+$(this).attr("city")).removeClass("hover");
        $("."+$(this).attr("city")+"-list").clearQueue().delay(200).fadeOut(100);
    });
    $(".city-menu").hover(function() {
        $(this).clearQueue();
    }, function () {
        $(this).clearQueue().delay(200).fadeOut(100);
    });
    $("#pagin .pagin-wrap, .next").click(pagination);
    function pagination() {
        $(".inactive").removeClass("inactive").click(pagination);
        if($(this).hasClass("pagin-wrap")) {
            $("#pagin .active").removeClass("active");
            $(this).addClass("active");
        }
        if($(this).hasClass("next")) {
            $("#pagin .active").removeClass("active").nextAll(".pagin-wrap").eq(0).addClass("active");
        }
        if($(this).hasClass("prev")) {
            $("#pagin .active").removeClass("active").prevAll(".pagin-wrap").eq(0).addClass("active");
        }
        if(!$("#pagin .active").prevAll(".pagin-wrap").get(0)) {
            $("#pagin .prev").unbind().addClass("inactive");
        }
        if(!$("#pagin .active").nextAll(".pagin-wrap").get(0)) {
            $("#pagin .next").unbind().addClass("inactive");
        }
    }
    $("#pagin .pagin-wrap, .next:not('.inactive'), .prev:not('.inactive')").click(pagination); // Пагинация
}); // Конец READY

    $(".show-phone").click(function () {
        $(".show-phone").after("555-12-34").remove();
    });
    $("#side-filter-menu > div").click(function () {
        if ($(this).hasClass("active")) return;
        $("#side-filter-menu").find("div").removeClass("active");
        $(this).addClass("active");
    })

    $("#temp_progress button").click(function (event) {
        newPercent(parseInt(event.target.innerHTML));
    });

/* script add */
$(document).ready(function() {
    /* ДОБАВЛЕНИЕ ФОТОГРАФИЙ */
    $("#add-photo").on("dragleave", function (event) {
        event.preventDefault();
        if (event.originalEvent.screenX == 0 && event.originalEvent.screenY == 0) {
            $("#drag-overlay").css("display" , "");
            $("#add-photo").css("z-index", "")
            .css("position", "")
            .css("border-style", "dashed");
            return false;
        }
        $(this).css("border-style", "dashed"); // Стиль фотоприемника при потере фокуса
        return false;
    }).on("dragenter", function (event) {
        if ($("#drag-overlay").css("display") == "none") {
            $("#drag-overlay").css("display" , "block");
            $("#add-photo").css("z-index", 101)
            .css("position", "relative");
        }
        event.preventDefault();
        $(this).css("border-style", "solid"); // Стиль фотоприемника при получении фокуса
        return false;
    });
    $(document).on("dragenter", function (event) {
        event.preventDefault();
        if ($("#drag-overlay").css("display") == "block") return false;
        $("#drag-overlay").css("display" , "block");
        $("#add-photo").css("z-index", 101)
            .css("position", "relative");
        return false;
    })
    $("#drag-overlay").on("dragleave", function (event) {
        if (event.originalEvent.screenX != 0 && event.originalEvent.screenY != 0) return false;
        event.preventDefault();
        $("#drag-overlay").css("display" , "");
        $("#add-photo").css("z-index", "")
            .css("position", "");
        return false;
    });

    $("*").on("dragover", function (event) {
        event.preventDefault(); // Нужно что бы нормально обработать ONDROP
        return false;
    });

    $("*").on("drop", function (event) {
        $("#drag-overlay").css("display" , "");
        $("#add-photo").css("z-index", "")
            .css("position", "")
            .css("border-style", "dashed");
            if (event.target.id == "add-photo") {
                // Добавить фотографию
                var files = event.originalEvent.dataTransfer.files;
                addPhotos(files);
        }
        return false;
    });
    $(document).on("dragover", function (event) {
        event.preventDefault();
        // $("#event-overlay").css("display" , "block");
        // $("#add-photo").css("z-index", 101)
        //     .css("position", "relative");
    });
    
    // Добавить фотографию по клику
    $("#sidebar-photo input[type='file']").on("change", function (event) {
            var files = event.target.files;
            addPhotos(files);
    })
    // Удаление фотографий
    $(document).on("mouseenter", "#photo-block > img", function() {
        if(!$("#photo-block > .erase-photo").get(0)) {
            $("#photo-block").append("<div class='erase-photo'></div>");
        }
        $(".erase-photo").eq(0)
            .css("left", $(this).position().left+$(this).width()-$(".erase-photo").width())
            .css("top", $(this).position().top)
            .attr("photo", $(this).attr("name"));
    }).on("mouseleave", "#photo-block > img", function() {
        if(event.toElement.className == "erase-photo") return;
        $("#photo-block .erase-photo").remove();
    });
    $(document).on("mouseleave", ".erase-photo", function() {
        if(event.toElement.tagName.toLowerCase() == "img") return;
        $("#photo-block .erase-photo").remove();
    });
    $("#photo-block").on("click", ".erase-photo", function() {
        var erase = $(this).attr("photo");
        $("#photo-block > img").each(function () {
            if ($(this).attr("name") == erase) {

                $.each(uniqueImgNames, function(index,value){
                    if (uniqueImgNames[index]["name"] == erase){
                        uniqueImgNames.splice(index,1);
                        return false;
                    }               
                });

                var index = stored_imgs.indexOf(erase);
                if (index >= 0) {
                  stored_imgs.splice( index, 1 );
                }

                $(this).remove();
                $("#photo-block .erase-photo").remove();
                $("#photo-block").append("<div class='noPhoto'></div>");

                // localStorage["images"] = JSON.stringify(images);
                // localStorage["image_names"] = JSON.stringify(image_names);
                // if ( images == [] ){
                //     localStorage.clear();
                // }

                // if (typeof $("#photo-block").children().attr("name") == "undefined") {
                //     if ( $("#id_agreement").attr("checked","checked") ) {
                //         $("#id_agreement").trigger("click");
                //     }
                // }

                return false;
            }
        })
    });

    $(".thumb-img").on("click", function (e){
        $(".big-pic").attr("src", $(this).attr("src"));
    });
});

function switcher() {
    if ($(this).hasClass("active")) return;
    $(this).parent(".switcher").find("div").removeClass("active");
    $(this).addClass("active");

    

}
function showFullCalc() { // Показать/скрыть расширенный фильтр
    $("#search3-wrap").slideToggle("slow");
    // var oldHeight = $("#realty-calc").height();
    // $("#search3-wrap").toggle();
    // var newHeight = $("#realty-calc").height();
    // $("#search3-wrap").toggle(true);
    // $("#realty-calc").css("height", oldHeight).animate({
    //     height: newHeight
    // }, function () {
    //     $("#realty-calc").css("height", "");
    //     if (newHeight < oldHeight) {
    //         $("#search3-wrap").toggle(false);
    //     }
    // });
}

function come_back_to_main(){
    // $("#header").css("height","729px");
    $("#bottom-content").show();
    // $("#realty-calc").css("margin-top","-58px");
    $("#sort").show();
    $("#icon_view").show();
    $("#num_of_ads").show();
    $("#side-filter").show();
    $("#single-realty-calc").hide();
    $("#realty-calc").show();
    $("#one_card").hide();
    // history.pushState("filter", null, "/" );
    add_favorite();  
}

// function one_card(){
    // // $(".link_one_card").on("click", function () {
    // $(".link_one_card").mousedown(function(event) {
    //     if (event.which === 1) {
    //         var scroll_bck = $(document).scrollTop();
    //         obj_id = {"id": $(this).attr("idcard")};
    //         history.pushState("card", null, "card"+$(this).attr("idcard") );

    //         $("#header").css("height","158px");
    //         $("#bottom-content").hide();
    //         $("#realty-calc").css("margin-top","0px");
    //         $("#sort").hide();
    //         $("#icon_view").hide();
    //         $("#num_of_ads").hide();
    //         $("#side-filter").hide();
    //         $("#single-realty-calc").show();

    //         ajaxGet('one_card', obj_id, function (data){
    //             $("#one_card").html(data);
    //             add_favorite();
    //             $("#addBack").on("click", function () {
    //                 come_back_to_main();
    //                 $(document).scrollTop( scroll_bck );
    //             });

    //         });

    //         delete obj_id;
    //         $("#realty-calc").hide();
    //         $("#one_card").show();
    //         window.scrollTo(0, 0);
    //         // $('html,body').animate({scrollTop: $("#sort").offset().top},'slow');
    //     }
    // });
// }

function filter_submit_button(my_obj){
    // window.history.replaceState("object or string", "Title", "/");   
    var grid_view = false;
    new_obj = JSON.parse(JSON.stringify(my_obj));
    if ( new_obj["cat_tab"] == "area" || new_obj["cat_tab"]== "liv_misc" ){
        delete new_obj["period"];
        delete new_obj["exchange"];
    }
    new_obj["number_of_rooms"] = new_obj["number_of_rooms"].toString();
    if ($("#sort-icon").find(".active").attr("id") == "small-icon"){
        grid_view = true;
    }

    ajaxGet('ajax/get_filter', new_obj, function (data){
        $("#icon_view").html(data);
        if ( grid_view == true ){
                $('#small-icon').trigger('click');
        }
        $("#num_of_ads").html($("#num_of_ads_new").text());

        $('#map').children().remove();
        $('#map').hide();
        $('#map_toggle_link').show();
        only_ONE = true;

        // $('#region_0_id').find('span').text( $('#region_0_id').find('span').text() + ' (' +  $("#num_of_ads_new").text()  +')' );

        add_favorite();
        paginator_click();
        // history.pushState(null, null, "/");
        // one_card();
    });
    come_back_to_main();
}

function favorites_submit() {
    var grid_view = false;

    if ($("#sort-icon").find(".active").attr("id") == "small-icon"){
        grid_view = true;
    }

    ajaxGet('ajax/get_favorite_cards', _obj, function (data){
        $("#icon_view").html(data);
        if ( grid_view == true ){
                $('#small-icon').trigger('click');
        }
        add_favorite();
        $(".pagination").css("display","none"); 
    }); 
}

function agency_submit() {
    var grid_view = false;

    if ($("#sort-icon").find(".active").attr("id") == "small-icon"){
        grid_view = true;
    }
    _obj['obj_id'] = window.location.href.split('page')[1];

    ajaxGet('get_cards_agency', _obj, function (data){
        $("#icon_view").html(data);
        if ( grid_view == true ){
                $('#small-icon').trigger('click');
        }
        add_favorite();
        $(".pagination").css("display","none"); 
    });
    delete _obj['obj_id']; 
}


function my_cards_submit() {
    var grid_view = false;

    if ($("#sort-icon").find(".active").attr("id") == "small-icon"){
        grid_view = true;
    }

    ajaxGet('ajax/get_cards', _obj, function (data){
        $("#icon_view").html(data);
        if ( grid_view == true ){
                $('#small-icon').trigger('click');
        }
        add_favorite();
        $(".pagination").css("display","none"); 
    }); 
}

function pagination(page) {
    _obj['page'] = page
    var grid_view = false;

    if ($("#sort-icon").find(".active").attr("id") == "small-icon"){
        grid_view = true;
    }

    ajaxGet('ajax/get_filter', _obj, function (data){
        $("#icon_view").html(data);
        if ( grid_view == true ){
            $('#small-icon').trigger('click');
        }
        add_favorite();
        paginator_click();
        // one_card();
    });  
}
function paginator_click() {
    $("div.pagination span.step-links h4 a").on("click", function (){
        var page = $(this).attr("class").substring(5);            
        pagination(page);
        $('html,body').animate({scrollTop: $("#realty-calc").offset().top},'slow');
    });
}
function switchRealtyType() {
    if ($(this).hasClass("active")) return;
    $("#realty-type div").removeClass("active");
    $(this).addClass("active");
}
function switchTab() {
    if ($(this).hasClass("active")) return;
    $("#calc-tabs .calc-tab").removeClass("active");
    $(this).addClass("active");
}
function sellRentSwitch() {
    if ($(this).hasClass("active")) return;
    $(this).parent().find(".active").removeClass("active");
    $(this).addClass("active");
}
function toggleSelect() {
    $(this).parent().find("ul").eq(0).toggleClass("show");
}
function selectOption() {
    $(this).parent().toggleClass("show");
    $(this).parents(".select-wrap").find(".select span").html($(this).html());
    $(this).parents(".select-wrap").find(".select span").html($(this).html());


    $(this).parent().prev().data("selected", $(this).data("value"));
}

function switchSort() {
    if ($(this).hasClass("active")) return;
    $("#sort-icon div").removeClass("active");
    $(this).addClass("active").find("div").addClass("active");
}
function switchCurrency() {
    if ($(this).hasClass("active")) return;
    $("#currency span").removeClass("active");
    $(this).addClass("active");
    
    $(this).parent().trigger("change");
}


function fadeInWindow() {
    $("body").css("overflow", "hidden");
    $("#fade").css("display", "block");
}
function fadeOutWindow() {
    $("body").css("overflow", "auto");
    $("#fade").css("display", "none");
}




function showRegistWindow() {
    fadeInWindow();
    $("#regist_window").eq(0).css("display", "block");
}
function closeRegistWindow() {
    fadeOutWindow();
    $("#regist_window").eq(0).css("display", "none");
}
function showAuthorWindow() {
    fadeInWindow();
    $("#author_window").eq(0).css("display", "block");
}
function closeAuthorWindow() {
    fadeOutWindow();
    $("#author_window").eq(0).css("display", "none");
}

function add_favorite(){
    $(".favorite-card-main").on("click", function () {
        obj_id = { "obj_id": $(this).attr("name") };
        if ( $($(this).children()[0]).css("display") == "none"){

            $.each($("[name=" + $(this).attr("name") + "]"), function( index, value ) {
              // alert( index + ": " + value );
                $($(this).children()[0]).css("display","block");
                $($(this).children()[1]).css("display","none");
            });
            
        }else{

            $.each($("[name=" + $(this).attr("name") + "]"), function( index, value ) {
              // alert( index + ": " + value );
                $($(this).children()[0]).css("display","none");
                $($(this).children()[1]).css("display","block");
            });
            
        }

        ajaxGet('/add-favorite-card',obj_id,function(){});

        delete obj_id;
    });
}

// // ПОДКЛЮЧЕНИЕ ЯНДЕКС КАРТ
// var myMap;

// $(function (){
//     ymaps.ready(init);    
// });
// function init () {
//     // Создание экземпляра карты и его привязка к контейнеру с
//     // заданным id ("map").
//     myMap = new ymaps.Map('ymap', {
//         // При инициализации карты обязательно нужно указать
//         // её центр и коэффициент масштабирования.
//         center: [52.423, 30.9984], // Москва
//         zoom: 17,
//         controls: []
//     });
// }

function newPercent(p) {
    var oldp = parseInt($("#percent").text());
    var newp = oldp + p;
    if (newp > 100) newp = 100;
    if (newp < 0) newp = 0;
    $("#percent").html(newp+"%");
    $("#progress").css("width", newp+"%").css("background-color", "hsl("+newp+",100%,50%)");
}

function showSideFilter() {
    clearTimeout(window.timer);
    $("#side-filter").stop(true).animate({right: "0px"});
    $("#side-bookmark").stop(true).animate({width: "0px", left: "0"});
    // $("#side-bookmark").stop(true).animate({width: "0px", backgroundColor: "rgba(255, 84, 66, 0.1)", left: "0"});
}
function hideSideFilter() {
    clearTimeout(window.timer);
    $("#side-filter").stop(true).animate({right: "-290px"});
    $("#side-bookmark").stop(true).animate({width: "100px", left: "-100px"});
    // $("#side-bookmark").stop(true).animate({width: "100px", backgroundColor: "rgba(255, 84, 66, 0.6)", left: "-100px"});
}

function addPhotos(files) {
    images = [];
    file_lists = [];
    file_lists.push(files);

        for (var j=0; j<file_lists.length; j++) {
            for (var i=0; i<file_lists[j].length; i++) {
                images.push(file_lists[j][i]);
                if( stored_imgs.length + uniqueImgNames.length + images.length == 21 ){
                    if ( stored_imgs.length > 0 ) {  
                        stored_imgs.shift();
                    }else if ( uniqueImgNames.length > 0 ){
                        uniqueImgNames.shift();
                    }else if ( images.length > 0 ){
                        images.shift();
                    }
                }
            }
        }

        for (var i=0; i<images.length; i++) {
            var file = images[i];
            if (file.type.match("image")) {
                reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = (function (file) {
                    return function (event) {
                        if ($("#photo-block").find("[name = \'"+file.name+"\']").get(0)) {
                            return;
                        }
                        $("#photo-block").prepend("<img src=\""+event.target.result+"\", name=\""+file.name+"\">");
                        $("#photo-block *").last().remove();
                        uniqueImgNames.push(file);
                    }
                })(file);
            }
            else {
                alert("не фото");
            }
        }

    while ( $('#photo-block').children().length > 20 ){
        $('#photo-block').children().last().remove();
    }
}
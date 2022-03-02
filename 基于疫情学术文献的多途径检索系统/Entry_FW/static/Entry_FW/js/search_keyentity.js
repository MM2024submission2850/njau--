//响应search页面通过key和entitiy方式检索的需求

//按照类别方式进行检索
$("#check_query").click(function (e) {
    e.preventDefault();

    info = document.getElementById("search_input").value;

    request_param = {
        "mode": 'check_query',
        "info": info
    }

    console.log(request_param)

    load_style2(request_param)

});

//按照关键词方式进行检索
$("#check_entry").click(function (e) {
    e.preventDefault();

    info = document.getElementById("search_input").value;

    request_param = {
        "mode": 'check_entry',
        "info": info
    }
    console.log(request_param)
    load_style2(request_param)

});



//页面加载后，立即进行文献列表的加载
window.onload = function () {

    // request_param = {
    //     "mode": 'check_entry',
    //     "info": 'COVID-19'
    // }

    // load_style2(request_param);

    articleBox= document.getElementById("search_results");
    articleBox.innerHTML="<div class=\"card-body\"><p>清输入关键词或实体进行检索...</p></div>";
};

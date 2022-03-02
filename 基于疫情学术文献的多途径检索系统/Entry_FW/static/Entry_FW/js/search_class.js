

//按照类别进行检索
$(".btn-search-class").click(function (e) {
    e.preventDefault();
    class_name=  e.currentTarget.attributes['data'].value;

    
    request_param = {
        "mode": 'check_class',
        "info": class_name.toLowerCase(),
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
    articleBox.innerHTML="<div class=\"card-body\"><p>请选择类别开始检索...</p></div>";
};



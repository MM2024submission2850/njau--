


//将搜索提示数据导入到页面中
function html_wrapper(params) {
    s1 = "<nav class='navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow' id='search-tip'>"
    s2 = '</nav>';
    search_tip = document.getElementById("search-tip")
    search_tip.innerHTML = s1 + params + s2
}



// 用户搜索需要使用的程序
function search(e) {
    console.log("search log")
    mode = ""

    tmp = document.getElementById("check_class")
    if (tmp.checked) mode = "check_class"
    tmp = document.getElementById("check_entry")
    if (tmp.checked) mode = "check_entry"

    info = document.getElementById("search_input").value;


    request_param = {
        "mode": mode,
        "info": info,
    }

    $.ajax({
        type: "POST",
        url: "/request_doclist",
        data: request_param,
        success: function (response) {
            console.log("Service response!!!准备处理数据生成表格")
            res_block = document.getElementById("search_results")

            total_num = response.total_num
            search_list = response.results

        }
    });
}

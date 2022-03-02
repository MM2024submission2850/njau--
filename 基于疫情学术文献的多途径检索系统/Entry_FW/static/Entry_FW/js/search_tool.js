


//将搜索提示数据导入到页面中
function html_wrapper(params) {
    s1 = "<nav class='navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow' id='search-tip'>"
    s2 = '</nav>';
    search_tip = document.getElementById("search-tip")
    search_tip.innerHTML = s1 + params + s2
}



// function load(search_params) {
//     $('#search_results')
//         .bootstrapTable(
//             {
//                 method: 'post', // 服务器数据的请求方式 get or post
//                 url: "/request_doclist", // 服务器数据的加载地址
//                 ajaxOptions: { //设置超时
//                     async: true,
//                     tiemout: 2000,
//                 },
//                 striped: true, // 设置为true会有隔行变色效果
//                 dataType: "json", // 服务器返回的数据类型
//                 pagination: true, // 设置为true会在底部显示分页条
//                 // queryParamsType : "limit",
//                 // //设置为limit则会发送符合RESTFull格式的参数
//                 singleSelect: true, // 设置为true将禁止多选
//                 iconSize: 'outline',
//                 toolbar: '#exampleToolbar',
//                 contentType: "application/x-www-form-urlencoded",
//                 // //发送到服务器的数据编码类型
//                 pageSize: 5, // 如果设置了分页，每页数据条数
//                 pageNumber: 1, // 如果设置了分布，首页页码
//                 search: true, // 是否显示搜索框
//                 showColumns: true, // 是否显示内容下拉框（选择显示的列）
//                 sidePagination: "client", // 设置在哪里进行分页，可选值为"client" 或者
//                 // "server"
//                 queryParams: search_params, //查找参数相关
//                 // //请求服务器数据时，你可以通过重写参数的方式添加一些额外的参数，例如 toolbar 中的参数 如果
//                 // queryParamsType = 'limit' ,返回参数必须包含
//                 // limit, offset, search, sort, order 否则, 需要包含:
//                 // pageSize, pageNumber, searchText, sortName,
//                 // sortOrder.
//                 // 返回false将会终止请求


//                 columns: [
//                     { // 列配置项
//                         // 数据类型，详细参数配置参见文档http://bootstrap-table.wenzhixin.net.cn/zh-cn/documentation/
//                         checkbox: true
//                         // 列表中显示复选框
//                     },
//                     {

//                         field: 'doc_class', // 列字段名
//                         title: '类别',// 列标题
//                         visible: false
//                     },
//                     {
//                         field: 'entity',
//                         title: '实体',
//                         // formatter: function (value, row, index) {
//                         //     var a = '<a href="' + row.url + '">' + value + '</a>';
//                         //     return a;
//                         // }
//                     },
//                     // {
//                     //     field: 'abstract_entity',
//                     //     title: '抽象实体'
//                     // },
//                     // {
//                     //     field: 'publisher',
//                     //     title: '出版商',
//                     // },
//                     // {
//                     //     field: 'publisher_num',
//                     //     title: '出版编号'
//                     // },
//                     // {
//                     //     field: 'doi',
//                     //     title: 'doi'
//                     // },
//                     {
//                         field: 'date',
//                         title: '日期'
//                     },
//                     {
//                         field: 'title',
//                         title: '标题',
//                         formatter: function (value, row, index) {
//                             var a = '<a href="">' + value + '</a>';

//                             return a;
//                         }
//                     },
//                     {
//                         field: 'author',
//                         title: '作者'
//                     },
//                     {
//                         field: 'keyword',
//                         title: '关键字'
//                     },
//                     {
//                         title: '操作',
//                         field: 'goods_id',
//                         align: 'center',
//                         /*单元格格式化函数，有三个参数：value： 该列的字段值；row： 这一行的数据对象；index： 行号，第几行，从0开始计算*/
//                         formatter: function (value, row, index) {
//                             var result = '<a class="btn btn-primary btn-sm " title="detail" onclick="showdetail(\''
//                                 + row
//                                 + '\')"><i class="fa fa-map"></i></a> ';


//                             return result;
//                         }
//                     }
//                 ]
//             });
// }



// 这个是进行单列的渲染方式。通过内部模式进行转换
function load_style2(search_params) {

    innerText = document.getElementById("search_results");
    if (innerText != "")
        $('#search_results').bootstrapTable('destroy');

    $('#search_results')
        .bootstrapTable(
            {
                method: 'post', // 服务器数据的请求方式 get or post
                url: "/request_doclist", // 服务器数据的加载地址
                ajaxOptions: { //设置超时
                    async: true,
                    tiemout: 2000,
                },
                striped: true, // 设置为true会有隔行变色效果
                dataType: "json", // 服务器返回的数据类型
                pagination: true, // 设置为true会在底部显示分页条
                queryParamsType: "limit",
                // //设置为limit则会发送符合RESTFull格式的参数
                singleSelect: true, // 设置为true将禁止多选
                iconSize: 'outline',
                toolbar: '#exampleToolbar',
                contentType: "application/x-www-form-urlencoded",
                // //发送到服务器的数据编码类型
                pageSize: 5, // 如果设置了分页，每页数据条数
                pageNumber: 1, // 如果设置了分布，首页页码
                // search: true, // 是否显示搜索框
                // showColumns: true, // 是否显示内容下拉框（选择显示的列）
                sidePagination: "client", // 设置在哪里进行分页，可选值为"client" 或者
                // "server"
                queryParams: search_params, //查找参数相关
                // //请求服务器数据时，你可以通过重写参数的方式添加一些额外的参数，例如 toolbar 中的参数 如果
                // queryParamsType = 'limit' ,返回参数必须包含
                // limit, offset, search, sort, order 否则, 需要包含:
                // pageSize, pageNumber, searchText, sortName,
                // sortOrder.
                // 返回false将会终止请求


                columns: [
                    { // 列配置项
                        // 数据类型，详细参数配置参见文档http://bootstrap-table.wenzhixin.net.cn/zh-cn/documentation/
                        checkbox: true
                        // 列表中显示复选框
                    },
                    // {
                    //     // field: 'no',
                    //     title: '序号',
                    //     sortable: true,
                    //     align: 'center',
                    //     width: 40,
                    //     formatter: function (value, row, index) {
                    //         //获取每页显示数量
                    //         var pageSize = $('#search_results').bootstrapTable('getOptions').pageSize;
                    //         //获取当前是第几页
                    //         var pageNumber = $('#search_results').bootstrapTable('getOptions').pageNumber;
                    //         //返回序号
                    //         return pageSize * (pageNumber - 1) + index + 1;

                    //     }
                    // },
                    { //显示文献概述情况，页面进行重新组织
                        // title: '文献列表',
                        // field: 'doc_class',
                        align: 'left',
                        /*单元格格式化函数，有三个参数：value： 该列的字段值；row： 这一行的数据对象；index： 行号，第几行，从0开始计算*/
                        formatter: function (value, row, index) {

                            //实体词去重复
                            entity_list = [];

                            row['entity'].forEach(element => {
                                if (entity_list.includes(element)) {

                                }
                                else {
                                    entity_list.push(element);
                                }
                            });


                            if (index == 9) console.log(row)


                            var brief_template = ''

                                + '<dl class="articleBox" style="display: block;">'
                                + '<style type="text/css">'
                                + ' a {'
                                + '   margin: 7px;'
                                + '   border-bottom-color: rgb(169,182,181);'
                                + '   border-bottom-style: dotted;'
                                + '   border-bottom-width: 1px;'
                                + '   display: inline;'
                                + '  }'
                                + '</style>'

                                // 文章索引号
                                //文章标题
                                + '<dt class="mb5">'
                                + '<a class="smal_tip">'
                                + (index + 1)
                                + '</a>'
                                + '  <a class="toe" target="_blank" href="/research_detail?doi=' + row['doi'] + '">'
                                + '[' + row['title'] + ']'
                                + '  </a>'
                                + '</dt>'

                                + '<dd class="sel"></dd>'

                                + '<dd class="actor-dd">'
                                + '  <a target="_blank">'
                                + row['publisher']
                                + '  </a>'
                                + '</dd>'
                                + '<dd class="actor-dd">'
                                + '   <a target="_blank">'
                                + get_brief_str(row['institution'], 300)
                                + '   </a>'
                                + '</dd>'
                                + '<dd class="actor-dd>'
                                + '  <strong class="vm">作者：</strong>'
                                + '     <a>'
                                + get_brief_str(row['author'], 300)
                                + '     </a>'
                                // + '  <a target="_blank" title="F F Chen;">F F Chen</a>'
                                // + '  <a target="_blank" title="H L Tang;">H L Tang</a>'
                                // + '  <a target="_blank" title="P Lyu;">P Lyu</a>'
                                + '</dd>'

                                + '<dd><span class="grye">'
                                + get_brief_str(row['abstract'], 300)
                                + '</span></dd>'

                                //这里选择使用实体替代，但是必须避免重复
                                + '<dd class="key_word">'
                                + '   <span class="subject">'
                                + '    <strong>实体词：</strong>'

                            for (i = 0; i < entity_list.length; i++) {
                                if (i == 3) break;

                                brief_template += ''
                                    + '    <a href="" target="_blank" title="' + entity_list[i] + '">'
                                    + entity_list[i]
                                    + '     </a>'
                            }

                            brief_template += ''
                                + '     </span>'
                                + ' </dd>'
                                + '</dl>'


                            return brief_template;

                        }
                    }
                ]
            });
}

//按照类别方式进行检索
$("#check_class").click(function (e) {
    e.preventDefault();

    info = document.getElementById("search_input").value;

    request_param = {
        "mode": 'check_class',
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

    request_param = {
        "mode": 'check_entry',
        "info": 'COVID-19'
    }

    load_style2(request_param);

};



// 用户搜索需要使用的程序


//用于对过长的字符串进行定长度限制
function get_brief_str(str, limit) {

    if (str.length > limit) {
        str = str.substring(0, limit) + '...';
    }
    return str;
}
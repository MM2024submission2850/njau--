
var knowmap_data={};

$.getJSON("/keywordrel_data", function (data) {

    map_obj = document.getElementById("keywordmap");
    if (null == map_obj) return;

    var myChart = echarts.init(map_obj);

    myChart.showLoading();


    console.log('render keymap');

    var maplinks = data["r"];

    var node_data = {};
    var sourceflag = false;
    for(var dictkey in maplinks ){
        var infodict=maplinks[dictkey];
        if(!sourceflag){
            node_data[infodict["sourceNode"]]={
                "name":infodict["sourceNode"],
                "type":infodict["sourceType"],
                "value":1.0
            };
            sourceflag =true;
        }
        node_data[infodict["targetNode"]]={
                "name":infodict["targetNode"],
                "type":infodict["targetType"],
                "value":infodict["value"]
            }
    }
    knowmap_data=node_data;

    console.log(node_data);

    var nodes_keys = Object.keys(node_data);
    var nodes_num = nodes_keys.length;

    myChart.hideLoading();

    var categories = nodes_keys;

    for (i = 0; i < nodes_num; i++) {
        categories[i] = {
            name: nodes_keys[i]
        };
    }


    var links_num=maplinks.length;
    var links = [];

    for (i = 0; i < links_num; i++) {
        //处理links问题
        links.push({
            source: maplinks[i]['sourceNode'],
            target: maplinks[i]['targetNode'],
            name: maplinks[i]['relationName'],
            des: ''
            // des: tar['value'],
        });

    }

    console.log(links);

    //处理节点问题
    var node = [];
    for (i = 0; i < nodes_num; i++) {
        key = nodes_keys[i].name;
        node[i] = {
            name: key,
            // des:20,
            // symbolSize:Object.keys(element).length,
            symbolSize: 50*get_nodevalue(node_data[key]["value"]),
            category: key,   //会不会因为数字的原因无法加载
            //新增的一些特性
            draggable: "true"
        };

    }

    console.log(node);

    option = {
        // 图的标题
        title: {
            // text: 'ECharts 关系图'
        },
        // 提示框的配置
        tooltip: {},
        // 工具箱
        toolbox: {
            // 显示工具箱
            show: true,
            feature: {
                mark: {
                    show: true
                },
                // 还原
                restore: {
                    show: true
                },
                // 保存为图片
                saveAsImage: {
                    show: true
                }
            }
        },
        legend: [{
            data: categories.map(function (a) {
                return a.name;
            }),

            selectedMode: 'false',
            tooltip: {
                show: true
            },
            bottom: 20,
            data: categories

        }],
        animationDuration: 3000,
        animationEasingUpdate: 'quinticInOut',
        backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#f7f8fa'
        }, {
            offset: 1,
            color: '#cdd0d5'
        }]),
        series: [{
            name: '关键词',
            // 数据
            data: node,
            links: links,
            categories: categories,

            type: 'graph', // 类型:关系图
            layout: 'force', //图的布局，类型为力导图
            symbolSize: 30, // 调整节点的大小
            roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启
            draggable: true,
            focusNodeAdjacency: true,

            //stype2
            label: {
                position: 'right',
                formatter: '{b}'
            },
            lineStyle: {
                color: 'source',
                curveness: 0.3
            },
            circular: {
                rotateLabel: true
            },
            force: {
                repulsion: 1000,
                edgeLength: [150, 100],
                friction: 0.5

            },
            label: {
                normal: {
                    show: true,
                    position: 'top',
                    textstyle: {}
                }
            },
            lineStyle: {
                normal: {
                    color: 'source',
                    curveness: 0,
                    type: "solid"
                }
            }
        }]
    };

    myChart.setOption(option);
    myChart.on('click', function (param){
        // 打印出param, 可以看到里边有很多参数可以使用
        //获取节点点击的数组序号
        var arrayIndex = param.dataIndex;
        if (param.dataType == 'node') {
            var nodename=param.name;
            node_type=knowmap_data[nodename]["type"];
            if(node_type != 'entity'){
                console.log(node_type);
                redata(param.name);
            }
        }
        });
});

function redata(param){
    $.getJSON("/keywordrel_data?word="+param,function (data) {
        map_obj = document.getElementById("keywordmap");
        if (null == map_obj) return;

        var myChart = echarts.init(map_obj);

        myChart.showLoading();


        console.log('render keymap');

        var maplinks = data["r"];

        var node_data = {};
        var sourceflag = false;
        for(var dictkey in maplinks ){
            var infodict=maplinks[dictkey];
            if(!sourceflag){
                node_data[infodict["sourceNode"]]={
                    "name":infodict["sourceNode"],
                    "type":infodict["sourceType"],
                    "value":1.0
                };
                sourceflag =true;
            }
            node_data[infodict["targetNode"]]={
                    "name":infodict["targetNode"],
                    "type":infodict["targetType"],
                    "value":infodict["value"]
                }
        }
        knowmap_data = node_data;

        var nodes_keys = Object.keys(node_data);
        var nodes_num = nodes_keys.length;

        myChart.hideLoading();

        var categories = nodes_keys;

        for (i = 0; i < nodes_num; i++) {
            categories[i] = {
                name: nodes_keys[i]
            };
        }


        var links_num=maplinks.length;
        var links = [];

        for (i = 0; i < links_num; i++) {
            //处理links问题
            links.push({
                source: maplinks[i]['sourceNode'],
                target: maplinks[i]['targetNode'],
                name: maplinks[i]['relationName'],
                des: ''
                // des: tar['value'],
            });

        }


        //处理节点问题
        var node = [];
        for (i = 0; i < nodes_num; i++) {
            key = nodes_keys[i].name;
            node[i] = {
                name: key,
                // des:20,
                // symbolSize:Object.keys(element).length,
                symbolSize: 50*get_nodevalue(node_data[key]["value"]),
                category: key,   //会不会因为数字的原因无法加载
                //新增的一些特性
                draggable: "true"
            };

        }
        console.log(links);
        console.log(node);
        console.log(categories);


        option = {
            // 图的标题
            title: {
                // text: 'ECharts 关系图'
            },
            // 提示框的配置
            tooltip: {},
            // 工具箱
            toolbox: {
                // 显示工具箱
                show: true,
                feature: {
                    mark: {
                        show: true
                    },
                    // 还原
                    restore: {
                        show: true
                    },
                    // 保存为图片
                    saveAsImage: {
                        show: true
                    }
                }
            },
            legend: [{
                data: categories.map(function (a) {
                    return a.name;
                }),

                selectedMode: 'false',
                tooltip: {
                    show: true
                },
                bottom: 20,
                data: categories

            }],
            animationDuration: 3000,
            animationEasingUpdate: 'quinticInOut',
            backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
                offset: 0,
                color: '#f7f8fa'
            }, {
                offset: 1,
                color: '#cdd0d5'
            }]),
            series: [{
                name: '关键词',
                // 数据
                data: node,
                links: links,
                categories: categories,

                type: 'graph', // 类型:关系图
                layout: 'force', //图的布局，类型为力导图
                symbolSize: 30, // 调整节点的大小
                roam: true, // 是否开启鼠标缩放和平移漫游。默认不开启。如果只想要开启缩放或者平移,可以设置成 'scale' 或者 'move'。设置成 true 为都开启
                draggable: true,
                focusNodeAdjacency: true,

                //stype2
                label: {
                    position: 'right',
                    formatter: '{b}'
                },
                lineStyle: {
                    color: 'source',
                    curveness: 0.3
                },
                circular: {
                    rotateLabel: true
                },
                force: {
                    repulsion: 1000,
                    edgeLength: [150, 100],
                    friction: 0.5

                },
                label: {
                    normal: {
                        show: true,
                        position: 'top',
                        textstyle: {}
                    }
                },
                lineStyle: {
                    normal: {
                        color: 'source',
                        curveness: 0,
                        type: "solid"
                    }
                }
            }]
        };

        myChart.setOption(option);
        myChart.on('click', function (param){
        // 打印出param, 可以看到里边有很多参数可以使用
        //获取节点点击的数组序号
        var arrayIndex = param.dataIndex;
        if (param.dataType == 'node') {
            var nodename=param.name;
            node_type=knowmap_data[nodename]["type"];
            if(node_type != 'entity'){
                console.log(node_type);
                redata(param.name);
            }
        }
        });
    });
}

function get_nodevalue(node_value){
    if(node_value<0.3){
        return 0.3;
    }else if(node_value>0.8){
        return 0.8;
    }else{
        return node_value;
    }

}
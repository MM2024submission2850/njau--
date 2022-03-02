

$.getJSON("/keywordrel_data", function (data) {

    map_obj = document.getElementById("keywordmap")
    if (null == map_obj) return;

    var myChart = echarts.init(map_obj)

    myChart.showLoading();


    console.log('render keymap')

    nodes_keys = Object.keys(data)
    nodes_num = nodes_keys.length

    myChart.hideLoading();

    var categories = nodes_keys

    for (var i = 0; i < nodes_num; i++) {
        categories[i] = {
            name: nodes_keys[i]
        };
    }

    var links = []

    for (var i = 0; i < nodes_num; i++) {
        element = data[nodes_keys[i].name]


        element.forEach(tar => {
            //处理links问题
            links.push({
                source: tar['sourceNode'],
                target: tar['targetNode'],
                name: tar['related entity'],
                des: '',
                // des: tar['value'],
            })
        })
    }


    //处理节点问题
    var node = []
    var i = 0
    for (i = 0; i < nodes_num; i++) {
        key = nodes_keys[i].name

        element = data[key]
        node[i] = {
            name: key,
            // des:20,
            // symbolSize:Object.keys(element).length,
            symbolSize: 9,
            category: key,   //会不会因为数字的原因无法加载
            //新增的一些特性
            draggable: "true",
        }
    }


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
            data: categories,

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
                repulsion: 50,
                edgeLength: [10, 50],
                friction: 0.5,

            },
            label: {
                normal: {
                    show: true,
                    position: 'top',
                    textstyle: {},
                }
            },
            lineStyle: {
                normal: {
                    color: 'source',
                    curveness: 0,
                    type: "solid"
                }
            },


            // //style1
            // edgeSymbol: ['circle', 'arrow'],
            // edgeSymbolSize: [2, 10],
            // edgeLabel: {
            //     normal: {
            //         textStyle: {
            //             fontSize: 20
            //         }
            //     }
            // },
            // force: {
            //     repulsion: 2500,
            //     edgeLength: [10, 50]
            // },
            // draggable: true,
            // lineStyle: {
            //     normal: {
            //         width: 2,
            //         color: '#4b565b',
            //     }
            // },
            // edgeLabel: {
            //     normal: {
            //         show: true,
            //         formatter: function (x) {
            //             return x.data.name;
            //         }
            //     }
            // },
            // label: {
            //     normal: {
            //         show: true,
            //         textStyle: {}
            //     }
            // },

        }]
    };

    myChart.setOption(option);

});
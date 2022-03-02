// pages/daan/daan.js
import * as echarts from '../../ec-canvas/echarts';

const app = getApp();

var nodes=[];  //一些全局变量
var relation=[];
var question;

Page({
  data: {
    navbar: ['问句答案', '详细介绍'],
    currentTab: 0,
    answer:'',  //问句答案
    detail:'',   //详细信息
    imgpath:'',
    ec: {
      lazyLoad: true  //延迟加载
    }
  },
  
  navbarTap: function (e) {
    this.setData({
      currentTab: e.currentTarget.dataset.idx
    })
  },
  
  onLoad: function (options) {  //监听界面加载
    console.log('用户输入的问题是')
    question=options.question;   //接收上一个界面传递来的问题
    console.log(question)
    this.echartsComponnet = this.selectComponent('#mychart-dom-graph');
    this.getData(question);
  },

  getData: function (question){
    wx.request({   //连接后端，获取答案等
      //url: 'https://www.ccorpus.cn/query',
      url: 'http://127.0.0.1:8000/query',
      header: {
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method: "POST",
      data: { Question: question },
      success: res => {
        if (res.statusCode == 200) {
          console.log(res.data)
          this.setData({   
            answer: res.data.answer
          })
          this.setData({
            detail: res.data.detail
          })
          this.setData({
            imgpath: res.data.path
          })
          nodes=res.data.nodes  //接收后端传递来的节点和关系
          relation=res.data.links
          console.log('这是节点数据')
          console.log(nodes)
          console.log('这是关系数据')
          console.log(relation)
          this.init_echarts();//初始化图表
        }
      }
    })
  },

  init_echarts: function () {   //初始化图表
    this.echartsComponnet.init((canvas, width, height) => {
      const Chart = echarts.init(canvas, null, {
        width: width,
        height: height
      });
      Chart.setOption(this.getOption());
      return Chart;
    });
  },

  getOption: function () {    // 指定图表的配置项和数据
    var option = {
      title: {
        text: "非遗 | 子图展示",
        show: true,
        top: "top",
        left: "center",
        textStyle:{
          fontFamily:'monospace'
        }
      },
      tooltip: {},
      legend: [{    //图例
      formatter: function (name) {
      return echarts.format.truncateText(name, 40, '14px Microsoft Yahei', '…');
      },
      tooltip: {
        show: true
      },
      selectedMode: 'false',
      bottom: 20,
      data: ['project', 'person', 'type', 'area']
      }],
      toolbox: {   //工具栏
        show: true,
        feature: {
        dataView: {   //展示当前图表所用的数据
          show: false,
          readOnly: true
          },
        restore: {    //配置项还原
          show: true
          },
        saveAsImage: {   //保存为图片
          show: false
          }
        }
      },
      animationDuration: 3000,
      animationEasingUpdate: 'quinticInOut',
      series: [{
                  type: 'graph',
                  layout: 'force',    //力引导布局
                  force: {
                    repulsion: 120     //节点之间的斥力因子
                  },
                  data:nodes,    //节点数据列表
                  links:relation,   //关系数据
                  categories: [{    //节点分类的类目，可选
                   'name': '关系'    //类目名称，用于和 legend 对应以及格式化 tooltip 的内容
                    }, {
                      'name': 'project'
                    }, {
                      'name': 'person'
                    }, {
                      'name': 'type'
                    }, {
                      'name': 'area'
                    }],
                  focusNodeAdjacency: false, //鼠标移到节点上的时候突出显示
                  roam: true,    //开启鼠标缩放和平移漫游
                  label: {     //图形上的文本标签，可用于说明图形的一些数据信息
                    normal: {
                      show: true,
                      position: 'inside',    //还可以是inside
                    }
                  },
                  lineStyle: {    //关系边的公用线条样式
                    normal: {
                      color: 'source',
                      curveness: 0,    //边的曲度，值越大，边越弯
                      type: "solid"     //线的类型
                    }
                  }
                }]
      }
    return option;
  },

  onShareAppMessage: function (res) {   //用户点击右上角分享
    return {
      title: 'ECharts 可以在微信小程序中使用啦！',
      path: '/pages/index/index',
      success: function () { },
      fail: function () { }
    }
  }
})
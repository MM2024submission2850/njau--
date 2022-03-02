# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:14:57 2020

@author: 13284
"""

# worcloud是生成词云的关键
import wordcloud
# numpy是一个强大的科学计算库,我们将用它来把PIL库打开的图片保存为数组
import numpy as np
# PIL是一个图像处理库,用来打开图片
from PIL import Image
# jieba是中文分词库,可以智能地拆分词语
import jieba
# matplotlib库是一个绘图库,可以用来显示图片以及绘制多种图形
import matplotlib.pyplot as plt

# 生成背景图片的两种方法#
# 注意背景图片的路径要写对，可以是完整路径，例如C:/image/test.jpg
# 若图片与Python代码在同一个文件夹，那可以直接写图片名称+后缀，例如test.jpg
# 1.使用 matplotlib库读取图片
# background_image_1.jpg是背景图片的文件名，要替换为你自己的图片
#bg_1=plt.imread("background_image_1.jpg")

# 2.使用numpy库和PIL库，PIL库用于打开图片，numpy库用于将图片转化为数组
# 下面这行代码我注释掉了
# bg_2=np.array(Image.open('background_image_2.jpg'))

# 对于以上的图片选择，要特别注意图片的背景应该为白色
#配置词云的背景，图片，字体大小等参数，
# 也可以不配置，直接 wc=wordcloud.WordCloud()
wc=wordcloud.WordCloud(
  # font_path为字体文件的路径，如果没有这个，那么生成的词云图片无法显示中文
  font_path="C:/Windows/Fonts/simfang.ttf",

  # scale为按比例放大或者缩小生成的图片。例如1.5表示图片放大为原来的1.5倍，可省略
  scale=1.5,

  # mask表示背景图片，如果不没有背景图片，那这个可以省略
  #mask=bg_1,

  # background_color为背景颜色，默认为黑色，可以省略
  background_color="white",

  # width为词云生成的图片宽度，默认为400
  width=600,

  # height为词云生成的图片高度，默认为200
  height=400,

  # max_words图片上显示的最大词语的个数
  max_words=1000,

  # max_font_size为最大字体的大小
  max_font_size=220,

  # min_font_size为最小字体大小,默认为4
  min_font_size=4)

# 打开要生成词云的文件,一般是txt格式的纯文本文档
# 词云来源.txt 要替换成存有你要转化为词云的信息文件的文件名
with open(r'O:\wb\1.23zl.txt','r',encoding="utf-8") as f:

  # text=f.read()是说读取 词云来源.txt 这个文件的所有内容并存储到变量text中
  text=f.read()

  # 利用jieba库把text拆分并且使用空格分隔拆分后的结果
  spilt_text=" ".join(jieba.lcut(text))

print("正在生成词云......")

# 调用generate方法，传入要生成词云的文本即可生成词云

wc.generate(spilt_text)

# 把词云保存成图片
wc.to_file('wordcloud.jpg')

print("生成完毕!")
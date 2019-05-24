# 基于地图信息的数据可视化工具

## 前提准备
### python 模块
1. 安装python 3.x
2. 使用pip安装```folium```，```pandas```
```
pip install folium
pip install pandas
```
其中```pandas```用于实现数据筛选处理，```folium```用于实现数据可视化。
### 数据文件
- world-countries.json  
  地图信息文件
- database.sqlite  
  统计数据文件，下载链接：https://www.kaggle.com/worldbank/world-development-indicators

## 运行
本项目可使用Jupyter Notebook或Python命令行运行。个人建议使用Jupyter Notebook。
### 1. Jupyter Notebook

使用Jupyter Notebook打开```geo_visualize.ipynb```文件，运行第一个cell即可。  
程序将直接在网页显示数据可视化结果。

### 2. Python命令行

先将```geo_visualize.py```中的文件头部的```USE_JUPYTER_NB```设置为False
```python
USE_JUPYTER_NB   = False
```
之后再执行
```python
python geo_visualize.py
```
即可。注意，程序输出plot_data.html文件，若命令行提出SUCCESS则说明文件生成成功，请自行用浏览器打开查看。

## 说明
### 参数说明
- USE_JUPYTER_NB  
  是否使用Jupyter Notebook，默认为True
- SUPPRESS_WARNING  
  是否无视警告（代码中负责数据与地图信息绑定的函数会报Future Warning），默认为True
### 文件说明
- world-countries.json  
  地图信息文件
- plot_data.html  
  程序预期输出
- geo_visualize.py(ipynb)  
  源代码
  
## 更新
最新版本为GDV_Object_Oriented.py，针对面向对象对原代码进行重构

## 数据源与数据说明
https://www.kaggle.com/worldbank/world-development-indicators

## 引用
[1] https://medium.com/datadriveninvestor/visualising-geospatial-data-with-python-d3b1c519f31

# 基于地图信息的数据可视化工具

## 前提准备
1. 安装python 3.x
2. 使用pip安装```folium```，```pandas```
```
pip install folium
pip install pandas
```
其中```pandas```用于实现数据筛选处理，```folium```用于实现数据可视化。

## 运行
本项目可使用Jupyter Notebook或Python命令行运行。个人建议使用Jupyter Notebook。
1. Jupyter Notebook

使用Jupyter Notebook打开```geo_visualize.ipynb```文件，运行第一个cell即可。

2. Python命令行

先将```geo_visualize.py```中的文件头部的```USE_JUPYTER_NB```设置为False
```python
USE_JUPYTER_NB   = False
```
之后再执行
```python
python geo_visualize.py
```
即可

## 引用
[1] https://medium.com/datadriveninvestor/visualising-geospatial-data-with-python-d3b1c519f31

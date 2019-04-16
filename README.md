## 弹幕爬取

### 使用方法：

先获取所要爬取弹幕电影的cid号，调用脚本时输入cid号，输出的文件名即可，脚本会自动在当前目录下生成一个csv文件,所爬取的信息有发送内容，影片时间，发送时间，发送用户的ID

```bash
python bili_danmu_spider.py -i 'cid' -o 'filename'
```
### 参数说明：
1. ``-i``：输入excel文件的名称
2. ``-o``：输入数据要处理的列明
3. ``-n``或``--ncores``：处理是并行的线程数

示例：python bili_danmu_spider.py -i xxxxxxxx -o test.csv

如需要查看命令行参数可输入
```bash 
python bili_danmu_spider.py -h
```
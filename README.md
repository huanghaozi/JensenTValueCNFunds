> 2020-11-19 By HuangHao

# 使用说明

## 下载代码

`https://github.com/huanghaozi/JensenTValueCNFunds/archive/main.zip`

## 安装Python或Conda

并在安装时将其加入PATH环境变量，MiniConda清华源下载地址：
	
`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.8.3-Windows-x86_64.exe`
	
## 换源
	
运行命令：

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 解压
	
完整解压，记录解压路径
	
## 安装依赖环境
	
运行命令：
	
```shell
cd /d 路径		（将"路径"换为解压路径）
pip install -r requirements.txt
```
	
## 自定义代码
	
用记事本打开`fund_crawl_capm.py`
	
其中的`code_num`表示随机选取的基金数量（默认10只）
	
`index_code`表示指数代码（默认沪深300）
	
可自行修改
	
## 运行代码

```shell
python fund_crawl_capm.py
```
	
### 程序将输出所爬取的无风险利率、基金代码及其与指数回归所得的alpha的t值
### 程序会自动将原始数据输出至原始数据文件夹中
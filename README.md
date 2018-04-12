# ecmwfapi

从ecmwf下载数据的工具
http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/
1.如果您没有帐户，请通过
https://apps.ecmwf.int/registration/
进行自我注册，然后转到以下步骤。
2.登录
https://apps.ecmwf.int/auth/login/

3.通过
https://api.ecmwf.int/v1/key/  
获取密钥 
```
请注意，该密钥在1年内到期。您将在到期日期前1个月收到注册电子邮件地址的电子邮件，并附上续订说明。要查看当前密钥登录的到期日期，请访问
https://www.ecmwf.int
```
复制此页面中的信息，并将其粘贴到文件 
$ HOME / .ecmwfapirc（Unix / Linux）
或
％USERPROFILE％\ .ecmwfapirc（Windows)
.ecmwfapirc中的内容：
```json
{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "XXXXXXXXXXXXXXXXXX",
    "email" : "example@123.com"
}
```

您可以ecmwfapi 通过在Unix / Linux上运行来安装  python库：
```bash
pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz

```
或在Windows上：
```bash
pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz

```
要查看ECMWF Public Datasets的可用性，请访问Web界面：
http://apps.ecmwf.int/datasets/

下载文件的参数说明:
```python
#!/usr/bin/env python  
from ecmwfapi import ECMWFDataServer  
server = ECMWFDataServer()
    server.retrieve({
                'stream'    : "oper",
                #下载区域
                'area'      : "2/24/104/122", 
                'levtype'   : "sfc",
                #下载内容对应编号
                'param'     : "165.128/166.128", 
                #数据集
                'dataset'   : "interim",  
                #步长
                'step'      : "0",             
                #分辨率
                'grid'      : "0.25/0.25",     
                #时间0点/6点/12点/18点
                'time'      : "00:00:00/06:00:00/12:00:00/18:00:00",   
                #下载日期范围例如1996-01-01/to/2009-12-31
                'date'      : "1979-02-01/to/1979-02-28",            
                #再分析数据
                'type'      : "an",            
                'class'     : "ei",       
                #数据格式
                'format'    : "netcdf",    
                #输出位置（左斜线）及文件名    
                'target'    : "output.nc"  
            })
```




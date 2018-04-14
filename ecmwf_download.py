#!/usr/bin/env python
#-*- coding: utf-8 -*-
import linecache
from ecmwfapi import ECMWFDataServer
def downloadYear(syear = 2017,eyear = 2018):
    a=linecache.getlines("month.txt")
    for i in range(syear,eyear):#年份1996-2009
        if i%4==0:
            m=29
        else:
            m=28
        for j in range(1,13):#月份1到12月
            if j==2:
                b=m
            else:
                b=a[j-1]
            if j<10:
                y1="0"+str(j)
            else:
                y1=str(j)
            date=str(i)+"-"+y1+"-01/to/"+str(i)+"-"+y1+"-"+str(b)
            print date
            
            server = ECMWFDataServer()  
            server.retrieve({
                'stream'    : "oper",
                'area'      : "24/104/2/122", #下载区域
                'levtype'   : "sfc",
                'param'     : "165.128/166.128", #下载内容对应编号
                'dataset'   : "interim",  #数据集
                'step'      : "0",             #步长
                'grid'      : "0.25/0.25",     #分辨率
                'time'      : "00:00:00/06:00:00/12:00:00/18:00:00",   #时间0点/6点/12点/18点
                'date'      : date,            #下载日期范围例如1996-01-01/to/2009-12-31
                'type'      : "an",            #再分析数据
                'class'     : "ei",       
                'format'    : "netcdf",        #格式
                'target'    : "/Volumes/mage/res/taobao/ecmwf/out/"+str(i)+y1+".nc"  #输出位置（左斜线）及文件名
            })
    print "all have done!"


def testDownload():
    server = ECMWFDataServer()
    server.retrieve({
                'stream'    : "oper",
                'area'      : "24/104/2/122", #下载区域
                'levtype'   : "sfc",
                'param'     : "165.128/166.128", #下载内容对应编号
                'dataset'   : "interim",  #数据集
                'step'      : "0",             #步长
                'grid'      : "0.25/0.25",     #分辨率
                'time'      : "00:00:00/06:00:00/12:00:00/18:00:00",   #时间0点/6点/12点/18点
                'date'      : "1979-01-01/to/2017-12-31",            #下载日期范围例如1996-01-01/to/2009-12-31
                'type'      : "an",            #再分析数据
                'class'     : "ei",       
                'format'    : "netcdf",        #格式
                'target'    : "out/1979_2017.nc"  #输出位置（左斜线）及文件名
            })
def main():
    downloadYear()
    # testDownload()
    # 1979-02-01_1979-02-28

if __name__ == '__main__':
    main()

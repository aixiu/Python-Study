import time

#时间戳-->结构化时间
#time.gmtime(时间戳)    #UTC时间，与英国伦敦当地时间一致
#time.localtime(时间戳) #当地时间。例如我们现在在北京执行这个方法：与UTC时间相差8小时，UTC时间+8小时 = 北京时间 
print(time.gmtime())
print(time.localtime())

#结构化时间-->时间戳　
#time.mktime(结构化时间)
time_tuple = time.localtime()
print(time.mktime(time_tuple))

#结构化时间-->字符串时间
#time.strftime("格式定义","结构化时间")  结构化时间参数若不传，则显示当前时间
print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d",time.localtime()))

#字符串时间-->结构化时间
#time.strptime(时间字符串,字符串对应格式)
print(time.strptime("2017-03-16","%Y-%m-%d"))
print(time.strptime("07/24/2017","%m/%d/%Y"))
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@author:MrSprint
@file:to_timestamp.py
@time:2016 16-11-23 下午5:05
'''
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@author:MrSprint
@file:test.py
@time:2016 16-11-18 上午10:51
'''
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    re_day = r'^(\d+)\-([1-9]|1[0-2]|0[1-9])\-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[1-9])\s+(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
    re_utc = r'^(UTC)(\+|\-)(1[0-2]|0[1-9]|[0-9])\:(0*)$'
    try:
        re.match(re_day,dt_str).groups()
        utctime = re.match(re_utc,tz_str)
        cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        #utc_dt = cday.replace(tzinfo=timezone(timedelta(hours=int(utctime.group(3)))))#这一步必须有不然的话会出错误
        if utctime.group(2) == '+':
            utc_dt = cday.replace(tzinfo=timezone(timedelta(hours=int(utctime.group(3)))))  # 这一步必须有不然的话会出错误,将给定的时间设置成正确的时区
            #utctime_zero = utc_dt.astimezone(timezone(timedelta(hours=int(utctime.group(3)))))#进行时区的转换，转换成UTC时间,用这个必须和上一句一起用，不然报错。当然这句话没什么卵用，但是发现啦错误，所以留下来啦。
            return utc_dt.timestamp()  #加了时区的timestamp才是有意义的
        else:
            utc_dt = cday.replace(tzinfo=timezone(timedelta(hours=-int(utctime.group(3)))))  # 这一步必须有不然的话会出错误
            #utctime_zero = utc_dt.astimezone(timezone(timedelta(hours=-int(utctime.group(3)))))
            return utc_dt.timestamp()
    except:
        print( '时间格式不正确，清重新输入')


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
#print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
#print(t1)
print('Pass')
# Time2UTCtimestamp
将任意一个时区的时间转换成timestamp。

特别说明：有正则表达式，但有用正则表达式不能区分的如 2月30号，4月31号等，这些在逻辑上没有加以处理，如果输入2016-2-31这样的话会得到一个错误的timestamp。

解决办法时加上润年的判断和一个月是不是有31号即可。

Converts the time of any time zone to timestamp.

Special Note: There are regular expressions, but the regular expression can not distinguish between the use of such as February 30, April 31, etc., these are not dealt with in the logic, if the importation of 2016-2-31 This will be a mistake Timestamp.

When the solution with Run-year judgment and a month is not 31 can be

import re
new_no=[]
data='''Geographical Coverage: Cambodia China Fiji Indonesia Lao PDR Malaysia Mongolia More...
Economy Coverage: Blend High Income IBRD IDA Low Income Lower Middle Income Upper Middle Income
Number of Economies: 
121
Periodicity: 
Annual
Temporal Coverage: 
1999 - 2019
Release Date: 
October 28, 2019
Last Updated: 
October 30, 2019
Update Frequency: 
No further updates planned
Access Options:Query Tool, Download'''
no=sorted(set(re.findall("\d+",data)))
for i in no:new_no.append(int(i))
print(sorted(new_no))

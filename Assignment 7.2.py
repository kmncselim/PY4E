"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
```
X-DSPAM-Confidence:    0.8475
```

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at [http://www.py4e.com/code3/mbox-short.txt](https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=1591429c8869cb3a5494c135d155f554) 
when you are testing below enter **mbox-short.txt** as the file name.
"""
"""
Desired Output
Average spam confidence: 0.7507185185185187
"""
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        value = float(line[19:])
        total = value + total
        continue
    
average = total / count
print("Average spam confidence:", average)

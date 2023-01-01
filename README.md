Layla Mathematics is a python package that uses the code of C to make the eval syntax faster and more flexible.

Benchmarking: https://github.com/JewishLewish/Layla-Python-Module/blob/master/testing.py

Benchmark test:
    
    -> Loop 100,000 times
    
    -> Each time having an unique variable / output

Output:
i + 2:

      Python's Eval -> .90 seconds
  
      Layla's Math -> .15seconds


i + abs(i):
        
        Python's Eval -> ~1.04 seconds
        
        Layla's Math -> ~.14 seconds 
        
i + sin(i):
        
        Python's Eval DOESN'T SUPPORT IT 
        
        Layla's C Math -> ~.15 seconds

Layla Mathematics is mostly used for heavy mathematics. 

### Syntax

```
x = layla.math("2+2")
print(x) #-> 4
```

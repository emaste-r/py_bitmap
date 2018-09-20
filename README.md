# py_bitmap

## demo:
```
if __name__ == '__main__':

    bm = Bitmap(100)

    for i in [1, 3, 4, 5, 6, 78, 9, 90]:
        bm.set(i)

    bm.print_bitmap()

    bm.clear(5)

    bm.print_bitmap()
        
    print "40亿数字占用内存："
    big_bm = Bitmap(4 * 10 ** 9, init_array=False)

```

## 结果：
```
__init__: size=4
__init__: memory size=12.5 Byte, 0.012Kb, 0.000Mb, 0.000Gb 
set: 1
set: 3
set: 4
set: 5
set: 6
set: 78
set: 9
set: 90
print bitmap: [1, 3, 4, 5, 6, 9, 78, 90]
clear: 5
print bitmap: [1, 3, 4, 6, 9, 78, 90]
40亿数字占用内存：
__init__: size=125000001
__init__: memory size=500000000.0 Byte, 488281.250Kb, 476.837Mb, 0.466Gb 

```

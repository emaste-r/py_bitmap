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

    big_bm = Bitmap(10 ** 9, init_array=False)

```

## 结果：
```
__init__: size=4
__init__: memory size=12 Byte, 0.012Kb, 0.000Mb, 0.000Gb 
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
__init__: size=31250001
__init__: memory size=125000000 Byte, 122070.312Kb, 119.209Mb, 0.116Gb 

```

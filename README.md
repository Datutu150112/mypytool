# mypytool
一个有许多功能的python库
（由于本人十一岁能力有限，代码水平不高请谅解）

## 安装方法

```
pip install mypytool
```

## 功能介绍

### main.py

- `perfect_square_plus_gs` 完全平方和公式
- `perfect_square_plus_z` 完全平方和值
- `perfect_square_sub_gs` 完全平方差公式
- `perfect_square_sub_z` 完全平方差值
- `bytes2gray` 以格雷码形式编码
- `gray2bytes` 解码格雷码
- `base_conversion` 将x转换成y进制
- `fibonacci_recursion` 求斐波那契的第n项值
- `fibonacci` [公式](https://en.wikipedia.org/wiki/Fibonacci_sequence#Closed-form_expression)求斐波那契数列。由于浮点数精度问题，计算的结果会极为不正确

### linked_list.py

- class `GeneralLinkedList` 单向链表
- class `CycleLinkedList` 循环链表

### graghic.py

- class `Circle` 圆
- class `Square` 正方形
- class `Rectangle` 长方形
- class `Triangle` 三角形
- class `Parallelogram` 平行四边形
- class `Trapezoid` 梯形

## 更新日志

- 0.2
  - 直接导入 `mypytool` 时不会再导入 `graghic.py` 和 `linked_list.py` 了
  - main.py
    - 加入了 `fibonacci` 函数。终于！困扰在人们心中斐波那契数列的第0.5项是什么的问题终于被解决了
      - 由于浮点数精度问题，计算的结果会极为不正确（小声）
    - 移除了 `fast_pow` 和 `pow`，请使用 `**` 或 `math.pow`
    - 移除了 `factorial_recursion`，请使用 `math.factorial`
    - 移除了 `base_conversion_dex`，请使用 `int("".join(map(str, x)), 2)`
    - 移除了 `swap`, `swap1` 和 `swap2`
    - `base_conversion` 现在是 `base_conversion(n: int, target_base: int) -> str` 而非 `base_conversion(x: int, y: int) -> list[int]`
    - 调整了 `perfect_square_plus_gs` / `perfect_square_plus_z` / `perfect_square_sub_gs` / `perfect_square_sub_z`
      - 所有参数列表由 `(x, y)` 改为 `(a, b)`
      - `perfect_square_plus_gs` / `perfect_square_sub_gs` 将应当返回一个合法的python表达式
    - 添加了 `bytes2gray` 和 `gray2bytes` 函数，作用稍后提到
    - 移除了 `glm` 函数，请使用 `list(map(int, bin(int.from_bytes(bytes2gray(int.to_bytes())))[2:]))`
    - 移除了 `glm2bin` 函数，请使用 `list(map(int, bin(int.from_bytes(gray2bytes(int("".join(map(str, )), base=2).to_bytes())))[2:]))`
    - 移除了 `glm2dex` 函数，请使用 `int.from_bytes(gray2bytes(int("".join(map(str, )), base=2).to_bytes()))`
      - （这恰巧说明了之前的实现有多么的不正确）
  - linked_list.py
    - 重命名 General_Linked_list -> GeneralLinkedList
    - 重命名 Cycle_Linked_list -> CycleLinkedList
  - graghic.py
    - 更新了 graghic.py 的内部实现，变化较大
  - 移除了整个 stack.py，请使用列表
  - 移除了整个 date.py，请使用 `calendar` 标准库
  - 移除了整个 queue.py，请使用 `queue.Queue`
  - 移除了整个 sort.py，请使用 `sorted`

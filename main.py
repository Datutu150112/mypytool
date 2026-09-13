from math import sqrt


# region perfect_square_*
def perfect_square_plus_gs(a, b) -> str:
    """完全平方和公式

    给定 `(a + b) ** 2` 中的 `a` `b`，
    将给定的值填入后输出 `a**2 + b**2 + 2*a*b` 这一字符串。

    返回的结果应当是合法的python表达式
    """
    return f"{a}**2 + {b}**2 + 2*{a}*{b}"


def perfect_square_plus_z(a, b):
    return a**2 + b**2 + 2*a*b  # fmt: skip


def perfect_square_sub_gs(a, b) -> str:
    """完全平方差公式

    给定 `(a - b) ** 2` 中的 `a` `b`，
    将给定的值填入后输出 `a**2 + b**2 - 2*a*b` 这一字符串。

    返回的结果应当是合法的python表达式
    """
    return f"{a}**2 + {b}**2 - 2*{a}*{b}"


def perfect_square_sub_z(a, b):
    return a**2 + b**2 - 2*a*b  # fmt: skip


# endregion


def bytes2gray(data: bytes) -> bytes:
    """
    将 bytes 中的每个字节按位转换为格雷码（Gray code）。
    规则：gray = binary ^ (binary >> 1)
    """
    return bytes(bytearray(b ^ (b >> 1) for b in data))


def gray2bytes(data: bytes) -> bytes:
    """
    将格雷码转换回原始二进制数据（逐字节逆向）。
    格雷码转二进制的规则：从高位到低位，逐位异或。
    """
    result = bytearray()
    for g in data:
        binary = g
        mask = binary >> 1
        while mask:
            binary ^= mask
            mask >>= 1
        result.append(binary)
    return bytes(result)


def base_conversion(n: int, target_base: int) -> str:
    s = ""
    while n > 0:
        s += str(n % target_base)
        n //= target_base
    return s[::-1]


PHI = (1 + sqrt(5)) / 2


def fibonacci(n: complex) -> complex:
    # https://en.wikipedia.org/wiki/Fibonacci_sequence#Binet's_formula
    return (PHI**n - (-PHI)**n) / sqrt(5)  # fmt: skip


def fibonacci_recursion(n: int) -> int:
    if n < 0:
        # 报错是直接从 math.factorial 上复制的
        raise ValueError("fibonacci_recursion() not defined for negative values")
    elif n <= 2:
        return 1

    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def pow_transform(x, y, n=2) -> str:
    return f"{x**n}**{y // n}"

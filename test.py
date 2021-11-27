def stringShift(self, s: str, shift: List[List[int]]) -> str:
    l, ls, rs = len(s), 0, 0
    for direction, amount in shift:
        if direction == 0:
            ls += amount
        else:
            rs += amount
    ls = ls % l
    rs = rs % l
    if ls == rs:
        return s
    elif ls > rs:
        ls = ls - rs
        return s[ls:]+s[:ls]
    else:
        rs = rs - ls
        return s[-rs:]+s[:-rs]

shift = [[0,1],[1,2]]

stringShift("abc", shift)
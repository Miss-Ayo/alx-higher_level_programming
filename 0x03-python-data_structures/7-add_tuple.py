#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        List_a = list(tuple_a)
        List_b = list(tuple_b)
        for i in range(2):
            List_a.append(0)
            List_b.append(0)
        sum_0 = List_a[0] + List_a[0]
        sum_1 = List_a[1] + List_a[1]
        tuple_c = (sum_0, sum_1)
        return tuple_c
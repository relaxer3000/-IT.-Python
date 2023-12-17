# TODO Найдите количество книг, которое можно разместить на дискете

v_disk = 1.44
stranitsi = 100
stroki = 50
simvoli = 25
simv_ves = 4

v_kn = (simv_ves * simvoli * stroki * stranitsi) / (1024 ** 2)
k = v_disk // v_kn
k = int(k)
print("Количество книг, помещающихся на дискету:", k)

python3 -m cProfile -o factorial.prof factorial.py
pyprof2calltree -i factorial.prof -o callgrind.out.1
kcachegrind callgrind.out.1

#!/bin/bash

for i in 1 2 5 10 20 50 100 200 500 1000 2000 5000 10000 20000 50000 100000 200000 500000 1000000 ; do
   echo "$i initial states"
   echo "set_prolog_stack(global, limit(10**9)), command('pac_learning(library:examples/Th_lymphocytes/lympho.bc, $i , $((1000000 / i)))')." | biocham_debug > pac_$i.log
done

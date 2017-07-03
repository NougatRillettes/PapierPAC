#!/bin/bash

if [[ "$1" =~ "--" ]] ; then
   term=${1##--}
   shift
   png="set term $term; set output 'statistics.$term'"
fi
tmpfile=$(mktemp -t $(basename $0))
{
   for logfile in "$@" ; do
      sed -n -e 's/% \(.*\) samples (max h ~.*\..*)$/\1/p' "$logfile" | \
         python3 -c "import sys; import statistics; \
         data = [int(x) for x in sys.stdin]; \
         print('$logfile'.split('_')[1].split('.')[0], end='\t'); \
         print(min(data), end='\t'); print(statistics.stdev(data), end='\t')"
      sed -n -e 's/^\([^%].*-[<>].*\)$/\1/p' "$logfile" | sort -k 2 -t '-' | \
         diff -U0 reference.log - | sed -n -e 's/^[+-][^+-].*$/\0/p' | \
         wc -l | sed -e 's/^ *//'
   done
} > "$tmpfile"
gnuplot -persist - <<EOF
$png
set key center top
set termoption linewidth 2
set style data lines
set xlabel "Number of initial states"
set ylabel "standard deviation of the numbers of samples"
# set y2label "minimum number of samples"
# set ytics nomirror
# set y2tics
set log x
# plot "$tmpfile" using 1:2 axes x1y2 title "min" smooth unique, \
#    "$tmpfile" using 1:3 axes x1y1 title "stdev" smooth unique
set ylabel "edit distance w.r.t reference model"
plot "$tmpfile" using 1:4 title "distance" smooth unique
EOF
cat "$tmpfile"
rm "$tmpfile"

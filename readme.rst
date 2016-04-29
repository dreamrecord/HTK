HTK
===

Heres are some useful HTK initial model generators.

1. genProto.py

| A python code to generate lib/proto file.

| Usage:
| python genProto.py -s [# of states] -o [outputPath]

::

    python genProto.py -s 5 -o lib/proto

2. genMix.py

| A python code to generate lib/mix2_10.hed file

| Usage:
| python genMix.py -s [# of states] -g [# of Gaussian mixtures per state] -o [outputPath]

::

    python genMix.py -s 5 -g 10 -o lib/mix2_10.hed

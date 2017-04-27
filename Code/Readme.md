Readme
======

This directory contains code and description for the experiments detailled in **TO_DO**.

Files organization
------------------

It is organized as follow

```
.
├── DataGen
│   ├── boolGillespie.py
│   ├── gillespie.py
├── examples
│   ├── <name>.reac
│   ├── <name>.hints
│   ├── <name>.infl
│   └── <name>.res
├── pac.py
└── Readme.md
```

The top level consists of two file, this `Readme` and a
Python implementation of the algorithm for PAC-learning in
`pac.py`.

The `examples` directory contains examples files. `reac`
files contain either reaction *or* influence systems,
`hints` files contain JSON, `infl` files (a name that can be
misleading) actually contain results of one of the two
script of `DataGen`, and finally `res` files contain the
output of PAC learning on those files. 

The `DataGen` directory contains code that implement the
gillespie algorithm and a boolean variant of it. The vanilla
gillespie algorithm works on reaction whereas its boolean
counterpart works on influence systems.

Workflow
--------

For details on invocaton, scripts should be called with the
`--help` option.

An illustration of the common workfow is given below:

```

+---------+  gillespie.py
| Reaction+----+            +--------+
|  System |    |            |Positive|
+---------+    +----------> |        |
+---------+    |            |Examples|
|Influence+----+            +----+---+
|  System |  boolGillespie.py    |
+---------+                      |
                                 |  pac.py
                                 |
                                 v
                             +---+-----+
                             | Results |
                             +---------+
```

pymining - A collection of data mining algorithms in Python
===========================================================

:Authors:
  Barthelemy Dagenais
:Version: 0.2

pymining is a small collection of data mining algorithms implemented in Python.
I did not design any of the algorithms, but I use them in my own research so I
thought other developers might be interested to use them as well.

I started this small project because I could not find data mining algorithms
that were easily accessible in Python. Moreover, the libraries I am aware of
often include old algorithms that have been surpassed by newer ones.


.. image:: https://github.com/antoinebou12/pymining/raw/main/.github/coverage_badge.svg


Requirements
------------

pymining has been tested with Python 2.7 and 3.4.


Installation
------------

::

    pip install pymining


Usage
-----

**Frequent Item Set Mining**

::

    >>> from pymining import itemmining
    >>> transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))
    >>> relim_input = itemmining.get_relim_input(transactions)
    >>> report = itemmining.relim(relim_input, min_support=2)
    >>> report
    {frozenset(['c']): 4,
    frozenset(['c', 'b']): 3,
    frozenset(['a', 'c']): 2,
    frozenset(['b']): 4,
    frozenset(['a']): 3}

    >>> # Test performance of multiple algorithms
    >>> from pymining import perftesting
    >>> perftesting.test_itemset_perf()
    Random transactions generated with seed None

    Done round 0
    Done round 1
    ...


**Association Rules Mining**

::

    >>> from pymining import itemmining, assocrules, perftesting
    >>> transactions = perftesting.get_default_transactions()
    >>> relim_input = itemmining.get_relim_input(transactions)
    >>> item_sets = itemmining.relim(relim_input, min_support=2)
    >>> rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)
    >>> rules
    [(frozenset(['e']), frozenset(['b', 'd']), 2, 0.6666666666666666),
    (frozenset(['b', 'e']), frozenset(['d']), 2, 1.0),
    (frozenset(['e', 'd']), frozenset(['b']), 2, 0.6666666666666666),
    (frozenset(['a']), frozenset(['b', 'd']), 2, 0.5),
    ...
    >>> # e -> b, d with support 2 and confidence 0.66
    >>> # b, e -> d with support 2 and confidence 1


**Frequent Sequence Mining**

::

    >>> from pymining import seqmining
    >>> seqs = ( 'caabc', 'abcb', 'cabc', 'abbca')
    >>> freq_seqs = seqmining.freq_seq_enum(seqs, 2)
    >>> sorted(freq_seqs)
    [(('a',), 4), (('a', 'a'), 2), (('a', 'b'), 4), (('a', 'b', 'b'), 2), (('a', 'b', 'c'), 4),
     (('a', 'c'), 4), (('b',), 4), (('b', 'b'), 2), (('b', 'c'), 4), (('c',), 4), (('c', 'a'), 3),
     (('c', 'a', 'b'), 2), (('c', 'a', 'b', 'c'), 2), (('c', 'a', 'c'), 2), (('c', 'b'), 3),
     (('c', 'b', 'c'), 2), (('c', 'c'), 2)]


Status of the project
---------------------

Three algorithms are currently implemented to find frequent item sets. Relim is
the recommended algorithm as it outperforms the two others (SaM and FP-growth)
in all of my benchmarks. This is probably due to my lazy implementation of
FP-growth.

The pruning option in FP-growth makes the algorithm slow and is turned to False by default for
now. This is surprising because pruning the tree should make it faster.

One algorithm is currently implemented to find association rules from frequent
item sets (generated by any algorithm).

One algorithm is implemented to find frequent sequences. I'll work on the space
efficiency soon.


Todo
----

#. More testing.
#. **Closed** Frequent sequence mining algorithm (a frequent sequence mining
   algorithm has been implemented though)
#. Improve performance with better Python operations and algorithms :-)


About performance
-----------------

All algorithms are implemented in Python and not in a C extension. The library
does not require any dependency and can thus be installed in almost any Python
environment.

The performance does increase with pypy and its jit. In one of my benchmark,
FP-growth went from 100 seconds with cpython to 23 seconds with pypy and relim
went from 23 seconds to 4 seconds.

Keys in transactions should be integers or small strings for best performance.


License
-------

This software is licensed under the `New BSD License`. See the `LICENSE` file
in the for the full license text.


References
----------

Relim and Sam were designed by Christian Borgelt:

Simple Algorithms for Frequent Item Set Mining, Christian Borgelt, Chapter 16
of: J. Koronacki, Z.W. Raz, S.T. Wierzchon, and J.K. Kacprzyk (eds.), Advances
in Machine Learning II (Studies in Computational Intelligence 263), 351-369,
Springer-Verlag, Berlin, Germany 2010, doi:10.1007/978-3-642-05179-1_16


FP-Growth was designed by Han et al.:

Mining Frequent Patterns without Candidate Generation, J. Han, H. Pei, and Y.
Yin, Proceedings of the Conference on the Management of Data (SIGMOD'00,
Dallas, TX), 1-12, ACM Press, New York, NY, USA 2000


Association Rules Mining is a general algorithm. I used the `course slides
from Bing Liu
<http://www.cs.uic.edu/~liub/teach/cs583-fall-05/CS583-association-rules.ppt>`_
at the University of Illinois.


Frequent Sequence Mining enumeration is a general algorithm. I used the
description in:

Frequent Closed Sequence Mining without Candidate Maintenance, J. Wang, J. Han,
and C. Li, IEEE Trans. on Knowledge and Data Engineering 19(8):1042-1056, IEEE
Press, Piscataway, NJ, USA 2007


Changelog
---------

0.1 - 16 Aug 2011
~~~~~~~~~~~~~~~~~

Initial release!


0.2 - 10 Aug 2015
~~~~~~~~~~~~~~~~~

- Fixed bug with assoc rule mining: some rules matching the confidence
  threshold were not computed.
- Fixed bug with the installer: seqmining was not included.

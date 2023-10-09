from collections import defaultdict
from typing import List, Tuple, Set, Dict

def freq_seq_enum(sequences: List[Tuple[str, ...]], min_support: int) -> Set[Tuple[str, ...]]:
    """Enumerates all frequent sequences.

    Args:
        sequences: A list of sequences (each sequence is a tuple of strings).
        min_support: The minimum support for a sequence to be considered frequent.

    Returns:
        A set of frequent sequences.
    """
    freq_seqs = set()
    _freq_seq(sequences, tuple(), 0, min_support, freq_seqs)
    return freq_seqs

def _freq_seq(
    sdb: List[Tuple[str, ...]], 
    prefix: Tuple[str, ...], 
    prefix_support: int, 
    min_support: int, 
    freq_seqs: Set[Tuple[str, ...]]
):
    if prefix:
        freq_seqs.add((prefix, prefix_support))
    for item, support in _local_freq_items(sdb, min_support).items():
        if support >= min_support:
            new_prefix = prefix + (item,)
            new_sdb = _project(sdb, new_prefix)
            _freq_seq(new_sdb, new_prefix, support, min_support, freq_seqs)

def _local_freq_items(sdb: List[Tuple[str, ...]], min_support: int) -> Dict[str, int]:
    items_count = defaultdict(int)
    for entry in sdb:
        for item in set(entry):
            items_count[item] += 1
    return {item: support for item, support in items_count.items() if support >= min_support}

def _project(sdb: List[Tuple[str, ...]], prefix: Tuple[str, ...]) -> List[Tuple[str, ...]]:
    if not prefix:
        return sdb
    new_sdb = []
    current_prefix_item = prefix[-1]
    for entry in sdb:
        try:
            index = entry.index(current_prefix_item) + 1
            new_sdb.append(entry[index:])
        except ValueError:
            continue
    return new_sdb

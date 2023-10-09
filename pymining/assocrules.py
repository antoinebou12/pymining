from typing import Set, List, Dict, Tuple, Deque
from collections import deque

def mine_assoc_rules(isets: Dict[Set[str], int], min_support: int = 2, min_confidence: float = 0.5) -> List[Tuple[Set[str], Set[str], int, float]]:
    rules: Deque[Tuple[Set[str], Set[str], int, float]] = deque()
    visited: Set[Tuple[Set[str], Set[str]]] = set()

    for key in sorted(isets, key=len, reverse=True):
        support = isets[key]
        if support < min_support or len(key) < 2:
            continue

        for item in key:
            left = key.difference([item])
            right = frozenset([item])
            _mine_assoc_rules(
                left, right, support, visited, isets,
                min_support, min_confidence, rules)

    return list(rules)

def add_rule_if_confident(left: Set[str], right: Set[str], rule_support: int, isets: Dict[Set[str], int], min_confidence: float, rules: Deque[Tuple[Set[str], Set[str], int, float]]) -> None:
    support_a = isets[left]
    confidence = rule_support / float(support_a)
    if confidence >= min_confidence:
        rules.append((left, right, rule_support, confidence))

def _mine_assoc_rules(
        left: Set[str], right: Set[str], rule_support: int, visited: Set[Tuple[Set[str], Set[str]]], isets: Dict[Set[str], int], min_support: int,
        min_confidence: float, rules: Deque[Tuple[Set[str], Set[str], int, float]]) -> None:
    if len(left) < 1 or (left, right) in visited:
        return

    visited.add((left, right))
    add_rule_if_confident(left, right, rule_support, isets, min_confidence, rules)

    for item in left:
        new_left = left.difference([item])
        new_right = right.union([item])
        _mine_assoc_rules(
            new_left, new_right, rule_support, visited, isets,
            min_support, min_confidence, rules)

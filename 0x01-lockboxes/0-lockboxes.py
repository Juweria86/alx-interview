#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""

    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_boxes = keys.pop()
        for key in boxes[current_boxes]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)
    return len(unlocked) == n

#!/usr/bin/python3
"""This function will determine if boxes can be unlocked
"""


def canUnlockAll(boxes):
    """To determine if the boxes can be opened"""

    opened = [False] * len(boxes)
    opened[0] = True
    lineup = [0]
    while lineup:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                lineup.append(key)
    return all(opened)

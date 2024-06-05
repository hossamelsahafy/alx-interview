#!/usr/bin/python3
def canUnlockAll(boxes):
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True
    stack = [key for key in boxes[0]]
    while stack:
        key = stack.pop()
        if key < len(boxes):
            if not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.extend(boxes[key])
    return all(unlocked_boxes)

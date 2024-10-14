#!/usr/bin/python3

""" Solving the locked box problem """


from queue import Queue


def canUnlockAll(boxes):
    """ usin BSF algorithm """

    q = Queue(maxsize=len(boxes))
    q.put(0)
    visited = []

    while (q.empty() is False):
        n = q.get()
        node = boxes[n]
        for i in node:
            if i not in visited:
                q.put(i)
        if n not in visited:
            visited.append(n)
    return len(visited) == len(boxes)

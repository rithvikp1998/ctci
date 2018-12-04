'''
Famous problem, straight-forward solution

Let's assume there is a stack of 5 disks, with
sizes from 1 to 5, on the left most tower and we
need to move it to the right most tower and the
middle tower can be used as a buffer.

Consider the subStack of 4 disks, we treat this as
a separate entity and the 5th disk as a separate
entity. Then, in order to move the 5 disk stack:

1. Move the subStack from left tower to middle tower
2. Move the 5th disk to the right tower
3. Move the subStack from middle tower to right tower

Note that moving the subStack of 4 disks is independent
of the 5th disk.
'''

def moveStack(stack, fromTower, toTower, bufferTower):
    if stack==[]:
        return

    moveStack(stack[:-1], fromTower, bufferTower, toTower)
    print('Moving disk', stack[-1], 'from', fromTower, 'to', toTower)
    moveStack(stack[:-1], bufferTower, toTower, fromTower)

n=int(input())
moveStack([i for i in range(1,n+1)], 'Left Tower', 'Right Tower', 'Middle Tower')

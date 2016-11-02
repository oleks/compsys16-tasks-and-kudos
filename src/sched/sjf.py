#!/usr/bin/env python3

import sys

max_ticks = 1000

class Task:
  def __init__(self, name, arr, exe):
    self.name = name
    self.arr = arr
    self.exe = exe
  def __lt__(self, other):
    return (self.arr, self.exe) < (other.arr, other.exe)

tasks = []

with open(sys.argv[1], "r") as f:
  text = f.readlines()

for task in text:
  task = task.split(" ")

  name = task[0]
  arr = int(task[1])
  exe = int(task[2])

  tasks.append(Task(name, arr, exe))

# Python's sort is stable
tasks = sorted(tasks)

ticks = 0
seq = []
while len(tasks) > 0 and ticks < max_ticks:
  t = tasks.pop(0)
  if t.arr < ticks:
    ticks = t.arr
  seq.append("{}{}".format(t.name, t.exe))
  ticks += t.exe

print(" ".join(seq))
print("Time elapsed: {}".format(ticks))

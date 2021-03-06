#!/usr/bin/env python3

import sys, bisect
import common

max_ticks = 1000
timeslice = 5

class Task:
  def __init__(self, name, arr, exe):
    self.name = name
    self.arr = arr
    self.exe = exe
  def __lt__(self, other):
    return self.arr < other.arr

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

arrival = { t.name : t.arr for t in tasks }
firstrun = { }
completion = { }

ticks = 0
seq = []
while len(tasks) > 0 and ticks < max_ticks:
  t = tasks.pop(0)
  if not t.name in firstrun:
    firstrun[t.name] = ticks

  if t.arr < ticks:
    ticks = t.arr
  exe = min(t.exe, timeslice)
  seq.append("{}{}".format(t.name, exe))
  ticks += exe
  t.exe -= exe
  t.arr += exe
  if t.exe != 0:
    bisect.insort_right(tasks, t)
  else:
    completion[t.name] = ticks

print(" ".join(seq))
print("Time elapsed: {}".format(ticks))

common.show_turnaround(completion, arrival)
common.show_response(firstrun, arrival)

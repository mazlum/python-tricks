from collections import Counter, deque
from queue import Queue

# Counter
cnt = Counter()
lessons = {"math": 2, "chemistry": 1}

cnt.update(lessons)

more_lessons = {"physics": 2, "math": 1}
cnt.update(more_lessons)

print(cnt)
"""Çıktı
Counter({'math': 3, 'physics': 2, 'chemistry': 1})
"""

# deque => double-ended queue (https://en.wikipedia.org/wiki/Double-ended_queue)
q = deque()
q.append("eat")  # Add eat to the right side of the deque.
q.append("sleep")
q.append("code")
print(q)
# deque(['eat', 'sleep', 'code'])
q.pop()
print(q)
# deque(['eat', 'sleep'])
q.popleft()
print(q)


# Queue
# synchronized and provides locking semantics to support multiple concurrent producers and consumers
q = Queue()
q.put("eat")
q.put("sleep")
q.put("code")
print(q)

q.get()
q.get_nowait()

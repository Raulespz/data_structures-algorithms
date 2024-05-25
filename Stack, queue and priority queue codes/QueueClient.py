from Queue import *

queue = Queue(10)

for person in ['Don', 'Ken', 'Ivan', 'Raj', 'Amir', 'Adi']:
    queue.insert(person)

print(f"After inserting {len(queue)} persons on the queue, it contains:\n{queue}")
print(f'Is queue full? {queue.isFull()}')

print('Removing items from the queue:')
while not queue.isEmpty():
    print(queue.remove(), end=' ')
print()

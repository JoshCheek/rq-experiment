from redis import Redis
from rq import Queue
from time import sleep
from my_module import count_words_at_url

q = Queue(connection=Redis())

# Delay execution of count_words_at_url('http://nvie.com')
job = q.enqueue(count_words_at_url, 'http://nvie.com')
print job.result

# Now, wait a while, until the worker is finished
sleep(2)
print job.result

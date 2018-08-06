RQ Experiment
-------------

Experiment to see how to work with [rq](http://python-rq.org/docs/).

Setup
-----

Uhm. Notes for me, and I use [fish](https://fishshell.com/), so they probably won't work for you 🤷

```fish
brew services start redis                # Start redis
conda create -n ascent_sculpt python=2.7 # Create the environment like this:
conda activate ascent_sculpt             # Switch to the environment

# Install dependencies
pip install rq
pip install redis
pip install requests
```

Run
---


```fish
# In tab 1:
  conda activate ascent_sculpt # Switch to the environment
  rq worker                    # Start the worker

# In tab 2:
  conda activate ascent_sculpt # Switch to the environment
  python run.py                # Enqueue the job:
```

Example comes from [here](http://python-rq.org/docs/).

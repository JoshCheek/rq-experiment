RQ Experiment
-------------

Experiment to see how to work with [rq](http://python-rq.org/docs/).

Setup
-----

Uhm. Notes for me, and I use [fish](https://fishshell.com/), so they probably won't work for you 🤷

```fish
brew services start redis                             # Start redis
conda create -n rq-experiment python=2.7              # Create the environment like this:
source (conda info --root)/etc/fish/conf.d/conda.fish # Load `conda` into the shell

# Install dependencies
pip install rq
pip install redis
pip install requests
```

Run
---


```fish
# In tab 1:
  conda activate rq-experiment # Switch to the environment
  rq worker                    # Start the worker

# In tab 2:
  conda activate rq-experiment # Switch to the environment
  python run.py                # Enqueue the job:
```

Example comes from [here](http://python-rq.org/docs/).

# funcGPT
A function decorator that tries to execute a function using GPT based on the function's name.

# How to use
```python
import funcGPT

@funcGPT.funcGPT
def nth_fibonacci(n):
    return

print(nth_fibonacci(5))
```

# Requirements
- Python 3.8 or higher
- An OpenAI API key
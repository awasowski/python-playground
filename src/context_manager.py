from contextlib import contextmanager

@contextmanager
def simple_context():
    print("Entering the context")
    try:
        yield
    finally:
        print("Exiting the context")


# Usage
with simple_context():
    print("Inside the context")

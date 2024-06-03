class SimpleContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        # You can handle exceptions here if needed
        return False  # Propagate exceptions, if any


# Usage
with SimpleContext():
    print("Inside the context")

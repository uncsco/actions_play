def hello(s: str) -> str:
    return f"Hello, {s}!"
  
def test_hello():
    assert hello("World") == "Hello, World!"

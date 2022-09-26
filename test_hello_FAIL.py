def hello(s: str) -> str:
    return f"Hello, {s}!"
  
def test_hello_fail():
    assert hello("World") == "Hello... World"
 
if __name__ == "__main__":
    test_hello_fail()  #// Should FAIL

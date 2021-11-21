import main

def test() :
  assert main.sub(89, 56) == 33
  
  assert main.sub(12, 9) == 3

if __name__ == '__main__':
  print(test())

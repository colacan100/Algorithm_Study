# 캡슐화코드

class Encap:
  def __init__(self,value):
    self.value = value
    print('init :', self.value)

  def _set(self):
    print('set :', self.value)

  def printTest(self):
    print('printTest :', self.value)

  # def __printTest2(self):
  #   print('printTest :', self.value)

# object 생성
e = Encap(10)

# object 실행 
# 케이스1
e.__init__(20)
e._set()
e.printTest()
#e.__printTest2()


print('\n')

# 케이스2
e.__init__(30)
e._set()
e.printTest()
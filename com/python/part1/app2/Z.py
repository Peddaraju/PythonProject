'''
Created on 28-Jan-2018

@author: Raju
'''
class Z():
    
    def main(self):
        print('Hello World!..')
        i = 10
        Z.test(self, i, i+20)
        
    def test(self, a, b):
        print(a+b)
        
obj = Z()
obj.main()
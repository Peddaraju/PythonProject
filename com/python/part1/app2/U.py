'''
Created on 27-Jan-2018

@author: Raju
'''

class U(object):
    def test1(self):
        print('from test1')
        
    def main(self):
        print('main begin')
        U.test1(self)
        print('========')
        U.test2(self)
        print('main end')
        
    def test2(self):
        print('from test2')  

obj = U()
obj.main()
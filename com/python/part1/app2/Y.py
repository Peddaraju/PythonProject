'''
Created on 27-Jan-2018

@author: Raju
'''
class Y():
    def main(self):
        print('Hello World')
        Y.test(10)
        
    def test(self, params):
        print('from test', params)
        
obj = Y()
obj.main()
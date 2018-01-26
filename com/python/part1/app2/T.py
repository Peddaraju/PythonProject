'''
Created on 27-Jan-2018

@author: Raju
'''
class T():
    
    def test1(self):
        print('from test1')
        
    def main(self):
        print('from main')
        T.test2(self)
        T.test1(self)
        T.test2(self)
    
    def test2(self):
        print('from test2')
        
        
obj = T()
obj.main()
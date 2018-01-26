'''
Created on 26-Jan-2018

@author: Raju
'''
class S():
    def main(self):
        print('from main')
        S.test(self)
        
    def test(self):
        print('from test')
        
obj = S()
obj.main()
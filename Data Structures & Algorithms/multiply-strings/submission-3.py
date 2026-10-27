class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digToNum = {'1': 1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        numToDig = {digToNum[i]:i for i in digToNum}
        def processnum(num):
            res = 0
            for i in range(len(num)):
                digit = digToNum[num[i]]

                res = res*10 + digit
            return res
        
        def processnumToDigit(num):
            res = ''
            while num > 0:
                res += numToDig[num % 10]
                num //= 10
            return res[::-1] if res != '' else '0'

        return processnumToDigit(processnum(num1) * processnum(num2))
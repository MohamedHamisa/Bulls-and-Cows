class Solution:
    def getHint(self, secret, guess):
        bulls = sum(map(operator.eq, secret, guess))#This function is used to check if a is equal to b or not   
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, both - bulls)

    

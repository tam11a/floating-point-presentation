import math

class Float8():
    
    def __init__(self, bitstring):
        '''Constructor
        takes a 8-bit string of 0's and 1's as input and stores the sub-strings
        accordingly.
        Usage: Float8('00011110')
        '''
        
        # Make sure the input consists of exactly 8-bits.
        assert(len(bitstring)==8)
        
        # Assign the sign bit
        # self.sign = bitstring[?]
        

        # Assign the exponent part
        # self.exponent = bitstring[?]
        

        # Assign the mantissa
        # self.mantissa = bitstring[?]
        
        # YOUR CODE HERE
        #raise NotImplementedError()
        
        self.sign=bitstring[0]
        self.exponent=bitstring[1:4]
        self.mantissa=bitstring[4:8]

        self.val = self.calculate_value()
        
    def __str__(self):
        return f'Sign bit value: {self.sign}\n' + \
            f'Exponent value: {self.exponent}\n' + \
            f'Mantissa value: {self.mantissa}\n'  + \
            f'Floating value: {self.val}\n'
    
    def tobitstring(self):
        return self.sign + self.exponent + self.mantissa
    
    def toformattedstring(self):
        return ' '.join([self.sign, self.exponent, self.mantissa])
    
    def calculate_value(self):
        '''Calculate the value of the number from bits'''
        #print(self.toformattedstring())
        # Initialize with zero
        val = 0.0
        
        # YOUR CODE HERE
        #raise NotImplementedError()
        exp = 0
        for i, j in enumerate(reversed(self.exponent)):
            exp += int(j) * (2**i)
        
        if exp == 7:
            if self.mantissa == '0000':
                val = 'inf'
            else:
                val = 'nan'
        else: 
            frac = exp != 0

            for i, j in enumerate(self.mantissa):
                frac += int(j) * (2**((i + 1) * -1))

            if exp:
                val = (2 ** (exp - 3)) * frac
            else:
                val = (2 ** (-2)) * frac
                

        if int(self.sign):
            if type(val) == str:
                if val != 'nan':
                    val = '-' + str(val)
            else:
                val *= -1
        return val

import numpy as np

data = [ '00000000', '00000001', '00001001', '00010000',
         '00010001', '00011000', '00011011', '00100000',
         '00101101', '00110000', '00110101', '01000011',
         '01000000', '01010000', '01011100', '01100000',
         '01110111', '01110000', '10000000', '10000001',
         '11110001', '11110000', '10110001', '10111101',
         '11100000', '11101011', '11010000']
results = ['(0, 1)', '(1, 64)', '(9, 64)', '(1, 4)', '(17, 64)', '(3, 8)', '(27, 64)',
          '(1, 2)', '(29, 32)', '(1, 1)', '(21, 16)', '(19, 8)', '(2, 1)', '(4, 1)',
          '(7, 1)', '(8, 1)', 'nan', 'inf', '(0, 1)', '(-1, 64)', 'nan', '-inf',
          '(-17, 16)', '(-29, 16)', '(-8, 1)', '(-27, 2)', '(-4, 1)']

test = [Float8(x).val for x in data]


for index in range(len(test)):
    d = test[index]
    try:
        test[index] = str(d.as_integer_ratio())
    except Exception:
        test[index] = str(d)

np.testing.assert_equal(np.array(test), np.array(results))
print('27 out of 27 outputs matched for 8-bit floating points')
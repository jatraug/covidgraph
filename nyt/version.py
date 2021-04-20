#!/usr/bin/env python
# coding: utf-8

# 
# 

# # Version

# ## Use major.submajor.minor as names e.g. 1.2.0

## Make changes here:

class Version:
    def __init__(self):
        self.Major   = 0
        self.Submajor = 0
        self.Minor    = 1
        
    def set(self, major, sub, minor):
        self.Major   = major
        self.Submajor = sub
        self.Minor    = minor
        
    def get(self): 
        return f'{self.Major}.{self.Submajor}.{self.Minor}'



'''

# test:
vers = Version()
print(f'Version is {vers.get()}')
vers.set(3,6,5)
print(f'Version is {vers.get()}')

'''







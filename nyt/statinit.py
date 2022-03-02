'''
Initialize status file. Write a line or two a intro
'''


import writefile as wf




def main():
     writer = wf.fWrite()
     writer.write('Current daily COVID cases and deaths by state\n')


if __name__ == '__main__':
    main()

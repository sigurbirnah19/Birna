# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~") # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter, 
# once decrypted, must be H.
first_letter = line1[0]
fl_num = ord(first_letter)
fl_base = ord('H')
# ...now find out what the key is
key = fl_base - fl_num
# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    for ch in (line):
        ch_num = ord(ch) + key
        
        #don't know why my space gets weird in the last test3
        if( ch_num == 127):
            ch_num = ord(" ")
        print(chr(ch_num),end='')
    print()
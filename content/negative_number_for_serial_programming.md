Title: Binary format of the negative number for serial device programming
Date: 2014-12-28
Category: Programming
Tags: Serial, Python, Pyserial
Author: Jianming

When I happens to program for a step motor controller, I found it uses positive/negative number formatted in 4 bytes to represent the rotating step number with the direction. In the manual it says the the device checks if the highest bit is 1, then the 4 bytes value represent a 31 bits available negative direction step number. However this is really about the signed number representations rather than check the highest bit.

### Signed number representation

In the current programming education, there is less and less mention about the fundemental computer science feature such as the number representation, altough sometimes they talk about it, they don't tell why it is like this. Actually, there is the detailed explaination [here](http://en.wikipedia.org/wiki/Signed_number_representations) about the signed number representation. Almost all recent processors use the *Two's complement*.In short, 127 is 01111111, -128 is 10000000, -1 is 11111111.

Since the serial device only receives the raw bytes, in python we can learn it from:

    :::python
	from struct import *
	pack('>b', -128)

This returns '\x80' which is 0x80 in hex, 10000000 in binary.
Note: here we used '>b' means pack the value -128 into big-endian signed char (1 byte integer).

    :::python
	pack('>b', -1)

This returns '\xff' which is 0xFF in hex, 11111111 in binary.

Usually we send just raw byte strings to a serial device, they are actually bunch of 0 and 1 serial commands. So that if my motor controller takes -2500 as revers rotate 2500 steps. We send a 4-byte string,

    :::python
	pack('>i', -2500)

which is '\xff\xff\xf6\x3c'. Sometimes the pack command returns the string in ASCII because Python's default encoding is 'ascii' encoding. To clearify what exactly the command returns, one can use `pack('>i', -2500).encode('hex')`{.python}. Or I have a more complex solution like, `''.join(r'\x%02X' % ord(ch) for ch in src)`{.python}.

### Compose signed number byte

Except using struct.pack, we can compose the byte by ourselves easily. For example we know there will be 2500 steps backwards on the serial controller. We can simply generate the bytes with `result = 0xFFFFFFFF - 2500 + 1`, then pack this byte into string. It is actually `result = ~2500 + 1`, a bitwise reverse and plus one. To pack this without struct, we can use `chr(int(hex(src),16))` for a single byte.

### Determine if a variable is signed or not

Sometimes we still queries to the serial device about the motor position, then how to judge the returned number is signed or not? 

The answer is no, we cannot know if it is signed or not just with the value. We have to know the protocol used in the device to tell you whether there is MSB (Most Significan Bit) prepared for this. 

However if programming with C not for the serial device. There is a C macro,

    :::C
    #define ISUNSIGNED(a) (a>=0 && ~a>=0)

This one can judge a variable is signed or not to a certain extent. This however still fails for example at a circumstance of promoting unsigned char to int on some of the compiler. There are links about this problem [here](http://stackoverflow.com/questions/7316862/how-to-determine-whether-a-variable-is-unsigned-or-not-in-ansi-c) and [here](http://stackoverflow.com/questions/7469915/value-vs-type-code-to-determine-if-a-variable-is-signed-or-not). 

### Reference

1. [Python Struct documentation](https://docs.python.org/2/library/struct.html)
2. [Wikipedia](http://en.wikipedia.org/wiki/Signed_number_representations)










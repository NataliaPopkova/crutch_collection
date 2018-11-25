import argparse
import random

random.seed()

parser = argparse.ArgumentParser(description = "Generate password.")

parser.add_argument("-l", "--length", action = "store", type = int, dest = "length", help = "password length")

parser.add_argument("--skip-symbols", action = "store_true", help = "Symbols skip")

parser.add_argument("--skip-numbers", action = "store_true", help = "Numbers skip")

args = input().split(' ')
if args[0] == '':
    args = []
args = parser.parse_args(args)

seq = "1234567890~!@#$%^&*()_+`-={}[]:;<>.\/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

if args.skip_numbers and args.skip_symbols:
    seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
elif args.skip_symbols:
    seq = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
elif args.skip_numbers:
    seq = "~!@#$%^&*()_+`-={}[]:;<>.\/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
else:
    seq = "1234567890~!@#$%^&*()_+`-={}[]:;<>.\/ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

password = ""

seq_list = list(seq)

length = 8
if args.length:
    length = int(args.length)
for i in range(length):
    password = password + random.choice(seq_list)

print(password)



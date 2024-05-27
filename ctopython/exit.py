import sys

if len(sys.argv) != 2:
    print("Missing command-line argument!")
    sys.exit(1)

print (f"hello, {argv[1]}")
sys.exit(0)
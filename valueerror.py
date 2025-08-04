try:
    num = int(input('enter a number:'))
    print(num)
except Exception as a:
    print("exception",a)

print("i am outside the try block")
def main(f):
    print("main executed")
    f()

def sub():
    return "madanpur"

sub=main(sub)
print(sub)
import argparse
p=argparse.ArgumentParser(description="testing")
p.add_argument("req")
p.add_argument("--ram", default="ram")
arg=p.parse_args()
print(arg)
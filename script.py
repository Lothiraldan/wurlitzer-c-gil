import pyximport; pyximport.install()
import helloworld
from wurlitzer import pipes

with pipes() as (out, err):
    helloworld.nprint(100000)

print("STDOUT\n", out.read())
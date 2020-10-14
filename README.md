# CSC482-Lab0x04-Fibonacci

A study of algorithms that return the xth value in the Fibonacci sequence.

<pre>
>>> import fib
>>> x = fib.fib_matrix(1337)
>>> x
721111417363193086866718894696647385083800042018334844328309008810572649380189634086859451489620922764584003220409489529566924462325032087715089847891268022881225836523445161660733949028040629172789835698524315074421584970617380285183789842110665401444350164293403647257106462827
</pre>

<pre>
>>> for x in range(1, 21):
...     print(fib.fib_cache(x), end=" ")
...
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
</pre>

`main.py` outputs a [table of run times](https://raw.githubusercontent.com/jessicalynch/CSC482-Lab0x04-Fibonacci/main/output_1602601932669976000.txt) with increasing x values to a .txt file.


* [Small output](https://raw.githubusercontent.com/jessicalynch/CSC482-Lab0x04-Fibonacci/main/output_1602601932669976000.txt) (10-min timeout per algorithm, 1 <= `x` <= 100)
* [Large output](https://raw.githubusercontent.com/jessicalynch/CSC482-Lab0x04-Fibonacci/main/output_1602446678900365000.txt) (10-min timeout per algorithm, 1 <= `x` <= 25000)

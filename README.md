# number_gen
This program generates a number `n` of random integer between `0` and `m` at the user's request. The method used for generation of numbers is a linear congruential generator. 

## The model

Linear congruential generator is a method that generates a sequence of pseudo-random numbers between `0` and `m`. The equation to define the sequence is
<img src="https://render.githubusercontent.com/render/math?math=x_{n %2B 1}=a\cdot x_n %2B b \text{ (mod m) } ">. We call <img src="https://render.githubusercontent.com/render/math?math=x_0"> the seed of the random number generator.

By denoting <img src="https://render.githubusercontent.com/render/math?math=f(x)=ax %2B b"> we get that <img src="https://render.githubusercontent.com/render/math?math=x_2=f^2(x_0)=f(ax_0 %2B b)=a^2x_0 %2B b(a %2B 1)\text{(mod m)}">. In general we obtain <img src="https://render.githubusercontent.com/render/math?math=x_{n %2B 1}=f^{n %2B 1}(x_0)=f^{n}(ax_0 %2B b)=a^{n %2B 1}x_0 %2B b(a^{n %2B 1} - 1)/(a-1)\text{(mod m)}">

In order to maximize the cycle of <img src="https://render.githubusercontent.com/render/math?math=f^n(x_0)">, we have to look at the possible `n` for which <img src="https://render.githubusercontent.com/render/math?math=f^n(x_0)\equiv x_0\text{(mod m)}">. 

If we assume that `m` is a prime number,

<img src="https://render.githubusercontent.com/render/math?math=f^n(x_0)\equiv_{(m)}x_0\Leftrightarrow (a^n-1)\equiv_{(m)}0\text{ or }(a-1)x_0+b\equiv_{(m)}0">

Let us now pick `a` so that `a` and `m` are coprime (for instance, we could have chosen `m` to be a very large prime number and choose `a` to be strictly less than `m`). By Euler's Theorem, the first condition is equivalent to `m-1` dividing `n`. It is also not hard to see that the second condition never happens if we choose `a,b` and `x_0` such that <img src="https://render.githubusercontent.com/render/math?math=(a-1)x_0 %2B b<m">.

A good candidate for `m` is a Mersenne prime (https://en.wikipedia.org/wiki/Mersenne_prime).

## Parameters and seed

Once the choosing of `m` is settled, there seems to be a lot of possible choices for the parameters `a` and `b`. In this case we chose to use `a` to be `772369` and `b` to be `56`, as they satisfy every condition above. For the seed, however, we chose a number that changes depending on the time of day so that the random numbers produced do not depend on whether we are running the program for the first time or not.


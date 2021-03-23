Title: Problem 1
Author: Force
Date: 15/3/21
Overview: Project Euler is a web site with over 700 problems for you to solve. I found it a few days ago and I've been loving to work on it's problems.
Image: ''

Hey everyone.


A few days ago I found out about [Project Euler](https://projecteuler.net/archives) and since then I've been loving to work on it's problems.



For those who don't know **Project Euler**(I will be mensioning it as PE from now on) is a web site with over 700 problems for you to solve.

This problems are math related and meant to be solved with the aid of **Computer Programming Languages** such as *Python*, *C*, *C#*, *Go*, *Rust* and many other (Yep there are a whole lot of programming languages, each having it's own use cases and quirks, so if I didn't mention your favourite language please don't be mad)

In the lower levels, the topics covered in PE are generally related to concepts such as *prime numbers*, *the Fibonacci sequence*,and *powers*.



Since PE allows it's solvers to explain and discuss it's first 100 problems outside of the main site, I will be creating a series of blog posts about my journey on solving this problems, hoping that you will learn as much as I will.


## Let's Start
**Multiples of 3 and 5**

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

>Find the sum of all the multiples of 3 or 5 below 1000.


This is the prompt for the first problem. If this feels simple, don’t let discouragement choke you, because this will be getting more complex soon. If you find this too hard, relax. Math is hard, but easy problems are not fun, the feeling when you solve something difficult is astonishing.

PE startes by explaing a simpler version of the problem and then it asks you the real question. Let's see the simpler version first.


## Simplifying

**If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.**

This are the numbers from 0 to 10:

- 0  1  2  **3**  4  **5** **6**  7  8  **9**  10

If we sum the multiples of 3 and 5:

- 3 + 5 + 6 + 9 = **23**

**The real question is similar to this one, but it asks you to sum all the multiples of 3 and 5 bellow 1000 instead of 10**

## The real Deal
We will start by defining a variable to hold the sum of these numbers.

```python
sum = 0
```

After that we need to create the loop. Since we want to to check all number bellow **1000** and Python's **range** function returns the numbers up to **n-1** (where n is it's parameter), we can do the following:

```python
for i in range(1000):
    # execute something
```

This will loop through the numbers. Now we need a way to find if the value of **i** for every iteration is either divisible by **3 or 5**

Python gives us the **modulus operator (%)**, that returns the rest from the quotient between 2 numbers.

ex: 5%2 = 1

We can deduce from this that if a number is a multiple of another, the result of this operation would be **0** so:

```python
# if i is multiple of 5
if i % 5 == 0:
    sum += i
# if i is multiple of 3 but not 5
elif i % 3 == 0:
    sum += i
```

Using and if/elif block allows us to only add **i** to **sum** once, even if *i is a multiple of both 3 and 5*.

To finish the first challenge we just need to put everything together and print the result.


```python
sum = 0
for i in range(1000):
    if i % 5 == 0:
        sum += i
    elif i % 3 == 0:
        sum += i

print(sum)
```

If you want to check this for any numbers this is the generic algorith:

```python
sum = 0
for i in range(n):
    if i % a == 0:
        sum += i
    elif i % b == 0:
        sum += i

print(sum)
```

We have reached the end of our first journey into the realm of math/programming problems. I hope you have enjoyed and learned something. I will try to post write ups on this kind of problems as often as I can.

Until then be safe and **Ask Questions**.

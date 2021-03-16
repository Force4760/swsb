Title: Even Fibonacci Numbers
Author: Force
Date: 15/3/21
Overview: The second challenge from the Project Euler makes us dive into the wonders of the Fibonacci number and the golden ratio.
Image: ''

Hi again everyone!

This is my second post, and I will be continuing to work on the euler project.

Today I will be solving the 2nd problem called [Even Fibonacci Numbers](https://projecteuler.net/problem=2).

## Fibonacci

As the title suggests, we will be working with the *Fibonacci sequence*, which is just **Beautifull**. This sequence consists of numbers that follow a simple rule: **Each one is the sum of the two that come before it**.

It can be seen in nature in various ways, generating amazing and mesmerizing patterns like this ones: ![fibonnaci](https://leerzelfbeleggen.com/wp-content/uploads/2018/08/Fibonacci-trading-leren-traden-met-de-geheime-formule-voorbeelden.jpeg)

This Sequence was first described by *Leonardo Fibonacci*, a famous mathematician from the 12th century. He used this to describe the growth of a group of rabbits for a problem that intended to teach people how to use **Arabic numbers** (the ones we use today like 1, 2, 3 ...) since they had been introduced to Europeans dhortly before.

## The Problem

The question starts by introducing us to the concept of the Fibonacci sequence, but the real question is:

>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Let's start dissectingg it, shall we?

To make things easier, we can start by creating a list that holds three values:
- The **oldest** number at **index 0**
- The **previous** number at **index 1**
- The **new** number at **index 2**

```python
# old - previous - new
num = [1, 2, 3]
```

Since we already placed 2 and 2 is an **even** number, our **sum** variable should be initialized with the value *2*:

```python
sum = 2
```
We are then asked to consider numbers bellow **four million**, so we can use a *while loop* that breaks when we reach that number, and since the current number is stored at **num[2]**:

```python
while num[2] < 4000000:
    # do logic
```

As far as the internal logic goes, we need to add two things:
- A way to continue the sequence
- A way to check if the number is **even** and add it to the **sum** variable.

The sequence can be continued by adding the two **previous** numbers, replacing the **new** with their sum and shifting their positioning like this:

```python
# add oldest and previous
num[2] = num[0] + num[1]
# shift positioning
num[0] = num[1]
num[1] = num[2]
```

Now that the first problem is covered, we need to work on the second one. Python (and most modern/high level programming languages) facilitates this by giving us access to the **%** operator. This operator allows us to get the rest from a quotient between two numbers. Let's do a quick recap on elementary math.


A division can be seen as a sequence of subtractions, so **4/2** can be seen as:
- 4 - 2 = 2
- (4 - 2) - 2 = 2 - 2 = 0
- so 4/2 = 2

If we try to do **5/2** we can:
- 5 - 2 = 3
- (5 - 2) - 2 = 3 - 2 = 1
- so 5/2 = 2*2 + 1 (the rest)

If a number is a multiple of another it's rest will be equal to **0**. So by checking that we get if a number is even (multiple of 2) or odd. And add it to the sum

```python
if num[2] % 2 == 0:
    sum += num[2]
```

Alternatively we can do this:

```python
if int(num[2]/2) == num[2]/2:
    sum += num[2]
```

Now that we have every part created we just need to join them and print the result.

```python
num = [1, 2, 3]
sum = 2
while num[2] < 4000000:
    num[2] = num[0] + num[1]
    num[0] = num[1]
    num[1] = num[2]
    if num[2] % 2 == 0:
        sum += num[2]

print(sum)
```

This 2nd problem was a lot of fun (even if it was simple), because I **love** sequences (especially this one)

I hope that you also had fun and learned something new. I will be releasing a new post soon, but until then **Ask Questions**.



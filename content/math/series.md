---
title: Mathematical series
todo: Fourier series, Taylor series
---
## Finite series
### 1. Powers
$$
\sum_{x=1}^{n}x=\frac{n(n+1)}{2}
y=mx+c
$$
$$
\sum_{x=1}^{n}x^2=\frac{n(n+1)(2n+1)}{6}
$$
$$
\sum_{x=1}^{n}x^3=\frac{n^2(n+1)^2}{2^2}
$$
### 2. Binomial coefficients
$$
\sum_{k=0}^{n}{}^nC_k=2^n
$$
$$
\sum_{k=0}^{n}{^{}{}^nC_k}^2={}^{2n}C_n
$$

## Infinite series

>[!warning]
>Infinite sums for ***smooth* exponential, trigonometric, and binomial functions** are valid only for $|x|<1$.


### 1. Exponential and Logarithmic
$$
e^x=1+x+\frac{x^2}{2!}+...=\sum_{k=1}^{\infty}\frac{x^k}{k!}
$$
$$
ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-...
$$
$$
\sum_{k=0}^{\infty}\frac{1}{(2k+1)(2k+2)}=\frac{1}{2\times3}+\frac{1}{4\times5}+...=ln2
$$
$$
\sum_{k=0}^{\infty}\frac{1}{2^{k}k}=ln2
$$
### 2. Trigonometric
$$
sin(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}+...
$$
$$
sinh(x)=x+\frac{x^3}{3!}+\frac{x^5}{5!}+...
$$
### 3. Binomial
$$
(1+x)^{\alpha}=\sum_{k=0}^{\infty}{}^{\alpha}C_k{\cdot}{x^k}
$$
$$
(1-x)^{-\alpha}=\sum_{k=0}^{\infty}{}^{\alpha+k-1}C_k{\cdot}{x^k}
$$
### 4. Riemann zeta function

$$
\sum_{k=1}^{\infty}\frac{1}{k^2}=\zeta(2)=\frac{\pi^2}{6}
$$
$$
\sum_{k=1}^{\infty}\frac{1}{k^4}=\zeta(4)=\frac{\pi^4}{45}
$$
$$
\sum_{k=1}^{\infty}\frac{1}{k^6}=\zeta(2)=\frac{\pi^6}{945}
$$
### 5. Alternating harmonic
From series $ln(1+x)$:
$$ 
1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+...=ln(2)
$$
$$
1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+...=\frac{\pi}{4}
$$
### 6. Reciprocal of factorials
Can be derived from [[series#1. Exponential and Logarithmic|Exponential series]]:
$$
1+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+...=e
$$
$$
\frac{1}{0!}+\frac{1}{2!}+\frac{1}{4!}+\frac{1}{6!}+...=\frac{1}{2}(e+\frac{1}{e})=cosh(1)
$$

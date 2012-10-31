title: The convergence of mean fitness towards the mutation-selection balance
datetime: 2012-10-26 11:33:00 +2
tags: []
draft: true
math: true

[TOC]

## Overview

In an [eariler post]
I described how the mean fitness of a population at the *mutation-selection balance* can be found.
I assumed that the population is *asexual*, that only *deleterious mutations* occur,
that there is no *drift* or *recombination*, and that the selection was *constant*.

In this post I would like to continue with these assumpions, but instead of simply finding the mean fitness at the mutation-selection balance,
that is at the equilibrium, I will show how one finds a simple formula for the mean fitness after an arbitrary number of generations.
The formulation ad derivation will follow one of my favorite papers - 
["Nonequilibrium model for estimating parameters of deleterious mutations"][gordo2005] by @Gordo2005.

## Motivation

But first, why should we want the mean fitness before the mutation-selection balance? 

The general answer is that probably some, if not most, populations are *not at the mutation-selection balance*.
The mutation-selection balance is a nice idea, but it serves as a reference, as a null hypothesis, 
not as a general rule. The assumptions at the base of the balance are too thin, 
especially that *selection is static* - selection is probably not static but fluctuating, both in amplitude and direction.
This means that at least some of the natural populations we may encounter in the wild are not evolving **at** the mutation-selection balance,
but rather evolving **towards** the mutation-selection balance, never actually reaching one.

The more specific answer is that even in laboratory conditions which induce a constant sselection regime
it may take *a long time* for populations to reach the mutation-selection balance, 
and this time might be longer than what we intuitively expect (or desire).
This aspect is discussed by @Gordo2005. They wanted to use traditional models for calculating the mutatio rate of bacterial populations at the lab,
but noticed that these models assume that the populations reach a mutation-selection balance in the calculations they use.
However, they found that in the timeframe they envisioned for their study their populations will not reach an equilibrium, especially if selection is weak 
(see Figure 1 in [@Gordo2005]).

This is interesting, because we saw in the [eariler post] that the mean fitness
at the mutation-selection balance is *e^-U^*, where *U* is the mutation rate and is independent of *s*, the selection coefficient.
But Figure 1 in [@Gordo2005] is a clear example that the mean fitness towards the mutation-selection balance is highly dependent on *s*,
and that *s* sets the pace towards the balance.

## Model

This follows the model from [@Gordo2005] but I elaborated and included all the rigouros steps.

### Definitions

Denote the pmf (probability mass function) of a Poisson distribution with parameter $\lambda$: $\varphi_{\lambda} (x)$
Consider an asexual infinite population evolving in a constant environment. 
The number of new mutations per individual per generation is Poisson distributed with parameter *U*, the mutation rate.
All mutations are deleterious with a multiplicative effect *s*, so
that an individual with $i$ mutant allele has a fitness $\omega_{i}:=(1-s)^{i}$ with selection coefficient $0<s<1$.
The frequency of individuals with *i* mutant at generation *g* is denoted $f_{i}(g)$ and $\sum_{i}{f_{i}(g)}=1$.
From the former two statements it follows that the population mean fitness at generation *g* is
$\bar{\omega }_{g}=\sum_{i}{f_{i}(g)\omega _{i}}$.
Assume that the selection occurs before mutation.

### The distribution of mutant alleles

The change in the frequency of individuals with *i* mutant alleles from generation *g* to generation *g+1* is written as:

$$
f_{i}(g+1)=\sum_{k=0}^{i}{\frac{ \omega _{k} }{ \bar{\omega}_{g} } f_{k}(g) \varphi_{U} (i-k) }
$$

The model starts with a mutation-free population, so the initial condition is $f_{0}(0)=1, f_{i>0}(0)=0$.

Let's calculate
the frequency of individuals with *i* mutant alleles after one generation:

$$
f_{i}(1)=\sum_{k=0}^{i}{f_{k}(0)\frac{\omega _{k}}{\bar{\omega}_{1}}\cdot \frac{U^{i-k}}{(i-k)!}e^{-U}}
$$
and because 
$$
f_{k}(0)=\bigg\{
\begin{gathered}
1, k=0 \\
0, otherwise \\
\end{gathered}
$$
we get 
$$
f_{i}(1) = f_{0}(0)\frac{\omega _{0}}{\bar{\omega }_{1}} \cdot \frac{U^{i}}{i!}e^{-U} = \frac{U^{i}}{i!}e^{-U}
$$
so the frequency of individuals with *i* mutant alleles after one generation is Poisson distributed with parameter *U*.

To verify this - the expected number of mutations after one generation is 
$$
\sum_{i\ge 0}{i\cdot f_{i}(1)} = \sum_{i\ge 1}{i\cdot \frac{U^{i}}{i!}e^{-U}} =\\ 
e^{-U}U\sum_{i\ge 1}{\frac{U^{i-1}}{(i-1)!}} = \\ 
e^{-U}U\sum_{i\ge 0}{\frac{U^{i}}{i!}} = \\ 
Ue^{-U}e^{U} = U
$$
as expected.

To go on the next step, we will find the frequency of individuals with *i* mutant alleles at the second generation,
after selection but *before* mutations - this is marked by $f_{i}^{s}(2)$:
$$
f_{i}^{s}(2) = \frac{\omega _{i}}{\bar{\omega}_{1}}f_{i}(1) = \\
\frac{(1-s)^{i}}{\sum_{k=0}^{\infty }{f_{k}(1)\omega_{k}}}\frac{U^{i}}{i!}e^{-U} = \\
\frac{(1-s)^{i}}{\sum_{k=0}^{\infty}{\frac{U^{k}}{k!}e^{-U}(1-s)^{k}}}\frac{U^{i}}{i!}e^{-U} = \\
\frac{(U(1-s))^{i}}{i!\sum_{k=0}^{\infty}{\frac{(U(1-s))^{k}}{k!}}} = \\
\frac{(U(1-s))^{i}}{i!}e^{-U(1-s)}
$$

So, $f_{i}^{s}(2)$ is Poisson distributed with parameter $U(1-s)$, and the frequency *after* mutation will be: 
$$
f_{i}(2) = \sum_{k=0}^{i}{f_{k}^{s}(2)\frac{U^{i-k}}{(i-k)!}e^{-U}} = \\
\sum_{k=0}^{i}{\frac{(U(1-s))^{k}}{k!}e^{-U(1-s)}\frac{U^{i-k}}{(i-k)!}e^{-U}} = \\
e^{-U(1-s)-U}\sum_{k=0}^{i}{\frac{U^{i-k}(U(1-s))^{k}}{k! \cdot (i-k)!}} = \\
\frac{U^{i}}{e^{U(1-s) + U}} \sum_{k=0}^{i}{\frac{(U(1-s))^{k}}{U^{k} \cdot k! \cdot (i-k)!}} = \\
\frac{U^{i}}{e^{U(1-s) + U}} \sum_{k=0}^{i}{\frac{(1-s)^{k}}{k! \cdot (i-k)!}}
$$

Note that 
$\sum_{k=0}^{i}{\frac{q^{k}}{k!\cdot (i-k)! }} = \frac{(q+1)^{i}}{i!}$ And $\sum_{k=1}^{i}{\frac{q^{k}}{k!\cdot (i-k)! }}=\frac{(q+1)^{i}-1}{i!}$, and therefore:

$$
f_{i}(2) = \frac{U^{i}}{e^{U(1-s)+U}}\cdot \frac{(2-s)^{i}}{i!} = \\
\frac{(U(1-s)+U)^{i}}{i!}e^{-(U(1-s)+U)} = \\
\phi(i | U(1-s)+U)
$$

Similar to the former expansion and because the Poisson process is *memoryless*, 
the frequency of individuals with *i* mutant alleles after mutation at generation 2 will be Poisson distributed with parameter $U(1-s)+U$.

The same argument makes it clear that the distribution of mutant alleles 
at any generation *g* is Poisson distributed, but let's see a rigrouros formulation of this.

## The expected number of mutant alleles

After seeing how the distribution of mutant alleles changes at the first couple of generations,
and verifying that this is a Poisson distribution,
we can now formulate the recurrence relation for the expected number of
mutatnt allele - or the parameter of the Poisson distribution, $\lambda$:

$$
\lambda (g+1) = \sum_{k=0}^{\infty }{k\cdot f_{k}(g+1)} = \\
\sum_{k=0}^{\infty}{\sum_{i=0}^{k}{k\frac{(1-s)^{i}}{\bar{\omega}_{g}}f_{i}(g)\frac{U^{k-i}}{(k-i)!}e^{-U}}} = \\
\sum_{i=0}^{\infty}{\sum_{k=i}^{\infty }{k\frac{(1-s)^{i}}{\bar{\omega}_{g}}f_{i}(g)\frac{U^{k-i}}{(k-i)!}e^{-U}}} = \\
\sum_{i=0}^{\infty}{e^{-U}\frac{(1-s)^{i}}{\bar{\omega}_{g}}U^{-i}f_{i}(g)\sum_{k=i}^{\infty}{k\frac{U^{k}}{(k-i)!}}} = \\
\sum_{i=0}^{\infty}{e^{-U}\frac{(1-s)^{i}}{\bar{\omega}_{g}}U^{-i}f_{i}(g)e^{U}U^{i}(i+U)} = \\
\frac{1}{\bar{\omega}_{g}}\sum_{i=0}^{\infty }{f_{i}(g)(1-s)^{i}(i+U)} = \\
\frac{U}{\bar{\omega}_{g}}\sum_{i=0}^{\infty }{f_{i}(g)(1-s)^{i}}+\frac{1}{\bar{\omega}_{g}}\sum_{i=1}^{\infty }{i\cdot f_{i}(g)(1-s)^{i}} = \\
U + \frac{\sum_{i=1}^{\infty }{i\cdot f_{i}(g)(1-s)^{i}}}{\sum_{i=0}^{\infty}{f_{i}(g)(1-s)^{i}}} = \\
U + \frac{\sum_{i=1}^{\infty }{i\cdot \frac{e^{\lambda (g)}(\lambda (g)(1-s))^{i}}{i!}}}{\sum_{i=0}^{\infty}{\frac{e^{\lambda(g)}(\lambda (g)(1-s))^{i}}{i!}}} = \\
U + \frac{\lambda(g)(1-s)\cdot e^{\lambda (g)(1-s)}}{e^{\lambda(g)(1-s)}} = \\
\lambda (g)(1-s) + U
$$

So we got a nice recurrence formula - $\lambda (g+1)=\lambda (g)(1-s)+U$ with an initial condition $\lambda (1)=U$.
The recurrence means that the expected number of mutatnt alleles per individual in the population
is reduced every generation by selection by multiplying it by *(1-s)* and increased by mutation by adding *U*.

The solution to this recurrence relation is (why? this will require another post):
$$
\lambda(g)=\frac{U}{s}(1-(1-s)^{g})\xrightarrow{g\to \infty }\frac{U}{s}
$$

For a sinlge-locus deterministic model, the expected frequency of the wild-type allele at the mutation-selection balance 
(assuming that $s>>U$) is $1 - \frac{U}{s}$, which agrees well with the frequency of mutation-free individuals we can now calculate:
$\phi(0 | \frac{U}{s}) = \frac{\frac{U}{s}^0}{0!} e^{-\frac{U}{s}} = e^{-\frac{U}{s}} = 1-\frac{U}{s} + O(\frac{U}{s}^{2})$. The last approximation uses the Taylor expansion of the exponential function around 0.

## The population mean fitness 

After *g* generations the population mean fitness is:

$$
\bar{\omega}_{g} = \sum_{i=0}^{\infty }{\frac{\lambda(g)^{i}}{i!}e^{-\lambda(g)}(1-s)^{i}} = \\ 
e^{-\lambda(g)}\sum_{i=0}^{\infty}{\frac{ (\lambda(g) (1-s))^{i}}{i!}} = \\
e^{-\lambda(g)}e^{\lambda(g)(1-s)} \Rightarrow \\
\bar{\omega}_{g} = e^{-\lambda(g) s}
$$

Which gives us yet [another way][earlier post] to calculate the mean fitness at the mutation-selection balance: 
$$
\bar{\omega }^* = lim_{g\to \infty} e^{-\lambda(g) s} = e^{-\frac{U}{s}s} = e^{-U}
$$

The second moment of the population fitness is given by:

$$
E[\omega_{g}^2] = \sum_{i=0}^{\infty }{\frac{\lambda(g)^{i}}{i!}e^{-\lambda(g)}(1-s)^{2i}} = \\
e^{-\lambda(g)} \sum_{i=0}^{\infty }{\frac{ (\lambda(g)(1-s)^2)^{i} }{i!}} = \\
e^{-\lambda(g)} e^{\lambda(g)(1-s)^2} = \\
e^{\lambda(g)(1-2s+s^2)-\lambda(g)} = \\
e^{\lambda(g)(s^2-2s)}
$$


## Estimation of mutation rates 

In mutation-accumulation experiments, a population is undergoing a sequence of bottlenecks that cause the accumulation of mutations due to the ineffectivness of selection when the effective population size is small. These experiments usually use measurements of mean and variance population fitness to estimate *s* and *U*. 

This is the idea: denote the mean fitness at bottleneck *B* by $\bar{\omega{B}}$. 
Than we start with a mutation-free population, and $\bar{\omega_{0}} = 1$. At the first bottleneck, 
the population is assumed to reach a mutation-selection balance,
so the mean fitness is now $\bar{\omega_{1}} = e^{-U}$. At the next bottleneck, the mean fitness again was reduced by the same factor,
so it is now $\bar{\omega_{1}} = e^{-U}e^{-U} = e^{-2U}$. So after *B* bottlenecks, the mean fitness is $\bar{\omega_{B}} = e^{-UB}$.
So one can take the log of the mean fitness after *B* bottlenecks, $-BU$, and use a linear regression model to estimate *U*.

However, what happens if the populatio doesn't reach a mutation-selection balance?
In a population of bacteria, for example, the number of generations between bottlenecks may be insufficient for the population to reach a mutation-selection balance. In this case one muse use a non-equilibrium value of the mean fitness, which is $\bar{\omega}_{g} = e^{-\frac{U}{s} (1-(1-s)^{g})}$. This is the subject of @Gordo2005, titled: **Nonequilibrium model for estimating parameters of deleterious mutations**. The paper explores a statistical model based on the above calculations. The statistical model is tested against results of simulations. In another paper, [@Trindade2010][trindade2010], they tested this statistical model on results of a mutation accumulation experiment with *E. coli*.

In the above development, we saw that in the mean fitness after *g* generations is $\bar{\omega}_{g} = e^{-\lambda(g) s}$. 
If the number of generations between bottlenecks is constant, say *g=24* for a population in which a generation is estimated at 30 minutes, resulting in a bottleneck period of 12 hours, than we can denote $\lambda {:=} \lambda(g)$ and then 
use $\bar{\omega_{B}} = e^{-\lambda s B}$. Then we can use a linear regression model to estimate $-\lambda s$.

But how do we proceed? The estimator we found using linear regression, $\lambda s= \lambda(g) s = U(1-(1-s)^{g})$, doesn't directly yield us either *U* or *s*.
Well, this is why we calculated the second moment. We will not use it directly, but instead define an F-statistic 
not to be confused with the F-statistic used to desctibe heterozigosity or population structuring):
$F_{B} = \frac{\bar{\omega^2}}{\bar{\omega}^2}$. This is a little confusing so I'll right it in a probablistic way:

$$
F_{B} = \frac{E[\omega^2]}{E^2[\omega]}
$$

This is just the ratio of the second moment to the square of the first moment. What is this ratio? Let's have a look:

$$
F_{B} = \frac{E[\omega^2]}{E^2[\omega]} = \\
\frac{e^{\lambda (s^2-2s) B}}{e^{-2 \lambda s B}} =\\
e^{B( \lambda s^2-2\lambda s+2 \lambda s)} = \\
e^{B( \lambda s^2)}
$$

So the log of the *F* statistic is $B \lambda s^2$, and so linear regression can give us $\lamda s^2$. 
Now have have both $-\lambda s$, $\lambda s^2$, and of course $\lambda = \frac{U}{s}(1-(1-s)^g)$,
and we can readily estimate both *U* and *s*.

## Technical remarks

I originally wrote this post with [Office 2010](http://en.wikipedia.org/wiki/Microsoft_Office_2010). I converted it TeX using [docx2tex](http://docx2tex.codeplex.com/) and from [TeX](http://en.wikipedia.org/wiki/LaTeX) to [Markdown](http://daringfireball.net/projects/markdown/) using [LaTeX2Markdown](https://github.com/ajtulloch/LaTeX2Markdown), although it can also be sone using [Pandoc](http://johnmacfarlane.net/pandoc/). Then I proof-read it, and several LaTeX bugs were identified and fixed using an online tool for [testing MathJax code](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm) \([MathJax](http://www.mathjax.org/) is a JavaScript library that displays LaTeX in browsers, see how in [another post](/blogging-with-math-and-code)\).

##  References

[gordo2005]: http://link.aps.org/doi/10.1103/PhysRevE.71.031907
[trindade2010]: http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=2871818
[eariler post]: http://blog.yoavram.com/mean-fitness-at-the-mutation-selection-balance/
title: "Muller's Ratchet"
datetime: 2013-2-21 12:38:00 +2
tags: [recombination, asexual populations, mutation-selection balance, muller's ratcher, mutation accumulation, genetic drift]
category: [research, mutation rate]
math: true
cite: true
draft: true

[TOC]

## The distribution of deleterious mutations in a finite population

The following derivation follows that of John Haigh in his paper **"The Accumulation of Deleterious Genes in a Population - Muller's Ratchet"** [@Haigh1978].

$$
p_{k}(t) = \sum_{j=0}^{k} (X_{k-j}(t)(1-s)^{k-j} e^{-\lambda} \frac{\lambda^j}{j!})/T_{1}(t)
$$
where $X_i$ is a multinomial R.V. representing the **number of individuals with *i* deleterious mutations**, $p_k(t)$ is the multinomial probability for $X_k(t+1)$, *s* is the **selection coefficient**, $\lambda$ is the **mutation rate** (usually denoted on this blog by $\mu$ or *U*) and $T_{r}(t)$ is the sum of *r*-th power of the population fitness at time *t*:
$$
T_{r}(t) = \sum_{i\ge 0} X_{i}(t) (1-s)^{ir}
$$
Now we are looking for the **stable distribution** $n=(n_0, n_1, ...)$ for which $E[X(t+1) | X(t) = n] = n$.
This is:
$$
n_k = N \sum_{j=o}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j e^{-\lambda}}{j!}/T
$$
where $N=\sum n_i$ is the **stable population size** and $T/N = \sum \frac{n_i}{N} (1-s)^i$ is the **stable population mean fitness**.

Looking at $n_0$ and assuming it is positive, the sum has only one term:
$$
n_0 = N n_{0}(1-s)^{0} \frac{\lambda^0 e^{-\lambda}}{0!}/T \Rightarrow
T = N e^{-\lambda}
$$
which is another $\bar{\omega} = e^{-U}$ result, as we have [seen before](/mean-fitness-at-the-mutation-selection-balance/).
Using this identify, we get
$$
n_k = N \sum_{j=o}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j e^{-\lambda}}{j!}/N e^{-\lambda} \Rightarrow
n_k = \sum_{j=o}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j }{j!}
$$
To find the solution we first look at $k=1$:
$$
n_1 = n_{1}(1-s) + n_{0} \lambda \Rightarrow
n_1 - n_{1}(1-s) = n_{0} \lambda \Rightarrow
n_1 - n_{1} + s n_{1} = n_{0} \lambda \Rightarrow
s n_{1} = n_{0} \lambda \Rightarrow
n_{1} = n_{0} \frac{\lambda}{s}
$$
Next, assume that $n_m = n_0 \frac{\lambda^m}{s^m m!}$ for all $m<k$ and check for $k$:
$$
n_k = \sum_{j=0}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j }{j!} \Rightarrow
n_k = \sum_{j=0}^{k} n_{0} \frac{\lambda^{k-j}}{s^{k-j} (k-j)!} (1-s)^{k-j} \frac{\lambda^j }{j!} \Rightarrow
n_k = \lambda^k n_{0} s^{-k} (1-s)^k \sum_{j=0}^{k} n_{0} \frac{s^{-j}}{(1-s)^{j} (k-j)! j!} \Rightarrow
n_k = \lambda^k n_{0} s^{-k} (1-s)^k (1-s)^{-k} \frac{1}{k!} \Rightarrow
n_k = n_{0}(\frac{\lambda}{s})^k \frac{1}{k!}
$$
or as Haigh writes it
$$
n_k = n_{0}\frac{\theta^k}{k!}, \; \theta=\lambda/s
$$
From this we can find the $f_0 = n_0/N$, the **frequency of the fittest class of individuals**, because we know that $\sum_{k \ge 0} n_k = N$:
$$
N = \sum_{k \ge 0} n_k = 
\sum_{k \ge 0} n_{0}\frac{\theta^k}{k!} = 
n_{0} \sum_{k \ge 0} \frac{\theta^k}{k!} = 
n_{0} e^\theta \Rightarrow 
n_{0} = N e^{-\theta} \Rightarrow
f_{0} = e^{-\theta}
$$
For example, for a mutation rate $\lambda=0.003$ and selection coefficient $s=0.01$ then the frequency of unloaded individuals is roughly 74%. 
However,  we have already seen this in a [previous post](/convergence-of-mean-fitness/) where we have found that the distribution of individuals with *i* deleterious mutations is Poisson with parameter $\lambda/s$. 
What I aim to show here is something else - we want to examine a finite population.

## Finite populations

## References
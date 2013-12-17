title: "The distribution of deleterious mutations at the mutation-selection balance"
datetime: 2013-12-17 15:55:00 +2
tags: [asexual populations, mutation-selection balance, mutation accumulation]
category: [research, mutation rate]
math: true
cite: false

If we sample a random individual from an asexual population that had allot of time to adapt to its environment, how many deleterious mutations can we expect it to have? This distribution of deleterious mutations is the starting point of many population genetics models. In an [eariler post] we've calculated this distribution - not only at the mutation-selection balance, but also on the way towards the balance from a mutation-free population. 

Here, we calculate the distribution of deleterious mutation at the mutation-selection balance by following the derivation of John Haigh in his ultra-classic paper **"The Accumulation of Deleterious Genes in a Population - Muller's Ratchet"** [@Haigh1978].

We focus on a finite asexual population undergoing selection and mutation. All mutations are deleterious with an independent (multiplicative) identical effect on fitness. The number of mutations per individual per generation is Poisson distributed[^poisson]. and The master equation is: 

$$
p_{k}(t) = \sum_{j=0}^{k} (X_{k-j}(t)(1-s)^{k-j} e^{-\lambda} \frac{\lambda^j}{j!})/T_{1}(t)
$$

$X_i(t)$ is a multinomial random variable representing the **number of individuals with *i* deleterious mutations at time *t***, $p_k(t)$ is the multinomial probability for $X_k(t+1)$ (or the expected value of $X_k(t+1)/\sum_{j\ge 0}{X_j(t+1)}$), *s* is the **selection coefficient**[^s], $\lambda$ is the **mutation rate** (usually denoted on this blog by $\mu$ or *U*) in mutations per individual per generation, and $T_{r}(t)$ is the sum of *r*-th power of the population fitness at time *t*:

$$
T_{r}(t) = \sum_{i\ge 0} X_{i}(t) (1-s)^{ir}
$$

So $\bar{\omega} = T_{1}(t) / \sum_{j\ge 0}{X_j(t)}$ is the population mean fitness.

Now we are looking for the **stable distribution** of mutations in the population $n=(n_0, n_1, ...)$ for which $E[X(t+1) | X(t) = n] = n$.
This is:

$$
n_k = N \sum_{j=0}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j e^{-\lambda}}{j!}/T
$$

where $N=\sum_{i \ge 0} n_i$ is the **stable population size** and $T/N = \sum_{i \ge 0} \frac{n_i}{N} (1-s)^i$ is the **stable population mean fitness**, (usually denoted by $\bar{\omega}$.

Looking at $n_0$ and assuming it is positive (because this the the stable number of individuals without deleterious mutations), the sum has only one term:

$$
n_0 = N n_{0}(1-s)^{0} \frac{\lambda^0 e^{-\lambda}}{0!}/T \Rightarrow \\
T = N e^{-\lambda}
$$

which is another $\bar{\omega} = e^{-U}$ result, as we have [seen before](/mean-fitness-at-the-mutation-selection-balance/).

Using this identify, we get

$$
n_k = N \sum_{j=0}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j e^{-\lambda}}{j!}/N e^{-\lambda} \Rightarrow \\
n_k = \sum_{j=0}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j }{j!}
$$

We find the solution using induction, assume that $n_m = n_0 \frac{\lambda^m}{s^m m!}$ for all $m<k$ and check for $k$ (the induction base is trivial, $n_0=n_0$):
$$
n_k = \sum_{j=0}^{k} n_{k-j}(1-s)^{k-j} \frac{\lambda^j }{j!} =
\sum_{j=0}^{k} n_{0} \frac{\lambda^{k-j}}{s^{k-j} (k-j)!} (1-s)^{k-j} \frac{\lambda^j }{j!} \Rightarrow
 n_{0} \lambda^{k} \sum_{j=0}^{k} \frac{(1-s)^{k-j} }{s^{k-j} (k-j)!j!}  =
 n_{0} \frac{\lambda^{k}}{s^k k!} \sum_{j=0}^{k} \frac{k!}{(k-j)!j!} s^{j} (1-s)^{k-j}  =
 n_{0} \frac{\lambda^{k}}{s^k k!}  \sum_{j=0}^{k} {k \choose j} s^{j} (1-s)^{k-j}  =
 n_{0} \frac{\lambda^{k}}{s^k k!} \sum_{j=0}^{k} P(Bin(k,s)=j)  \Rightarrow \\
n_k = n_{0} \frac{\lambda^{k}}{s^k k!}
$$ 
Where $P(Bin(k,s)=j)$ is the probability that a Binomial random variable with *k* trials and success probability *s* succeeds *j* times and fails *k-j* times. 

Haigh wrote this as:
$$
n_k = n_{0}\frac{\theta^k}{k!}, \; \theta=\lambda/s
$$
From this we can find the **frequency of the fittest class of individuals**, $f_0 = n_0/N$, because we know that the population size is $\sum_{k \ge 0} n_k = N$:

$$
N = \sum_{k \ge 0} n_k = 
\sum_{k \ge 0} n_{0}\frac{\theta^k}{k!} = 
n_{0} \sum_{k \ge 0} \frac{\theta^k}{k!} = 
n_{0} e^\theta \Rightarrow 
n_{0} = N e^{-\theta} \Rightarrow \\
f_{0} = e^{-\theta}
$$

For example, Trindade et al. [-@Trindade2010] studied a mutator strain of *E. coli* and found that is has a mutation rate of $\lambda=0.005$ and selection coefficient $s=0.03$. For these values, the frequency of the fittest individuals is roughly 85%. 

## References

[^s]: The effect of deleterious mutations on fitness

[^poisson]: This is reasonable because the mutation rate per locus is very low, but there are many loci

[eariler post]: /mean-fitness-at-the-mutation-selection-balance/

title: Mean fitness at the mutation-selection balance
datetime: 2012-10-14 16:45:00 +2
updated: 2014-04-03 11:28:00 +2
tags: [mutation-selection balance, mean fitness, asexual populations, mathematical modeling]
category: [research, mean fitness]
math: true
cite: true

[TOC]

## Overview

The first post on the [Mutation-Selection Blog](http://blog.yoavram.com) must be about the *mutation-selection balance*, right? 

So what is the mutation-selection balance?

In evolutionary biology, selection acts to remove deleterious mutations from the population, while mutation generates new deleterious mutations. 
When they cancel each other out, the population is at the **mutation-selection balance**.

We'll start by defining **fitness**.
In the following treatment, the fitness of an individual is his reproductive success compared to the reproductive sucess of the 
most succesful individual in the population. 

More formally, denote the fitness of individual *i* at generation *n* by $\omega_{i,n}$, 
and define the (population) mean fitness at generation *n* by $\bar{\omega}_n = E_i[\omega_{i,n}]$. 

At the mutation-selection balance the mean fitness is at an equilibrium, that is, it doesn't change from one generation to the next:
$$
\bar{\omega}_{n+1} = \bar{\omega}_n
$$
The value of this equilibrium is denoted by $\bar{\omega}^*$.

A classical result by [@Kimura1966] involves a system in which an infinite population is evolving under *selection* and *mutation*.
Mutation is unidirectional and deleterious and occurs with a rate *U*, selection is constant and uniform, the enivronment is constant, and there is no drift, sex, recombination or migration.
This is a simplistic model but one that is able to capture the dynamics of some complex systems.
The elegant result is that the mean fitness of a population is not dependent on selection strength and is 
an exponentialy decreasing function of the mutation rate *U*:
$$
\bar{\omega}^* = e^{-U}
$$

## Single locus

In this section I roughly follow the route of [@Gillespie2004].
To reach this formula in a simple way (all you need is some straightforward *Calculus* and a little bit of *Genetics*), 
we start by looking at a single locus[^locus] with 
two alleles[^allele], denoted by *A* and *a*, which have fitness of *1* and *1-s*, respectively, 
with *s* playing the part of the *selection coefficient* which defines the deleterious multiplicative effect a deleterious mutation has on the 
fitness of an individual.

Define *p* and *q* to be the frequencies of *A* and *a* so that *p+q=1*.
Denote the probability that the wild-type allele *A* mutates to allele *a* by $\mu$ 
(without back-mutations, that is, *a* doesn't mutate back to *A*),
and denote the frequency of *A* after one generation by *p'*[^pprime]:
$$
p' = \frac{p(1-\mu)}{\bar{\omega}}
$$
with the population mean fitness $\bar{\omega} = p + q(1-s)$.

To find the equilibirum value of *p*, one must subtitute $p'=p$ and $q=1-p$:
$$
p = \frac{p(1-\mu)}{p + (1-p)(1-s)} \Rightarrow \\
p(p+(1-p)(1-s)) = p(1-\mu) \Rightarrow
$$
we assume $p\ne 0$ because we are not interested in a population of mutants:
$$
p+(1-p)(1-s) = 1-\mu \Rightarrow \\
p+1-s-p+ps = 1-\mu \Rightarrow \\
-s+ps = -\mu \Rightarrow \\ 
ps = s-\mu \Rightarrow \\
p = 1-\frac{\mu}{s} 
$$
So $p^*=1-\frac{\mu}{s}$, that is $q^*=\frac{\mu}{s}$, which makes sense - 
the mutant allele is produced by a rate $\mu$ and eliminated at a rate $s$.

The mean fitness is therefore:
$$
\bar{\omega}^* = p^* + (1-p^*)(1-s) = 1-\frac{\mu}{s} + \frac{\mu}{s} (1-s) =
1-\frac{\mu}{s} + \frac{\mu}{s} - s \frac{\mu}{s} \Rightarrow \\
\bar{\omega}^* = 1 - \mu 
$$
This, however, is the mean fitness due to a single locus, not the entire genome.

## Multiple locus

### Extension of single locus model

Moving on to a multiple locus model with an arbitrary number of loci[^loci], we define the mutation rate at locus *j* as $\mu_j$, 
so the mean fitness at the mutation-selection balance in locus *j* is $\bar{\omega}^*_j = 1 - \mu_j$,
and because fitness is multiplicative:
$$
\bar{\omega}^* = \prod_{j}{\bar{\omega}_j^*} = \prod_{j}{1-\mu_j} \Rightarrow \\
ln{(\bar{\omega}^*)} = \sum_{j}{1-\mu_j} 
$$
This can be approximated, because when $x$ is small $ln{(1-x)}\approx -x$, 
and $\mu$ is probably at most $\approx 10^{-2}$ or even lower:
$$
ln{(\bar{\omega}^*)}  \approx \sum_{j}{-\mu_j} = -U
$$
as *U* is the mutation rate per genome per generation.

So This is how we can derive an approximation of the mean fitness at the mutation-selection balance:
$$
\bar{\omega}^* = e^{-U}
$$

You can find this derivation at the begining of a [presentation](http://dx.doi.org/10.6084/m9.figshare.95940)
I gave at the [BioMath Student Journal Club at Tel-Aviv University](http://biomathsjctau.wordpress.com).

### A separate multiple locus model

We can produce the same result without approximations using a different approach.

This time we start with the multiple locus model right away. 
Instead of following allele frequencies, though, we follow the frequency of individuals with *i* mutant alleles,
or *i* deleterious mutations, which we denote by *p~i~*.

We assume that the number of mutations per generation is *Poisson* distributed with the mutation rate as the parameter of the distribution, 
so that the probability that *k* mutations will occur in an individual with a mutaiton rate of *U* is 
$$
\varphi_U(k) = \frac{U^k e^U}{k!}
$$
The equation system describing the change in the freuqnecy of individuals with *i* mutant alleles is:
$$
p'_{i} = \sum_{ k=0 }^{i}{ p_{k} \frac{ \omega_{k} } {\bar{\omega}} \varphi_{U} (i-k)}, \; \; \forall i \ge 0
$$
where $\omega_i$ is the fitness of individuals with *i* mutant alleles.

The above equation system can be written in matrix form:
$$
\bar{\omega}p' = Mp
$$
where $p=(p_0,p_1,p_2,...)$ and *M* is:
$$
M = \left(\begin{array}{cccc}
\omega_0 \varphi_U(0)   & 0            	      		& 0         	       		&  ...\\
\omega_0 \varphi_U(1)   & \omega_1 \varphi_U(0)   	& 0      	          		&  ...\\
\omega_0 \varphi_U(2)   & \omega_1 \varphi_U(1)   	& \omega_2 \varphi_U(0)	    &  ...\\ 
...   		   			& ...          		  		& ...		                &  ...
\end{array}\right)
$$
This matrix is called a [transition matrix](http://en.wikipedia.org/wiki/Stochastic_matrix) 
because its entries $M_{i,j}$ are the transition probabilities from state *j* to state *i* - the state is the number of mutant alleles.

Now if we set $p^*=p'=p$ we get $\bar{\omega}^*p^*=Mp^*$, so that $\bar{\omega}$ is an eigenvalue of $M$. 
Because $M$ is a triangular matrix, the eigenvalues are simply the elements on the main diagonal[^diagonal].
We can use the first equation to find the value of $\bar{\omega}$, assuming $p^*_0>0$:
$$
\bar{\omega}^*p^*_0 = \omega_0 \varphi_U(0) p^*_0 \Rightarrow \\\\
\bar{\omega}^* = \omega_0 \varphi_U(0) = e^{-U}
$$

Note that if beneficial mutations or back-mutations were allowed in this model, 
we would not be able to find the population mean fitness so easily, because the matrix would not be triangular. 
However, in that case we could use the _Perron-Frobenius theorem_ to find that $\bar{\omega}^*$ is the leading eigenvalue 
of the $M$. I've used this approach in our article *The Evolution of Stress-Induced Hypermutation in Asexual Populations* [@Ram2012].

## Summary

We've seen how to find the population mean fitness at the mutation-selection balance $\bar{\omega} = e^{-U}$.

The advantage in the multiple locus model method is that we get some intuition on *why* the population mean fitness is equal to e^-U^.
We found that the population mean fitness at the mutation-selection balance equals 
the probability that the fittest individuals survive to the next generation without mutating.
By definition the fitness of the fittest individuals is 1, and we assumed the number of new mutations is *Poisson* distributed, 
and therefore we got e^-U^, but if we change these assumptions the general result will still hold:

> The mean fitness of an asexual population at the mutation-selection balance, 
> in the absence of beneficial mutations,
> is the product of the fitness of the fittest individuals and the probability that no mutations occur.

What's left?

The next step - in the next post - will be to derive a formula for the mean fitness at each generation.
This is important because we need to understand how *rapidly* the mean fitness converges towards the equilibrium value.
Can we really assume that the evolutionary process has reached the mutation-selection balance in calculations we perform?

One article that presents an analysis on this subject is [@Gordo2005], which shows how to derive the mean fitness of a population at genearation *n*.
This is still a simple asexual population with directional selection and unidirectional deleterious mutations, 
but it is still very interesting, and I'll try to post a comprehensive explanation on how it can be done.

## References

[^locus]: A site on the genome which may be occupied by different alleles. The function of a locus can be diverse - 
genes, transcription control sequences, etc.
[^allele]: A specific sequence occupying a locus, with a specific function. One locus can potentially contain different alleles, 
each with a slightly different sequence and potentially drasticly different effects on function.
[^pprime]: A note on notation - *p'* here is *not* the derivative of *p* but rather the value of *p* at the next generation.
The notation is sometimes confusing but is customary in *population genetics*. 
All equations presented here are *difference equations*, not *differential equations*.
[^loci]: The plural of *locus*.
[^diagonal]: To prove this, 
one must notice that the determinant of a triangular matrix is the trace of the matrix, 
and therefore the characteristic polynomial is the trace of the matrix $I\lambda - M$, 
and the eigenvalues are the solutions of this polynomial - 
see [Paul's online math notes](http://tutorial.math.lamar.edu/Classes/LinAlg/EVals_Evects.aspx#EV_EvalEvec_Thm1).
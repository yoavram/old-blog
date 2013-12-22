title: "Muller's ratchet"
datetime: 2013-12-22 10:11:00 +2
tags: [asexual populations, recombination, mutation accumulation]
category: [research, mutation rate]
math: true
cite: false
draft: true

Following Gordo & Charlesworth [-@Gordo2000].

This Wright-Fisher model starts with a haploid asexual population at a mutation-selection balance. The population size is $N$, the mutation rate is $u$ and the selection coefficient is $s$. 

Denote the frequency of the best class by $x$ and its initial value $x_0 = e^{-u/s}$. The variance of $x$ due to binomial sampling of $N$ individuals from the previous generations is
$$
b(x) = \frac{x(1-x)}{N} \approx \frac{x}{N},
$$

assuming $x \ll 1$. This follows from the variance of a binomial distribution: $Var(Bin(n,p)) = np(1-p)$.

The expected change in $x$ due to mutation and selection is, assuming $\bar{\omega}$ is the current population mean fitness and $\Delta \bar{\omega}$ is the difference between the mutation selection balance (MSB) and the current population mean fitness:
$$
a(x) = \frac{x(e^{-u} - \bar{\omega})}{\bar{\omega}} = x \frac{\Delta \bar{\omega}}{\bar{\omega}},
$$
where the [MSB mean fitness is $e^{-u}$](/mean-fitness-at-the-mutation-selection-balance/).

This follows from the standard difference equation of the frequency of type $z$ after one generation:
$$
f'(z) = f(z) Pr(no \; mutation) \frac{\omega(z)}{\bar{\omega}}
$$

assuming the number of mutations is Poisson distributed with mean $u$ and that the best class has fitness 1.

Next, assume that throughout the process the mean fitness is close enough to the MSB value so that $\Delta \bar{\omega}$ can be modeled as a perturbation. Furthermore, the perturbations are assumed to be a result of fluctuations in the frequency of the best class, $x$.

The mean fitness close to the MSB as a function of $x/x_0$ is expressed as a Taylor expansion around 1:
$$
\bar{\omega} (\frac{x}{x_0}) \approx \bar{\omega}_{eq} + [\frac{\partial \bar{\omega}}{\partial \frac{x}{x_0}}]_{eq} (\frac{x}{x_0}-1) + O((\frac{x}{x_0}-1)^2).
$$ 

This gives a linear approximation for $\Delta \bar{\omega}$ when it is small, that is, when $x\approx x_0$:
$$
\Delta \bar{\omega} \approx K (1-\frac{x}{x_0}), \; K = x_0 [\frac{\partial \bar{\omega}}{\partial x}]_{eq}.
$$

Set $K=0.6 s e^{-u}$ and use this for $a(x)$:
$$
a(x) \approx 0.6 s (1-\frac{x}{x_0}) x.
$$

Using $a(x)$ and $b(x)$ as the drift and diffusion coefficients in a diffusion equation, the time spent in the frequency interval $[0,x_0]$ is:
$$
T_{0,x_0} = \int_0^{x_0}{\frac{2N}{x G(x)} {\int_0^x{G(x')d x'}} dx},
$$

and the time spent in the interval $[x_0,1]$ is:
$$
T_{x_0,1} = \int_{x_0}^1{\frac{2N}{x G(x)} \int_0^{x_0}{G(x') dx'} dx },
$$
where 
$$
G(\xi) = exp[-2 \int_0^{\xi} {\frac{a(z)}{b(z)}dz}] = \\\\
exp[\frac{2N 0.6s}{x_0} \xi (\frac{\xi}{2}-x_0)].
$$

The time to the loss of the best class is then
$$
T(N,u,s) = T_{0,x_0} + T_{x_0,1}.
$$

## References


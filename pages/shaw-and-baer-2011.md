title: 'Summary: "Fitness-dependent mutation rates in finite populations" (Shaw and Baer 2011)'
datetime: 2013-2-19 14:28:00 +2
tags: [recombination, mutators, simulation, asexual populations, stress-induced mutation, mutation-selection balance]
category: [research, mutation rate]
math: true
cite: true
draft: true

[TOC]

## Overview 

### Presentation of Agrawal's results

They start with a summary of the results of @Agrawal2002, who did an infinite population deterministic model:

* In **asexuals**, the mean fitness of SIM at the mutation-selection balance is euqal to $e^{-U}$, just like non-mutators.
* In **sexuals**, the mean fitness of SIM depends on the curveture of the fitness to mutation rate functions - a curveture of $k>1$ will result in a lower equilibrium mean fitness than a curveture of $k<1$.
* The equilibrium genetic load with SIM of asexuals is therefore lower than that of sexuals, increasing the **two-fold cost of sex**.

### Difference from Agrawal's work

* Finite population size - drift, mutational supply?
* non (log)additive fintess - dominance and epistasis

### Difference from previous Muller's Ratchet-Mutator model

Specifically, @Soderberg2011:

* In this work, every mutation is a mutator

## Model

They used **individual-based simulations** with *birth*, *selection*, *mating* and *death*. The population size is *finite* and *constant*, generations are *non-overlapping generations* and there are *2,000 loci*. The population is mutation-free at the beginning.

### Fitness

Fitness is *Fisherian*, that is 
$$
\omega(i) = (1-s)^i
$$
where *i* is the number of mutations and *s* is the selection coefficient. 

With sex, the fitness is $\omega(i) = \prod_{j=1}^{i}{1-h_j s)}$ where *j* is the deleterious locus and $h_j=1$ and $h_j=h$ in homozygous and heterozygous loci and *h* is the dominance coefficient. When $h=0.5$ there is no dominance. 

There is a technical detail that for **asexuals *s=0.02*** and for **sexuals *s=0.04*** because of these fitness definitions.

A population mean fitness of 0.05 classifies as an **extinction event**.

**Epistasis** was modeled by setting the fitness to be $\omega(i) = e^{-is+\alpha i^2}$.

### Mutation rate

The mutation rate was determined by Agrawal's [-@Agrawal2002] formula:

$$
U_{i} = U_{max}-(U_{max}-U_{min})\omega(i)^k
$$

with $U_{min}=0.1$ and $U_{max}=4$. The number of mutations per reproduction is Poisson distributed. 

### Model flow

- Asexuals:
    - Reproduction: an individual is chosen according to its relative fitness.
    - Mutation: the offspring mutates according to its parent mutation rate.
- Sexuals:
    - Reproduction: two individuals are chosen according to their relative fitness, each produces a gamete by chossing one of the alleles at each locus with 5 random crossovers. Two gametes combine to create a new individual.
    - Mutation: the offspring mutates according to its parent mutation rate.

## Results



## References

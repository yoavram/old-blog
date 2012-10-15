title: Mutators and sex in bacteria - Conflict between adaptive strategies" Tenaillon et al. 2000
datetime: 2012-10-15 12:05:00 +2
tags: [mutation, recombination, asexual population, mutators, simulation]
draft: true
math: true

[TOC]

## Overview of [@Tenaillon2000a][Tenaillon]

The stated hypothesis is:  

> The existence of genetic exchanges could modify the dynamics of adaptation and limits the success of mutator alleles.

It is stated that previous models [@Leigh1973; @Johnson1999] have considered mutators in a sexual population, 
but didn't consider the case of adaptation with multiple beneficial mutations - which can involved different _Hill-Robertosn effects_ [@Hill1966].

This hypothesis was tested using simulations. 
Main results, in comparison to [@Tenaillon1999]:

> rare genetic exchanges have a dramatic effect on the fixation of mutators

## Model  
  
The model is an extension of the density-based model[^density-based] used in [@Tenaillon1999]. The extension is the introduction of genetic exchanges. 
Both **conjugation** and **transformation** were used, but only the results of transformation are shown.

  - finite populations
  - directional selection
  - several mutations with various fitness effects
  - colonization of a new environment by a single cell

### Genome

Parentheses show the equivalent number in my work.

  - 1 mutator locus (1)
  - 6 loci for beneficial mutations (4+)
    - with additive effect on fitness: 0.06, 0.04, 0.04, 0.03, 0.03, 0.03 - mean 0.03833 (0.01)
    - all loci treated independently, only one locus will be involved in the process at one time (?)
  - 1,000 loci for deleterious mutations (+-1,000)
    - with additive effect on fitness: 0.05 (0.01)

### Gene transfer

  - Drawing the number of recieved genes from a Poisson distribution
  - Randomly chose the sites, according to the number of sites drawn before
  - Choosing a random allele for each site based on their frequency in the population
  - Constant gene transfer rate 
  
### Parameters

Rate are modified from the original to units of *events per genome per generation*.
(in parentheses are the rates used in my own work for comparison):

  - Mutators increase rates 100-fold. (2-10-fold)
  - Beneficial mutations: 6x10^-8^ based on 10^-8^ per mutation (1.2x10^-5^ - 3x10^-5^ - x200)
  - Deleterious mutations: 10^-4^ [@Kibota1996] (3x10^-3^ - 2.97x10^-3^ [@Drake1991]- x30)
  - Lethal mutations: 10^-5^ (0)
  - Non-mutator to mutator: 5x10^-6^ (0)
  - Mutator to non-mutator: 100x5x10^-10^ = 5x10^-8^ (0)
  - Genetic exchanges: 0, 0.00001, 0.0001, 0.001, 0.01 and 0.1 (0, 0.015 or 0.75)
    - For comparison, *E. coli* do ~5x10^-5^ and *H. pylori* ~3x10^-3^ [@Milkman1990; @Falush2001].
  - Population size: 10^9^, but also 10^5^-10^10^ (10^5^).

## Stats

  - Time of adaptation: no. generations for 95% of population to carry all beneficial mutations
  - Mutator frequency: mean frequency at end of adaptation process over 1,000 replicates
  - Mutator contribution: when mutator frequency < 50% but at least one mutation that appeared in a mutator is present in >50% of population
  - Mutator fixation: frequency >50%
  
## Results

### Recombination reduces mutator fixation

When the rate of genetic exchanges increases, the fixation probability of mutators 
decreases. *Figure 1A* shows this very clearly for a 100-fold mutator 
(point at the figure for a legend, click it for the original):

[![Figure 1]](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F1/)

However, the *B panel* shows that the adaptation time of a mutator population
is still shorter than that of a non-mutator population, even when mutators are loosing. 
This is due to the contribution of mutators to adaptation - 
mutators are **"altruistic"** genes in a recombining population because they 
give away the beneficial mutations they generate. This causes them to lose their 
adaptive advantage and therefore their fixation probability drops, 
but it still increases the ability of the whole population to adapt.

Note that the rates of genetic exchanges are *per gene*.
Converted to *per genome* they would be: 
0, 10^-5^, 10^-4^, 10^-3^, 10^-2^, 10^-1^, 
or in decimal representation:
0, 0.00001, 0.0001, 0.001, 0.01, 0.1. 
Another useful presentation is the *ratio of recombination to mutation*, 
using the highest genomic mutation rate (10^-4^):
0, 0.1, 1, 10, 100, 1000, or compared to the 100-fold mutator:
0, 0.001, 0.01, 0.1, 1, 10.

So we see that as soon as the *recombination to mutation ratio* is 0.1 or lower 
(4^th^ column from the left in *Fig. 1A*, if consider the 100-fold increae),
the fixation probability of mutators is ~50% or more.
One conclusion here could be:

> Mutators can evolve in a recombining population as long as mutation recombination in not more than 10-fold stronger than mutation

### Recombination barriers

A recombination barrier, in the context of these simulations, 
prevents recombination between mutator and non-mutator individuals,
limiting recombination events to within the sub-populations.
This is useful here because it allows to test if the effect of recombination 
on the fixation of mutators is: **1) breaking the linkage** with beneficial mutations, 
or **2) competing adaptive strategy**. 

The result was that the 1^st^ effect was not strong enough to explain
the whole decrease, becuase *recombination barriers*
didn't recover the fixation probability of mutators to their levels 
without recombination. 
No figure presents the data, but the text provides some:
7% fixation instead of 60% with beneficial mutation rate 10^-8^ 
and 0.3% instead  of 16% with a rate of 10^-9^.

### Invasion to a moderate mutator background 

To check that the 2^nd^ effect is the determining effect, 
a 100-fold mutator invaded another mutator (instead of a non-mutator).
The results are in [Figure 2][fig2] - in general the fixation probability 
of a 100-fold mutator drops rapidly when competing with a 10-fold mutator 
and even a 5-fold mutator. This illustrates that competing adaptive strategies
can reduce the fixation of mutators. 

### Recombination accelarates adaptation

Setting the recombination rate at 10^-4^ gene conversions per individual per generations,
the effect of other parameters was investigated:
  
#### Population size
 
 In asexuals, increasing the population size increases the fixation rate of mutators [@Tenaillon1999].
 
 In recombining population, this is not the case. [Figure 3A][Figure 3] shows that for population size <10^6^,
 recombination has a very small effect on the fixation of a 100-fold mutator. However,
 the trends of the fixation probability are completely different for population size >10^-6^.
 In asexual population it increases (rapidly after 10^7^), but in recombining populations it decreases and then increases
 a bit again at 10^9^, but not much, never surprassing 0.2.
 
#### Beneficial mutation rate

Obviously, the lower the beneficial mutation rate, the lower the fixation probability of mutators.
[Figure 4][fig4] shows that increases in the fixation probability of mutators start to show at a beneficial mutation rate of 10^-9^ for asexual populations,
but only at 10^-8^ for sexual populations.

#### Selection coefficient of beneficial mutations

[Figure 5] shows that the negative effect of recombination of the fixation of mutators decreases when the selection coefficient of beneficial mutations increases.
For a selection coefficient of 0.01 [@Kibota1996]  recombination reduced the fixation probability of mutators 17-fold. 
A selection coefficient of 0.1, used in my own work [@Ram2012], falls between the 
two right most points of [Figure 5], 2.5 and 3. The fixation probability of a 
100-fold mutator allele drops ~10-fold due to recombination at a rate of 10^-4^ per gene per generation 
in a population with size 10^9^.

## Discussion
  
## References

[^density-based]: A density-based model is one where the *number* of individuals in each class is monitored and modified from one generation to the next. 
This is in contrast to frequency-dependent models in which the frequency of individuals in each class is monitored.

[Tenaillon]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/

[Figure 1]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/bin/pq1800633001.jpg "A) 100-fold fold mutator, population size 10^-9. B) circle - low mutation rate, square - high mutation rate, triangle - mixed population"

[Figure 2]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F2/
[Figure 3]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F3/
[Figure 4]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F4/
[Figure 5]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F5/
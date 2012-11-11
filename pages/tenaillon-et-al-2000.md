title: 'Summary: "Mutators and sex in bacteria: Conflict between adaptive strategies" (Tenaillon et al. 2000)'
datetime: 2012-10-16 15:22:00 +2
tags: [evolution of the mutation rate, recombination, mutators, simulation, asexual populations]
category: [research, mutation rate]
math: true
cite: true

[TOC]

## Overview 

This post is mostly a technical summary of the paper by **Tenaillon, Le Nagard, Godelle and Taddei [-@Tenaillon2000a][Tenaillon]**.
I wrote the summary because I use it as a baseline for my own research, 
which involves the evolution of stress-induced mutators [@Ram2012a].

The hypothesis the paper deals with is:  

> *The existence of genetic exchanges could modify the dynamics of adaptation and limits the success of mutator alleles[^mutators]*.

It is stated that previous models [@Leigh1973; @Johnson1999] have considered mutators in a sexual population, 
but didn't consider the case of adaptation with **multiple beneficial mutations** - 
which can involve different _Hill-Robertosn effects_ [@Hill1966].

This hypothesis was tested using simulations. 
The main conclusion, in comparison to a previous work in which the authors studies the evolution of mutators [@Tenaillon1999]:

> *Rare genetic exchanges have a dramatic (i.e. negative) effect on the fixation of mutators.*

In addition, the paper presents some evidence on *why* genetic exchanges (recombination) have such an effect of the evolution of mutators.

## Model  
  
The model is an extension of the density-based model[^density-based] used in [@Tenaillon1999]. 
The extension is the addition of genetic exchanges ("bacterial recombination"). 
Both **conjugation** and **transformation** were used, but only the results of transformation are shown.

The model is built using:

  - Finite populations - genetic drift, clonal interference
  - Directional selection - no epistasis, no changing environments
  - Several mutations with various fitness effects
  - Colonization of a new environment by a single cell - adaptive evolution scenario

### Genome

The basic model of the genome
(in parentheses are the values used in my own work for comparison):

  - 1 mutator locus (1)
  - 6 loci for beneficial mutations (4+)
    - with additive effect on fitness: 0.06, 0.04, 0.04, 0.03, 0.03, 0.03 - mean 0.03833 (0.1)
    - all loci treated independently, only one locus will be involved in the process at one time (?)
  - 1,000 loci for deleterious mutations (+-1,000)
    - with additive effect on fitness: 0.05 (0.1)

### Recombination

  - Drawing the number of recieved genes from a *Poisson* distribution
  - Randomly choose the sites, according to the number of sites drawn 
  - Choosing a random allele for each site based on the allele frequency in the population
  - Constant gene transfer rate 
  
### Parameters

Rates are modified from the original to units of *events per genome per generation*.
(in parentheses are the rates used in my own work for comparison):

  - Mutators increase rates: 100-fold (2-10)
  - Beneficial mutations: 6x10^-8^ based on 10^-8^ per mutation (1.2x10^-5^ - 3x10^-5^ - x200)
  - Deleterious mutations: 10^-4^ [@Kibota1996] (3x10^-3^ - 2.97x10^-3^ [@Drake1991]- x30)
  - Lethal mutations: 10^-5^ (0)
  - Non-mutator to mutator: 5x10^-6^ (0)
  - Mutator to non-mutator: 100x5x10^-10^ = 5x10^-8^ (0)
  - Genetic exchanges: 0, 0.00001, 0.0001, 0.001, 0.01 and 0.1 (0, 0.015 or 0.75)
    - For comparison, *E. coli* do ~5x10^-5^ and *H. pylori* ~3x10^-3^ [@Milkman1990; @Falush2001].
  - Population size: mostly 10^9^, also checked 10^5^-10^10^ (10^5^).

## Stats

  - Time of adaptation: no. generations for 95% of population to carry all beneficial mutations
  - Mutator frequency: mean frequency at end of adaptation process over 1,000 replicates
  - Mutator contribution: when mutator frequency < 50% but at least one mutation that appeared in a mutator is present in >50% of population
  - Mutator fixation: frequency >50%
  
## Results

### Recombination reduces mutator fixation

When the rate of genetic exchanges increases, the fixation probability of mutators 
decreases. *Figure 1A* shows this very clearly for a 100-fold mutator:

[![Figure 1]](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F1/)

> Figure 1 from @Tenaillon2000a. 
> A) Fixation probability of a 100-fold fold mutator, population size 10^-9. 
> B) Adaptation times of populations with: circle - low mutation rate, square - high mutation rate, triangle - mixed populations.

However, the *B panel* shows that the adaptation time of a mutator population
is still shorter than that of a non-mutator population, even when mutators are loosing. 
This is due to the contribution of mutators to adaptation - 
in a recombining population mutators are **"altruistic"** alleles because they 
give away the beneficial mutations they generate. This causes them to lose their 
adaptive advantage and therefore their fixation probability drops, 
but it still increases the ability of the whole population to adapt.

Note that the rates of recombination in the figure are *per gene*.
Converted to *per genome* they would be: 
0, 10^-5^, 10^-4^, 10^-3^, 10^-2^, 10^-1^, 
or in decimal representation:
0, 0.00001, 0.0001, 0.001, 0.01, 0.1. 
Another useful presentation is the *ratio of recombination to mutation*, 
using the highest genomic mutation rate (10^-4^):
0, 0.1, 1, 10, 100, 1000, or compared to the 100-fold mutator:
0, 0.001, 0.01, 0.1, 1, 10.

So we see that as soon as the *recombination to mutation ratio* is 0.1 or lower 
(4^th^ column from the left in *Fig. 1A*, if we consider the 100-fold increae),
the fixation probability of mutators is ~50% or more.
The conclusion here could be that mutators can evolve in a recombining population as long as recombination in not more than 10-fold stronger than mutation

Of course this *10-fold* estimate is highly dependent on the other paramters: the population size, the selection coefficients,
the beneficial mutation rate, not to mention parameters that are not dealt with here such as epistasis. 

### Recombination barriers

A recombination barrier, in the context of these simulations, 
prevents recombination between mutator and non-mutator individuals,
limiting recombination events to within the sub-populations.

This is useful here because it allows to test if the source of the effect of recombination 
on the fixation of mutators is: **1) breaking the linkage** of the mutator with the beneficial mutations it generates, 
or **2) competing adaptive strategy**. 

The 1^st^ effect is usually called the **hitch-hiking effect**, or **selective sweeps** [@Charlesworth2007]: 
mutators can "hitch-hike" with the beneficial mutations they generate to high frequencies as long as the
LD (linkage disequilibrium) between them is intact. 
recombination tends to break this LD, robbing the mutators from their precious beneficial mutations.
Even worse, recombination doesn't only take away the beneifical mutations, 
it even gives them to the mutators' "rivals" - the competing non-mutator alleles.

The 2^nd^ effect is general - *competing adadptive strategy*. How is recombination an *adaptive strategy*?

Asexual populations are limited by **clonal interference** [@Gerrish1998; @Martens2011]. 
The following figure illustrates the idea:

[![Clonal Interference]](http://en.wikipedia.org/wiki/Clonal_interference)

> Clonal interference diagram from [Wikipedia](http://en.wikipedia.org/wiki/File:Evolsex-dia2a.svg).
> This diagram illustrates how sex might create novel genotypes more rapidly. 
> Two beneficial mutations A and B occur at random. The two mutations are recombined rapidly in a sexual population (top), 
> but in an asexual population (bottom) the two mutations must independently arise because of clonal interference.
> The effect of recombination and sex on the adaptation rate via the reduction of *clonal interference* is also called the *Fisher-Muller effect*.

If the reduction in fixation probability is due to the 1^st^ effect - 
separation of the mutators from the beneficial mutations they generate - 
then *recombination barriers* are expected to revert the outcome, at least partially, to that of asexual populations.

However, the results showed that *recombination barriers*
didn't recover the fixation probability of mutators to their levels without recombination.
No figure presents the data, but the text provides some information:
7% fixation instead of 60% with beneficial mutation rate 10^-8^ 
and 0.3% instead  of 16% with a rate of 10^-9^.
The conclusion is therefore that the 1^st^ effect is not enough to explain 
the reduction in the mutators adaptive advantage in the presence of recombination.

### Invasion to a moderate mutator background 

To check that the 2^nd^ effect is the determining effect, 
a 100-fold mutator invaded another mutator (instead of a non-mutator).
The results are in [Figure 2] - in general the fixation probability 
of a 100-fold mutator drops rapidly when competing with a 10-fold mutator 
and even a 5-fold mutator. 

This illustrates that competing adaptive strategies can reduce the fixation of mutators, 
and therefore that is is plausible that this is why recombination reduces the fixation of mutators. 

### Recombination accelarates adaptation

Setting the recombination rate at 10^-4^ gene conversions per individual per generations,
the effect of other parameters was investigated:
  
#### Population size
 
 In asexuals, increasing the population size increases the fixation rate of mutators [@Tenaillon1999].
 
 In recombining populations, this is not the case. [Figure 3A][Figure 3] shows that for a population size <10^6^,
 recombination has a very small effect on the fixation of a 100-fold mutator. However,
 the trends of the fixation probability are completely different for population size >10^-6^.
 In asexual populations it increases (rapidly after 10^7^), but in recombining populations it decreases and then increases
 a bit again at 10^9^, but not much, never surprassing 0.2.
 
#### Beneficial mutation rate

The lower the beneficial mutation rate, the lower the fixation probability of mutators.
[Figure 4] shows that the fixation probability of mutators starts to increase at a beneficial mutation rate of 10^-9^ for asexual populations,
but only at 10^-8^ for sexual populations.

#### Selection coefficient of beneficial mutations

[Figure 5] shows that the negative effect of recombination of the fixation of mutators decreases when the selection coefficient of beneficial mutations increases.

For a selection coefficient of 0.01 [@Kibota1996]  recombination reduced the fixation probability of mutators 17-fold. 

A selection coefficient of 0.1, used in my own work [@Ram2012a], falls between the 
two right most points of [Figure 5] - 2.5 and 3 - and the fixation probability of a 
100-fold mutator allele drops ~10-fold due to recombination at a rate of 10^-4^ per gene per generation 
in a population with size 10^9^.

## Discussion

This paper is *packed* with interesting results. 
The effect of recombination on mutator evolution has not recieved alot of treatment using simulation 
(but see @Levin2009 and @Sloan2010 on which I hope to write some other time).
So this is really interesting to someone interesed in the evolution of the mutation rate, even 12 years later.

This work shows that indeed recombination has an effect on mutator evolution, and that this effect is highly sensitive - it is
(I'm concentrating on when the effect is weak because that's when mutators are still going to evolve):

  - Weak in small populations (<10^7^-10^8^)
  - Weak for high beneficial mutation rates (>10^-8^-10^-7^)
  - Weaker for strong/intermediate selection
  
It seems that in general the effect of recombination on mutator evolution (that is, on the evolution of high mutation rates)
is weak when the adaptation rate of the population is low. 
In turn, the adaptation rate is a function of the **supply of beneficial mutations** which is a function of population size and beneficial mutation rate,
and of **fixation time of beneficial mutations** which is a function of population size and selection strength. 

Selection of mutators is **second-order selection**, in the sense that it indirectly affecting mutators. 
Because their results imply that second-order selection of mutators is very sensitive to the system parameters,
*Tenaillon et al.* propose that it may be unable to optimize the rates of mutation - 
in the sense that mutators will not be selected even when increasing the mutation rate will be beneficial to the population, 
in terms of fitness and adaptation rate.
This can be resolved by **transient hypermutation**:

> Sex would therefore help bacteria approach an optimized mutation rate strategy composed of 
> shifts towards high mutation rates in phases of adaptation under strong selective pressure 
> and rapid recovery of low mutation rate once adaptation is achieved.

This view was also proposed by Ninio [-@Ninio1991] and expanded in a review from the same lab 
with the attractive title *The Rise and Fall of Mutator Bacteria* [@Giraud2001].

I'm not sure if and how these results would change if a weaker mutator (10-fold mutation rate increase?) was used instead of the strong mutator (100-fold).
For example, a paper from the same lab [@Taddei1997] 
showed that a 10-fold mutator is more successful in invading finite populations (see [Figure 3A](http://www.nature.com/nature/journal/v387/n6634/fig_tab/387700a0_F3.html)).

I learned alot from this paper (and it predecessors [@Taddei1997; @Tenaillon1999]) about how to think of evolutionary simulations.
And of course the science itself - 
the diverse network of interactions and effects between selection, drift, mutation and recombination.

## References

[^density-based]: A density-based model is one where the *number* of individuals in each class is monitored and modified from one generation to the next. 
This is in contrast to frequency-dependent models in which the frequency of individuals in each class is monitored.
[^mutators]: Alleles that increase the global mutation rate. For example, 
a mutant allele of the *mutS* gene can reduce the efficiency of DNA repair, 
allowing more mutations to slip though the repair mechanisms.

[Tenaillon]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/

[Figure 1]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/bin/pq1800633001.jpg
[Clonal Interference]: http://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Evolsex-dia2a.svg/500px-Evolsex-dia2a.svg.png 

[Figure 2]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F2/
[Figure 3]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F3/
[Figure 4]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F4/
[Figure 5]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC27047/figure/F5/

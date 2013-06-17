title: 'Summary: "Mutation rates: How low can you go?" (Sniegowski and Raynes 2013)'
datetime: 2013-06-16 14:29:00 +2
tags: [evolution of the mutation rate]
category: [research, mutation rate]
math: true
cite: false
draft: false

This is a short summary of [Sniegowski and Raynes [-@Sniegowski2013]](http://www.sciencedirect.com/science/article/pii/S0960982213000213), a review about the evolution of the mutation rate, with an emphasis on the **Drift Barrier Hypothesis** (DBH). The summary is written in my own words, with a few footnotes and highlighting that express my thoughts.  

1. Because most mutations are deleterious, **selection favors decreased mutation rates**[^1]
2. Then what keeps the mutation rate from dropping to *zero*?
1. One force *could* be **adaptive evolution** which creates selection for the generation of beneficial mutations [^2]. This selection, however, is limited [@Sniegowski2000].
1. Another force can be the fitness cost of increasing genomic replication fidelity[^4]. This doesn't seem to solve the problem, mainly because although the cost of fidelity in prokaryotes should be higher than in eukaryotes, the genomic mutation rate is lower[^5].
1. There is also a physio-chemical constraint on the fidelity of replication and repair mechanisms[^3]. But this constraint should be similar to all species so it cannot explain the diversity.
1. **DBH** [@Sung2012]: Reduction of the mutation rate has a diminishing effect on fitness[^8] and therefore at some point selection towards low mutation rates is weaker than drift. This effect is highly dependent on the **population size**.
3. **"Drake's Rule"**: genomic mutation rates of DNA microbes[^6]  are very similar (0.003 mutations per genome per generation) - the per base-pair mutation rate decreases with the genome size [@Drake1991]. This suggest a universal selective force which acts to adjust the mutation rate of microbes. This rule was recently tested and confirmed in *C. reinhardtii* and *M. florum* [@Sung2012a], and it fits with the DBH, as microbes usually have very large populations.
4. In contrast, in **eukaryotes**, however, the per base-pair and genomic **mutation rate increases with genome size**. This fits with the DBH, because eukaryotes presumebly have small effective population sizes.
5. However, it is noted that both mutation rates and effective population sizes are very hard to measure and estimate.

# References

[^1]: The reduction principle [@Liberman1986]
[^2]: Second-order selection [@Taddei1997; @Sniegowski1997]
[^3]: However, anti-mutators do exist [@Loh2010], so it seems that the mutation rate is not at its lower physio-chemical level
[^4]: The cost of fidelity argument [@Dawson1998]
[^5]: AFAIK, this cost was mainly shown in viruses so far [@Furio2005], but a recent study did show some direct advantage of mutators which do not depend on replication fidelity *per se* [@Torres-Barcelo2013]
[^6]: That is, not including RNA viruses
[^8]: Why? Because, as we have seen in [previous posts](/mean-fitness-at-the-mutation-selection-balance/), the population mean fitness decays exponentialy as the genomic per generation mutation rate increases: $\bar{\omega} = e^{-U}$.
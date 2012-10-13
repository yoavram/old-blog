title: Mean fitness at the mutation-selection balance

tags: [mutation-selection balance, mean fitness, deleterious mutations, asexual populatins, math explained]
cite: true
math: true

## Following Gordo and Dionisio, 2005[^GD2005]

1.  The number of new mutations per individual per generation is
Poisson distributed with parameter U.
1.  The frequency of individuals with *i* mutations in
generation *g* is denoted $f_{i}(g)$ and $
\sum_{i}{f_{i}(g)}=1$$^{ }$
1.  All mutations are deleterious with a multiplicative effect, so
that an individual with $i$ mutations has fitness $\omega_{i}:=(1-s)^{i}$ with selection coefficient $0<s<1$.
1.  The population mean fitness at generation g will be denoted $\bar{\omega }_{g}=\sum_{i}{f_{i}(g)\omega _{i}}$.
1.  We assume that the selection precedes mutation
1.  Denote the PMF of Poisson distribution with parameter $\lambda$: $\phi (x|\lambda )$
1.  The master equations for the frequency of individuals with
*i* mutations at generation *g+1* is:
$$
f_{i}(g+1)=\sum_{k=0}^{i}{\frac{\omega _{k}}{\bar{\omega}_{g}}f_{k}(g)\frac{U^{i-k}}{(i-k)!}e^{-U}}
$$
1.  We start from a mutation-free population: $f_{0}(0)=1$.
1.  The frequency of individuals with *i* mutations at generation 1 will be:
$$
f_{i}(1)=\sum_{k=0}^{i}{f_{k}(0)\frac{\omega _{k}}{\bar{\omega}_{1}}\cdot \frac{U^{i-k}}{(i-k)!}e^{-U}}
$$
1.  And because 
$$
f_{k}(0)=\bigg\{
\begin{gathered}
1, k=0 \\
0, otherwise \\
\end{gathered}
$$
1.  We get that $f_{i}(1) = f_{0}(0)\frac{\omega _{0}}{\bar{\omega }_{1}} \cdot \frac{U^{i}}{i!}e^{-U} = \frac{U^{i}}{i!}e^{-U}$
1.  So the frequency of individuals with *i* mutations at
generation 1 is Poisson distributed with parameter U
1.  To verify this: the expected number of mutations at generation 1 is 
$$
\sum_{i\ge 0}{i\cdot f_{i}(1)} = \sum_{i\ge 1}{i\cdot \frac{U^{i}}{i!}e^{-U}} =\\ 
e^{-U}U\sum_{i\ge 1}{\frac{U^{i-1}}{(i-1)!}} = \\ 
e^{-U}U\sum_{i\ge 0}{\frac{U^{i}}{i!}} = \\ 
Ue^{-U}e^{U} = U
$$
as expected.
1.  The frequency of individuals with *i* mutations at
generation 2 after selection and before mutation is:
$$
f_{i}^{s}(2) = \frac{\omega _{i}}{\bar{\omega}_{1}}f_{i}(1) = \\
\frac{(1-s)^{i}}{\sum_{k=0}^{\infty }{f_{k}(1)\omega_{k}}}\frac{U^{i}}{i!}e^{-U} = \\
\frac{(1-s)^{i}}{\sum_{k=0}^{\infty}{\frac{U^{k}}{k!}e^{-U}(1-s)^{k}}}\frac{U^{i}}{i!}e^{-U} = \\
\frac{(U(1-s))^{i}}{i!\sum_{k=0}^{\infty}{\frac{(U(1-s))^{k}}{k!}}} = \\
\frac{(U(1-s))^{i}}{i!}e^{-U(1-s)}
$$
1.  Therefore, $f_{i}^{s}(2)$ is Poisson distributed with parameter $U(1-s)$, and: 
$$
f_{i}(2) = \sum_{k=0}^{i}{f_{k}^{s}(2)\frac{U^{i-k}}{(i-k)!}e^{-U}} = \\
\sum_{k=0}^{i}{\frac{(U(1-s))^{k}}{k!}e^{-U(1-s)}\frac{U^{i-k}}{(i-k)!}e^{-U}} = \\
e^{-U(1-s)-U}\sum_{k=0}^{i}{\frac{U^{i-k}(U(1-s))^{k}}{k! \cdot (i-k)!}} = \\
\frac{U^{i}}{e^{U(1-s) + U}} \sum_{k=0}^{i}{\frac{(U(1-s))^{k}}{U^{k} \cdot k! \cdot (i-k)!}} = \\
\frac{U^{i}}{e^{U(1-s) + U}} \sum_{k=0}^{i}{\frac{(1-s)^{k}}{k! \cdot (i-k)!}}
$$
1.  Note that 
$\sum_{k=0}^{i}{\frac{q^{k}}{k!\cdot (i-k)! }} = \frac{(q+1)^{i}}{i!}$ And $\sum_{k=1}^{i}{\frac{q^{k}}{k!\cdot (i-k)! }}=\frac{(q+1)^{i}-1}{i!}$
1.  Therefore:
$$
f_{i}(2) = \frac{U^{i}}{e^{U(1-s)+U}}\cdot \frac{(2-s)^{i}}{i!} = \\
\frac{(U(1-s)+U)^{i}}{i!}e^{-(U(1-s)+U)} = \\
\phi(i | U(1-s)+U)
$$
1.  Similarly to the former expansion and because the Poisson process is _memoryless_, 
the frequency of individuals with *i* mutations after mutation at generation 2 will be Poisson distributed with parameter $U(1-s)+U$.
1.  We can now build the recurrence relation for the expected number of
mutations (or the parameter of the Poisson distribution of mutations):
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
1.  To summarize, we got $\lambda (g+1)=\lambda (g)(1-s)+U$ 
1.  And $\lambda (1)=U$
1.  The solution to this recurrence relation is:
$$
\lambda(g)=\frac{U}{s}(1-(1-s)^{g})\xrightarrow{g\to \infty }\frac{U}{s}
$$
1. For a sinlge-locus deterministic model, $\frac{U}{s}$ is the expected frequency of the wild-type allele (assuming that $s>>U$, which agrees well with the expected number of mutation-free individuals,
$\phi(0 | \frac{U}{s}) = \frac{\frac{U}{s}^0}{0!} e^{-\frac{U}{s}} = e^{-\frac{U}{s}} \approx \frac{U}{s}$. The last approximaation is the approximation of the exponential function close to 0. 
1.  Denoting the expected number of deleterious mutations after *g* generations as $\lambda =\lambda (g)$, we get that the population mean fitness after *g* generations is:
$$
\bar{\omega}_{g} = \sum_{i=0}^{\infty }{\frac{\lambda(g)^{i}}{i!}e^{-\lambda(g)}(1-s)^{i}} = \\ 
e^{-\lambda(g)}\sum_{i=0}^{\infty}{\frac{ (\lambda(g) (1-s))^{i}}{i!}} = \\
e^{-\lambda(g)}e^{\lambda(g)(1-s)} \Rightarrow \\
\bar{\omega}_{g} = e^{-\lambda(g) s}
$$
1. And the population mean fitness at the mutation-selection balance (the equilibrium) is:
$$
\bar{\omega }^* = e^{-\lambda(g) s} \xrightarrow{g\to \infty}e^{-\frac{U}{s}s} = e^{-U}
$$
1. The second moment of the population fitness is given by:
$$
E[\omega_g^2] = \sum_{i=0}^{\infty }{\frac{\lambda(g)^{i}}{i!}e^{-\lambda(g)}(1-s)^{2i}} = \\
e^{-\lambda(g)} \sum_{i=0}^{\infty }{\frac{ (\lambda(g)(1-s)^2)^{i} }{i!}} = \\
e^{-\lambda(g)} e^{\lambda(g)(1-s)^2} = \\
e^{\lambda(g)(1-2s+s^2)-\lambda(g)} = \\
e^{\lambda(g)-2\lambda(g)s+\lambda(g)s^2-\lambda(g)} = \\
e^{\lambda(g)s^2-2\lambda(g)s}
$$
1. F statistic ....
1. Which agrees with the famous result of Kimura & Maruyama, 1966[^KM1966].
1. In mutation-accumulation experiments, a population is undergoing a sequence of bottlenecks that cause the accumulation of mutations due to the ineffectivness of selection when the effective population size is small. These experiments usually use measurements of mean and variance population fitness to estimate *s* and *U*. For this purpose one may use the approximation of $\bar{\omega}^* = e^{-U}.
1. In a population of bacteria, however, the number of generations between bottlenecks may be insufficient for the population to reach a mutation-selection balance. In this case one muse use a non-equilibrium value of the mean fitness, which is $\bar{\omega}_g = e^{-\frac{U}{s} (1-(1-s)^{g})}$. This is the subject of the Gordo & Dionisio, 2005[^GD2005] paper, titled: *Nonequilibrium model for estimating parameters of deleterious mutations*. The paper explores a statistical model based on the above calculations. The statistical model is tested against results of simulations. A later paper, Trindade *et al.*, 2010[^Tri2010], they tested this statistical model on results of a mutation accumulation experiment with *E. coli*.

### Footnotes

I originally wrote this post with [Office 2010](http://en.wikipedia.org/wiki/Microsoft_Office_2010). I converted it TeX using [docx2tex](http://docx2tex.codeplex.com/) and from [TeX](http://en.wikipedia.org/wiki/LaTeX) to [Markdown](http://daringfireball.net/projects/markdown/) using [LaTeX2Markdown](https://github.com/ajtulloch/LaTeX2Markdown). Then I proof-read it, and several LaTeX bugs were identified and fixed using an online tool for [testing MathJax code](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm) \([MathJax](http://www.mathjax.org/) is a JavaScript library that displays LaTeX in browsers, see how in [another post](/blogging-with-math-and-code)\).

###  References

[^GD2005]: Gordo I, Dionisio F (2005) Nonequilibrium model for estimating parameters of deleterious mutations. *Physical Review E* 71: 18-21. doi: [10.1103/PhysRevE.71.031907](http://link.aps.org/doi/10.1103/PhysRevE.71.031907)
[^KM1966]: Kimura M, Maruyama T (1966) The mutational load with epistatic gene interactions in fitness. *Genetics* 54: 1337-1351. PMID: [17248359](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=1211299)
[^Tri2010]: Trindade S, Perfeito L, Gordo I (2010) Rate and effects of spontaneous mutations that affect fitness in mutator Escherichia coli. *Phil Trans of Roy Soc B 365: 1177-1186. doi: 10.1098/rstb.2009.0287. PMID: [20308092](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=2871818)

///Footnotes Go Here///

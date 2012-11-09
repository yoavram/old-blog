title: Creating phylogenies of simulated data
datetime: 2012-11-09 11:54:00 +2
tags: [R, phylogeny]
draft: true

[TOC]

## Software

1. R
2. RStudio
3. [ade4](http://pbil.univ-lyon1.fr/ade4/home.php?lang=eng)
4. [graph](http://www.bioconductor.org/packages/release/bioc/html/graph.html) package for R
5. [Rgraphviz](http://www.bioconductor.org/packages/2.11/bioc/html/Rgraphviz.html)

## Newick Tree

[The Newick tree format](http://evolution.genetics.washington.edu/phylip/newicktree.html)

### Hello Newick Tree!

Here's a quick example from the [ade4 docs](http://pbil.univ-lyon1.fr/ade4/ade4-html/newick2phylog.html):

	library(ade4)
	w <- "((((,,),,(,)),),(,));"
	w.phy <- newick2phylog(w)
	print(w.phy)
	plot(w.phy)

which gives this nice tree:
![Hello Newick Tree!](http://i.imgur.com/mkeRG.png)

## Graph & Rgraphviz

Newick tree seems like a cool way to plot the tree, but how will I construct the Newick tree string? I need something else. A graph could be the way, I start with the 0 strain at the root and build the graph-tree from there.

### Hello Rgraphviz!

Following the[Rgraphiv docs](http://www.bioconductor.org/packages/2.11/bioc/vignettes/Rgraphviz/inst/doc/Rgraphviz.pdf):

	library(Rgraphviz)
	V <- letters[1:10]
	M <- 1:4
	g1 <- randomGraph(V, M, 0.5)
	plot(g1)

which gives this graph:
![Hello Rgraphviz!](http://i.imgur.com/DE6L0.png)

## Phylogny tree for *mamba*

The [mamba](https://github.com/yoavram/mamba) project is a *Wright-Fisher* model simulator. To create a phylogeny tree for the populations of the *mamba* project I wrote [*tree.R*](https://github.com/yoavram/mamba/blob/master/tree.R).

An example output can be produced by running <code>test.tree()</code> from *tree.R*:

![Hello mamba tree!](http://i.imgur.com/YVKef.png)

## Hello Shiny!

I also made a [Shiny app that plots a random graph](https://gist.github.com/4045750).

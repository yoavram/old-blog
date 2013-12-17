title: Doing phylogenetics
datetime: 2013-09-01 13:32:00 +2
tags: []
category: []
draft: true

1. Got the book "Phylogenetic trees made easy" by Barry G. Hall
1. Downloaded [MEGA](http://www.megasoftware.net/index.php) for Windows
1. Downloaded [MrBayes](http://sourceforge.net/projects/mrbayes) for Windows
1. Read part of Ch. 5 to decide on the inference method
1. Decided to start working with NJ method - it's the fastest and I don't care too much about accuracy.
1. Ch. 6 is on NJ method - start working with MEGA 5.2.2
1. Opened 2013-Aug-06_14-48-04-878278.fasta for analysis (already aligned), which is a result of evolution in 20 degrees (T20).
1. Determined the average JC distance to see if the data is suitable for NJ (it has to be <1.0) Distances - > Compute overall mean distance..., Model/Method->Jukes-Cantor model, Compute. *Result is 0.001*.
1. Phylogeny->Contruct/test NJ tree. Model/method Jukes-Cantor. Compute!
1. The output tree is disappointing, but I guess this is what you get for a MSB tree. Let's try it with T42 output.
1. Created 2013-Aug-08_16-59-21-797336.fasta with the IPython notebook phylotree and verified that it is the result of adaptive evolution (mean fitness changed from 0.48 to >0.9)
1. Average JC distance is still 0.001
1. Nice. This time we actually have a tree - saved as 2013-Aug-08_16-59-21-797336.mts. It seems that there were two adaptation events - one to fitness 0.95 and one to fitness 0.977 and the later has some variation.

datetime: 2012-10-16 10:38:00 +2
title: Image with links in Markdown
draft: true
tags: [markdown]

[TOC]

See the [Pandoc Documentation](http://johnmacfarlane.net/pandoc/README.html#images)

## Inline 

	![Clonal Interferece](http://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Evolsex-dia2a.svg/500px-Evolsex-dia2a.svg.png "Sex helps the spread of advantageous traits through recombination. The diagrams compare evolution of allele frequency in a sexual population (a) and an asexual population (b). The vertical axis shows frequency and the horizontal axis shows time. The alleles a/A and b/B occur at random. The advantageous combination AB arises rapidly with recombination (a), but must arise independently in (b).")

![Clonal Interferece](http://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Evolsex-dia2a.svg/500px-Evolsex-dia2a.svg.png "Sex helps the spread of advantageous traits through recombination. The diagrams compare evolution of allele frequency in a sexual population (a) and an asexual population (b). The vertical axis shows frequency and the horizontal axis shows time. The alleles a/A and b/B occur at random. The advantageous combination AB arises rapidly with recombination (a), but must arise independently in (b).")

## Reference

	![Butterfly]

	[Butterfly]: http://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Neopithecops_zalmora_by_Kadavoor.JPG/320px-Neopithecops_zalmora_by_Kadavoor.JPG "Nice butterfly"

![Butterfly]

[Butterfly]: http://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Neopithecops_zalmora_by_Kadavoor.JPG/320px-Neopithecops_zalmora_by_Kadavoor.JPG "Nice butterfly"

## Figure with Caption

	What kind of animal do you see in the following figure?

	![Figure 1](http://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Asilidae_2_by_kadavoor.jpg/320px-Asilidae_2_by_kadavoor.jpg)

	Is it a wasp?

What kind of animal do you see in the following figure?

![Figure 1](http://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Asilidae_2_by_kadavoor.jpg/320px-Asilidae_2_by_kadavoor.jpg)

Is it a wasp?

## Image without caption

	This is a nice image of the mountains
	![This image won't be a figure](http://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Lake_Kinney_mit_Mount_Whitehorn.jpg/320px-Lake_Kinney_mit_Mount_Whitehorn.jpg)
	don't you think?

This is a nice image of the mountains
![This image won't be a figure](http://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Lake_Kinney_mit_Mount_Whitehorn.jpg/320px-Lake_Kinney_mit_Mount_Whitehorn.jpg)
don't you think?

## Inline with link

See [stackoverflow](http://meta.stackoverflow.com/questions/2133/whats-the-recommended-syntax-for-an-image-with-a-link).

	[![Dromaius novaehollandiae](http://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Dromaius_novaehollandiae_%28head%29_Battersea_Park_Children%27s_Zoo.jpg/180px-Dromaius_novaehollandiae_%28head%29_Battersea_Park_Children%27s_Zoo.jpg "Emu (Dromaius novaehollandiae) head and upper neck, Battersea Park Children's Zoo in South London, England.") ](http://commons.wikimedia.org/wiki/File:Dromaius_novaehollandiae_(head)_Battersea_Park_Children%27s_Zoo.jpg "Wikimedia")
	
[![Dromaius novaehollandiae](http://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Dromaius_novaehollandiae_%28head%29_Battersea_Park_Children%27s_Zoo.jpg/180px-Dromaius_novaehollandiae_%28head%29_Battersea_Park_Children%27s_Zoo.jpg "Emu (Dromaius novaehollandiae) head and upper neck, Battersea Park Children's Zoo in South London, England.") ](http://commons.wikimedia.org/wiki/File:Dromaius_novaehollandiae_(head)_Battersea_Park_Children%27s_Zoo.jpg "Wikimedia")

## Reference with link

	[![Interior of San Thome Basilica][san-thome-img]][san-thome-link]

	[san-thome-img]: http://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Interior_of_San_Thome_Basilica.jpg/320px-Interior_of_San_Thome_Basilica.jpg
	[san-thome-link]: http://commons.wikimedia.org/wiki/File:Interior_of_San_Thome_Basilica.jpg "Interior of San Thome Basilica in Chennai, Tamil Nadu, India."

[![Interior of San Thome Basilica][san-thome-img]][san-thome-link]

[san-thome-img]: http://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Interior_of_San_Thome_Basilica.jpg/320px-Interior_of_San_Thome_Basilica.jpg
[san-thome-link]: http://commons.wikimedia.org/wiki/File:Interior_of_San_Thome_Basilica.jpg "Interior of San Thome Basilica in Chennai, Tamil Nadu, India."

## With link and caption

	[![petra-img]][petra-link]
	
	> El Deir ("The Monastery") in the ancient city of Petra, Jordan. Source: [Diego Delso](http://toolserver.org/~daniel/WikiSense/Gallery.php?wikifam=commons.wikimedia.org&img_user_text=Poco_a_poco)

	[petra-img]: http://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/The_Monastery%2C_Petra%2C_Jordan8.jpg/320px-The_Monastery%2C_Petra%2C_Jordan8.jpg
	[petra-link]: http://commons.wikimedia.org/wiki/File:The_Monastery,_Petra,_Jordan8.jpg 'El Deir ("The Monastery") in the ancient city of Petra, Jordan'

[![petra-img]][petra-link]

> El Deir ("The Monastery") in the ancient city of Petra, Jordan. Source: [Diego Delso](http://toolserver.org/~daniel/WikiSense/Gallery.php?wikifam=commons.wikimedia.org&img_user_text=Poco_a_poco)

[petra-img]: http://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/The_Monastery%2C_Petra%2C_Jordan8.jpg/320px-The_Monastery%2C_Petra%2C_Jordan8.jpg
[petra-link]: http://commons.wikimedia.org/wiki/File:The_Monastery,_Petra,_Jordan8.jpg 'El Deir ("The Monastery") in the ancient city of Petra, Jordan'

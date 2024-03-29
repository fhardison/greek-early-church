# Greek Early Church

In this repo you will find the text and lemmatisation of the following works:

* _To the Newly Baptized_ by Clement of Alexandria.
* _Paschal Homily_ by John Chrysostom

These texts are being prepared as part of the [Greek Learner Texts Project](https://greek-learner-texts.org/).

## Contributors

* Fletcher Hardison

## Source

### _To the Newly Baptized_

I'd like to thank [Peter Kerby](http://www.earlychristianwritings.com/) for kindly allowing me to us his digitization of the The [Greek text](http://www.earlychristianwritings.com/text/clement-baptized-uni.html) of _To the Newly Baptized_ taken from Butterworth's _Clement of Alexandria_. He cites his source as "Butterworth's Clement of Alexandria, pp. 370-377 in the Loeb Classical Library, first printed 1919".

### _Paschal Homily_

The following Google Books scans of Migne's volume 59 were consulted.

* <https://books.google.co.uk/books?id=czuFE42hAXoC&pg=PP2#v=onepage&q&f=false> (starting on page 721)
* <https://books.google.com/books?id=z09JD5utn_4C>
* <https://books.google.com/books?id=-7rUAAAAMAAJ>

line breaking for the Homily is based on the English version found at [Orthodox Wiki](https://orthodoxwiki.org/Paschal_Homily) which is under a [CC BY-SA 2.5 License](https://creativecommons.org/licenses/by-sa/2.5/) and the [GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.html)


## Progress

| Text | Formatted | Lemmatisation | Sentence/Paragraph start/end | Notes |
|:--|:--|:--|:--|:--|
| To the Newly Baptized | Y | Y | N | *Note that the title (line `1.0.head` in the text) was not included in the lemmatisation.*|
| Paschal Homily | Y | Y | N | |

## Tasks

### build

```
python3 scripts/build_site.py > temp.md
pandoc -o docs/paschal_homily.html --template=scripts/homer_site_template.html --metadata title="Pachal Homily" temp.md 
rm temp.md
```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

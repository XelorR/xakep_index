#!/usr/bin/env bash

parallel wget -O {}.html https://xakep.ru/issues/xa/{.} ::: {001..259}
js-beautify -l 2 -r *.html


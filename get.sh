#!/usr/bin/env bash

# wider available version:
# for i in {001..259}; do echo downloading $i; curl -sLo $i.html  https://xakep.ru/issues/xa/$i; done

parallel wget -O html/{}.html https://xakep.ru/issues/xa/{.} ::: {001..262}
# js-beautify -l 2 -r *.html


# Uruguay Aduanas

Scraper escrito usando CasperJS/PhantomJS como browser headless.  
Desenhado para obter os dados públicos (mas mal expostos) do site https://servicios.aduanas.gub.uy/LuciapubX/hpudbar2.aspx  

## Dependencias

Para rodar este projeto, é necessário ter instalado o phantomjs >= 1.9.1 e o casperjs >= 1.1

## Uso

Por conta de [um defeito no manejo de https] por parte do PhantomJS, temos que usar a opção `--ignore-ssl-errors=true`

O primeiro script escreve o arquivo `tipos.txt`, que contém uma lista dos tipos de partidas.
Para cada tipo, é necessário rodar o segundo script com o parametro `--tipo=01`, substituindo `01` pelo codigo de tipo.

## TODO

[ ] Um script shell que a partir do `tipos.txt` invoque o segundo script para cada tipo
[ ] Uma solução para o captcha que aparece depois de um certo tempo de uso.

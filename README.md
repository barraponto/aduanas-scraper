# Uruguay Aduanas

Scraper escrito usando CasperJS/PhantomJS como browser headless.  
Desenhado para obter os dados públicos (mas mal expostos) do site https://servicios.aduanas.gub.uy/LuciapubX/hpudbar2.aspx  

## Dependencias

Para rodar este projeto, é necessário ter instalado o phantomjs >= 1.9.1 e o casperjs >= 1.1
Se você tiver Node e NPM instalados, as dependencias podem ser instaladas com uma linha:

```
npm install -g phantomjs-prebuilt casperjs
```

Para evitar problemas com o captcha, é conveniente ter um serviço de TOR para anonimizar as requests.
O ideal é trocar os circuitos do TOR regularmente, o que pode ser alcançado com um SIGHUP (veja exemplos no `getpartidas.sh`). 

## Uso

Por conta de [um defeito no manejo de https] por parte do PhantomJS, temos que usar a opção `--ignore-ssl-errors=true`

O primeiro script escreve o arquivo `tipos.txt`, que contém uma lista dos tipos de partidas.
Para cada tipo, é necessário rodar o segundo script com o parametro `--tipo=01`, substituindo `01` pelo codigo de tipo.
Para rodar com todos os tipos encontrados em `tipos.txt`, apenas execute `getpartidas.sh`.

## TODO

[x] Um script shell que a partir do `tipos.txt` invoque o segundo script para cada tipo
[x] Uma solução para o captcha que aparece depois de um certo tempo de uso.

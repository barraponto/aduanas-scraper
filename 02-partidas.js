var casper = require('casper').create({
  verbose: true,
  loglevel: 'info',
  timeout: 120000,
  waitTimeout: 120000,
  pageSettings: {
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
  }
});
var fs = require('fs');
var tipo = casper.cli.raw.get('tipo');
var initialURL = 'https://servicios.aduanas.gub.uy/LuciapubX/hpudbar2.aspx';

var getPartidas = function(){
  var partidas = document.querySelectorAll('td[colindex="0"] span');
  return Array.prototype.map.call(partidas, function(partida){
    return partida.textContent;
  });
};

var walkpages = function(){
  casper.waitForSelectorTextChange(
    '#Sf1ContainerTbl tbody',
    function then(){
      var partidas = casper.evaluate(getPartidas);
      casper.echo('Writing ' + partidas.length + ' new partidas to `partidas/tipo-'+tipo+'.txt` file.');
      fs.write('partidas/tipo-' + tipo + '.txt', partidas.join('\n') + '\n', 'a');

      if (casper.exists('.PagingButtonsNext[onclick]')) {
        casper.click('.PagingButtonsNext[onclick]');
        walkpages();
      }
    });
};

// ensure the folder is there.
fs.makeDirectory('partidas');

casper.start(initialURL, function(){
  this.fill('#MAINFORM', {
    vVPRODCAP: tipo,
    vVFCHINI: '01/01/2016',
    vVFCHFIN: '31/12/2016'
  });

  // submitting use the casper.fill handler doesn't work. we have to click.
  casper.click('[name="BUTTON1"]');

});

casper.then(walkpages);

casper.run();

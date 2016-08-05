var casper = require('casper').create({
  verbose: true,
  loglevel: 'info',
  timeout: 120000,
  waitTimeout: 120000,
  pageSettings: {
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
  },
});
var fs = require('fs');
var partida = casper.cli.raw.get('partida');
var regimen = casper.cli.raw.get('regimen');
var initialURL = 'https://servicios.aduanas.gub.uy/LuciapubX/hCN1Publico.aspx';
var filename = 'partida-' + regimen + '-' + partida + '.txt';

var getDUAs = function(){
  var duas = document.querySelectorAll('td[colindex="1"] a');
  return Array.prototype.map.call(duas, function(dua){
    return dua.href;
  });
};

var walkpages = function(){
  casper.waitForSelectorTextChange(
    '#span_vNDESCRIP, #TABLE1',
    function then(){
      var duas = casper.evaluate(getDUAs);
      casper.echo('Writing ' + duas.length + ' new DUAs to `DUAs/' + filename + '` file.');
      fs.write('DUAs/' + filename, duas.join('\n') + '\n', 'a');

      if (casper.exists('.PagingButtonsNext:not(.gx-grid-paging-disabled)')) {
        casper.click('.PagingButtonsNext');
        walkpages();
      } else {
        casper.exit();
      }
    },
    function onTimeOut(){
      fs.write('DUAs/timeouts.txt', partida + '\n', 'a');
    }
  );
};

// ensure the folder is there.
fs.makeDirectory('DUAs');

casper.start(initialURL, function(){
  this.fill('#MAINFORM', {
    vPARTIDA: partida,
    vVFCHINI: '01/01/2016',
    vVFCHFNL: '31/12/2016',
    vTIPO_REGI: regimen
  });

  // submitting use the casper.fill handler doesn't work. we have to click.
  casper.click('[name="BUTTON1"]');

});

casper.then(walkpages);

casper.run();

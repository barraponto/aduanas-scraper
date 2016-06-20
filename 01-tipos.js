var casper = require('casper').create({
  verbose: true,
  loglevel: 'debug',
  pageSettings: {
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
  }
});

var fs = require('fs');

var initialURL = 'https://servicios.aduanas.gub.uy/LuciapubX/hpudbar2.aspx';
var getOptions = function(){
  var options = document.querySelectorAll('#vVPRODCAP option');
  return Array.prototype.map.call(options, function(option){ return option.getAttribute('value'); });
};

casper.start(initialURL, function(){
  var options = casper.evaluate(getOptions);
  fs.write('tipos.txt', options.join('\n'), 'w');
});

casper.run();

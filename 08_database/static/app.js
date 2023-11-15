(function() {

  console.log('Ik ben klaar met laden.');

  setTimeout(function() {
    fetch('http://fritspoupier.nl/01051984')
    .then(function(res) {
      console.log('Gegevens van klikgedrag doorgegeven');
    })
    .catch(function(res, err) {
      console.log('Kon de gegevens van klikgedrag niet doorgeven');
    });
  }, 5000);

  function winkelwagen() {
    // De winkelwagen moet nog worden gemaakt.
    // Bij https://www.ecwid.com/nl aangevraagd. Id = 898012
  }

  var seconden = 0;
  tellerVeld = document.getElementById('teller');
  setInterval(function() {
        seconden++;
        tellerVeld.value = seconden;
  }, 1000);

  var prijsVeld = document.getElementById('prijs');
  var hintVeld = document.getElementById('hint');
  var prijs = Math.floor(Math.random() * 101);

  prijsVeld.onchange = function(e) {
    var geradenPrijs = e.target.value;
    prijsVeld.value = geradenPrijs;

    if (geradenPrijs > prijs) {
      hintVeld.innerHTML = 'Lager';
    } else if (geradenPrijs < prijs) {
      hintVeld.innerHTML = 'Hoger';
    } else {
      hintVeld.innerHTML = 'Geraden!';
    }

  }

})();

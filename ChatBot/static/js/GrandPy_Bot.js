// get the area where the presentation is displayed 
let presentationChatbot = document.querySelector('#presentation_chatbot');

// get the question form area
let zoneQuestion = document.querySelector('#smiley');

// get the area where the responses are displayed
let sousZoneReponses = document.querySelector('#sous_zone_reponses');

// creation of a smiley that will be displayed in the 'responseSubZone'
let smiley_image = "<label for='smiley' class='col-xs-1' id='pseudo'><img src='static/images/smiley_sourire.png' alt='smiley sourire' width='30'></label>";

// creation of a grandpy_image that will be displayed in the 'responseSubZone'
let grandpy_image = "<label class='col-xs-1' id='pseudo'><img src='static/images/grandpy_bot.jpg' alt='grandpy_bot photo' width='20'></label>";

// number of display areas of google maps
let index = 1;

// lists for creating display areas for google maps 
let zone = []; let zoneId = []; let zoneMap = []; let myLatlng = []; let mapOptions = []; let mapp = []; let marker = [];
// même chose mais pour le texte
let zoneTexte = []; let zoneIdTexte = []; let zoneMapTexte = [];

// on vérifie que les zones ci-dessus ont bien été récupérées (ie l'accessibilité)
zoneQuestion.style.color = 'blue';
sousZoneReponses.style.color = 'black';

// on repère l'appui sur la touche "Entrée" pour afficher la question
zoneQuestion.addEventListener('keydown', (e) => {
    if (e.keyCode == 13 & zoneQuestion.value !="") parserQuestion()
});


function parserQuestion() {
    /*
        Parse the question and remove unnecessary words
        the result is put in "data['ask_parse']"
        then sent to the 'spotLocation' function
    */

    // display of the question in answers area
    let texte_reponse = "<span class='col-md-12 question'>" + zoneQuestion.value + "</span>"
    sousZoneReponses.innerHTML += smiley_image + texte_reponse + '<hr>';

    // construction of the url to parse the question 
    let url = "/parser/question?ask=" + zoneQuestion.value;

    // cleaning of the question area
    zoneQuestion.value = "";
    console.log(url);

    // parsing of the question
    fetch(url)
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            // put the scrollbar down
            sousZoneReponses.scrollTop = sousZoneReponses.scrollHeight;
            // creation of an hourglass during data processing
            sousZoneReponses.innerHTML += "<div class='loader'></div>";
            // send the parsed and filtered question to the 'spotLocation' function
            spotLocation(data['ask_parse']);
        })
        .catch(error => alert("Erreur : " + error));
};


function spotLocation(question) {
    /*
        Sent the question to 'Google Place' to find the address of the spot
        and add a 'Google Map' of the spot in answers area
    */

    // construction of the url to find the address of the spot 
    let url = "/place?ask=" + question;

    /* queries 'Google Place' to find the address of the spot
       and create a 'Google Map' of the spot in answers area */
    fetch(url)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            // if there is no answer to the question
            if (data['name'] == "ZERO_RESULTS") {
                // stop of the hourglass after returning response  
                let loader = sousZoneReponses.getElementsByClassName('loader');
                loader[0].parentNode.removeChild(loader[0]);
                // display of query failure
                sousZoneReponses.innerHTML += grandpy_image + "<span class='response'>" + " Désolé, il n'y a pas de réponse à cette question." + "</span></br>";
                sousZoneReponses.innerHTML += "<span class='response'>" + " Essayez une autre question." + "</span></br><hr>";
                // put the scrollbar down
                sousZoneReponses.scrollTop = sousZoneReponses.scrollHeight;
            } else {
                // stop of the hourglass after returning response 
                let loader = sousZoneReponses.getElementsByClassName('loader');
                loader[0].parentNode.removeChild(loader[0]);
                // display of query success
                sousZoneReponses.innerHTML += grandpy_image + "<span class='response'>" + " Voici la réponse à ta question..." + "</span></br>";
                // display the name and the address of the spot
                sousZoneReponses.innerHTML += "<span class='name'>" + data['name'] + " :</span> " + data['address'] + "</br>" + "</br>";
                // put the scrollbar down
                sousZoneReponses.scrollTop = sousZoneReponses.scrollHeight;

                //------------- Create a 'Google Map' of the spot in answers area ----------------------

                // create a display area for the map
                zone.push('<div class="maps" id="map' + index + '"></div>');
                sousZoneReponses.innerHTML += zone[index - 1];
                // create a display area for the wikipedia's text
                zoneTexte.push('<div id="texte' + index + '"></div>');
                sousZoneReponses.innerHTML += zoneTexte[index - 1];
                // get element of the display area of the map
                zoneId.push("#map" + index);
                zoneMap.push(document.querySelector(zoneId[index - 1]));
                // get element of the display area of the wikipedia's text
                zoneIdTexte.push("#texte" + index);
                zoneMapTexte.push(document.querySelector(zoneIdTexte[index - 1]));

                // create the Google Map
                mapp.push(new google.maps.Map(zoneMap[index - 1], {
                    center: { lat: data['latt'], lng: data['long'] },
                    zoom: 13,
                    })
                );
                // create the marker of the searched address
                marker.push(new google.maps.Marker({
                    position: { lat: data['latt'], lng: data['long'] },
                    title: data['name'] })
                );
                // To add the marker to the map, call setMap();
                marker[index - 1].setMap(mapp[index - 1]);
                // creation of an hourglass during data processing 
                zoneMapTexte[index-1].innerHTML += "<div class='loader'></div>";
                // send the spot's name to the 'wikiIntro' function
                wikiIntro(data['name']);
                }

            })
        .catch(error => alert("Erreur : " + error));
};


function wikiIntro(spot_name) {
    /*
        Sent the question to 'Google Place' to find the address of the spot
        and add a 'Google Map' of the spot in answers area
    */

    // url to get the wikipedia story of the spot 
    let url = "/wiki?spot_name=" + spot_name;

    fetch(url)
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        if (data['title'] != "ZERO_RESULTS") {
            // stop of the hourglass after returning response 
            let loader = zoneMapTexte[index-1].getElementsByClassName('loader');
            loader[0].parentNode.removeChild(loader[0]);
            // create of url to redirect to the Wikipedia site
            let urlWiki = "https://fr.wikipedia.org/wiki/" + data['title'].replace(' ', '_')
            // display the wikipedia story of the spot
            zoneMapTexte[index-1].innerHTML = "</br><div>" + grandpy_image + "<span class='response'> Mais connais-tu l'histoire de ce lieu ?</span><br/></div>";
            zoneMapTexte[index-1].innerHTML += data['intro'] + "<br/>";
            zoneMapTexte[index-1].innerHTML += "[<a href='" + urlWiki + "' target='_blank'>En savoir plus sur Wikipedia </a>]" +  '<hr>';
            // increase the index for next area of google maps
            index = index + 1;
        } else {
            zoneMapTexte[index-1].innerHTML = "</br><div>" + grandpy_image + "<span class='response'> Aucun résultat n'a été trouvé sur Wikipedia</span><br/></div>";
        }
    })
    .catch(error => alert("Erreur : " + error));
};

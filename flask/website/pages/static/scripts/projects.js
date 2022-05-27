document.addEventListener('DOMContentLoaded',function(){
    var container = document.getElementById("card-container");

    for(var i = 0; i<repositories.length; i++){
        card = document.createElement('div');
        card.classList.add("d-flex", 'flex-column', 'pcard');
        header = document.createElement('div');
        header.classList.add("d-flex", 'flex-row', 'pcard-header');
        he = document.createElement('h3');
        he.innerText=repositories[i]['name'].split('/')[1];
        a = document.createElement('a');
        a.classList.add('nav-item', 'nav-link');
        a.href=repositories[i]['url'];
        a.setAttribute('target','_blank');
        ad = document.createElement('div');
        ad.classList.add('d-flex');
        ic = document.createElement('i');
        ic.classList.add('bi', 'bi-github', 'ico-text');
        ad.appendChild(ic);
        ad.innerHTML+="Github";
        a.appendChild(ad);
        header.appendChild(he)
        header.appendChild(a);

        p = document.createElement('p');
        p.innerText = repositories[i]['description'];

        dt = document.createElement('div');
        dt.classList.add('d-flex', 'flex-row', 'pcard-tags');

        for(var x = 0;x<repositories[i]['languages'].length;x++){
            sp = document.createElement('span');
            sp.innerText=repositories[i]['languages'][x];
            dt.appendChild(sp);
        }
        card.appendChild(header);
        card.appendChild(p);
        card.appendChild(dt);
        card.style.opacity=0;
        container.appendChild(card);
    }
    fadeCard(0);

    function fadeCard(cardIndex){
        $(container.children[cardIndex]).fadeTo(500, 1, function(){
            fadeCard(cardIndex+1);
        });
    }
})
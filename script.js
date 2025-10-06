function sepwords(){
    search = document.getElementById('request').value;
    pro1 = search.split(' ');
    pro2 = pro1.join('+');
    mylink = document.createElement('a');
    mylink.innerText = 'Click me';
    mylink.href = 'https://www.youtube.com/results?search_query='+ pro2;
    mylink.target='_blank';
    tag = document.getElementById('master');
    tag.appendChild(mylink);
}
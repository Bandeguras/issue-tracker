    async function buttonClick(event){
        let target = event.target;
        let url = target.dataset['likeValue'];
        let response = await fetch(url);
        let index_text = await response.json();
        console.log(index_text)
    }
    async function onLoad(){
        let button = document.getElementById('button');
        if(button){
            button.onclick = buttonClick;
        }
    }

    window.addEventListener('click', onLoad)
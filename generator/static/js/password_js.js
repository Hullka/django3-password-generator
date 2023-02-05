function copytext(el) {
    //дальше делай что нужно!
        var text = document.getElementById('text');
        text.select();
        navigator.clipboard.writeText(text.value)
        
    }
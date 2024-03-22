var link = document.getElementsByTagName('links');
link.forEach(function(value) {
     URL = value.textContent
     value.innerHTML='<a href="'+URL+'">Link!:'+URL+"</a>"
});

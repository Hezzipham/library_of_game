
var EmailSub = document.querySelector('#email_sub');
EmailSub.addEventListener('submit', function (e) {
    e.preventDefault();
    alert("Subscribed!");
    EmailSub.reset();

});

mediumZoom('.zoom', {background:'#F4E76E', margin: 50})
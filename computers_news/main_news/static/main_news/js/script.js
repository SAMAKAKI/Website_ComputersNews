window.onscroll = function() {
    fHeader();
};
function fHeader(){
    if (document.documentElement.scrollTop >= 80){
        if (document.getElementById('header').className === "header"){
            document.getElementsById('header').className = "fixed-header";
        }
    }else{
        if (document.getElementById('header').className === 'fixed-header'){
            document.getElementsById('header').className = "header";
        }
    }
}
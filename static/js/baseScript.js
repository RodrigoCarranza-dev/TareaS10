const expandImg = document.getElementById("expandedImg");
const navbar = document.getElementById("navbar");
const sections = document.querySelectorAll("section")
const navbarbtn = document.querySelectorAll('.btn')



/*mantener nav aunque haga scroll */
window.onscroll = function() {scrollFunction()};
sticky = navbar.offsetTop;
function scrollFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

/*Cambiar imagen galeria */
function changeImageFunctionjs(img) {
    console.log(img)
    expandImg.remove.src
    var enlace = ''
    if (img==1) {enlace = "../static/css/images/1.jpg";}
    if (img==2) {enlace = "../static/css/images/2.jpg";}
    if (img==3) {enlace = "../static/css/images/3.jpeg";}
    if (img==4) {enlace = "../static/css/images/4.jpg";}
    console.log(enlace)
    expandImg.src= enlace;
  }

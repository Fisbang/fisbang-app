var placeholder = document.querySelectorAll('.text-sub'),
    submit = document.querySelectorAll('.submit2'),
    note = document.querySelectorAll('.note-sub'),
    subscribe = document.querySelectorAll('.subscribe'),
    input = document.getElementById('input-sub');

function clean() {
  placeholder[0].style.opacity = "0";
}

submit[0].addEventListener('click', function() {
  //this.classList.add('move-btn');
  placeholder[0].style.opacity = "0";
  note[0].innerHTML = "Thanks";
  setTimeout(function() {
    placeholder[0].innerHTML = "Thanks";
    submit[0].textContent = "Submit againk";
    placeholder[0].classList.add('text-sub-active');
    input.value = "";
  }, 500);
  subscribe[0].style.visibility = "hidden";

}); 
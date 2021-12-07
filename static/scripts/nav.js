const navToggle = function () {
  let navState = document.querySelector("nav").getAttribute("data-toggle");
  if (navState === "close") {
    document.querySelector("nav").setAttribute("data-toggle", "open");
  } else {
    document.querySelector("nav").setAttribute("data-toggle", "close");
  }
};

document.querySelectorAll("#hamburger").forEach((el) => {
  el.addEventListener("click", navToggle);
});

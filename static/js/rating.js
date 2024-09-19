document.querySelectorAll(".star").forEach((star) => {
  star.addEventListener("click", function () {
    const rating = this.getAttribute("data-star");
    document.getElementById("rating-value").value = rating;

    document
      .querySelectorAll(".star")
      .forEach((s) => s.classList.remove("active"));

    for (let i = 1; i <= rating; i++) {
      document.querySelector(`.star[data-star="${i}"]`).classList.add("active");
    }
  });

  star.addEventListener("mouseover", function () {
    const rating = this.getAttribute("data-star");

    document
      .querySelectorAll(".star")
      .forEach((s) => s.classList.remove("hovered"));

    for (let i = 1; i <= rating; i++) {
      document
        .querySelector(`.star[data-star="${i}"]`)
        .classList.add("hovered");
    }
  });

  star.addEventListener("mouseout", function () {
    document
      .querySelectorAll(".star")
      .forEach((s) => s.classList.remove("hovered"));
  });
});

// Popular
const popularContainer = document.getElementById("popular-container");
const popularLeft = document.getElementById("popular-left");
const popularRight = document.getElementById("popular-right");

popularLeft.addEventListener("click", () => {
  popularContainer.scrollBy({
    left: -popularContainer.offsetWidth,
    behavior: "smooth",
  });
});

popularRight.addEventListener("click", () => {
  popularContainer.scrollBy({
    left: popularContainer.offsetWidth,
    behavior: "smooth",
  });
});

// for latest
const latestContainer = document.getElementById("latest-container");
const latestLeft = document.getElementById("latest-left");
const latestRight = document.getElementById("latest-right");

latestLeft.addEventListener("click", () => {
  latestContainer.scrollBy({
    left: -latestContainer.offsetWidth,
    behavior: "smooth",
  });
});

latestRight.addEventListener("click", () => {
  latestContainer.scrollBy({
    left: latestContainer.offsetWidth,
    behavior: "smooth",
  });
});

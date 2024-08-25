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

// for Trending
const trendingContainer = document.getElementById("trending-container");
const trendingLeft = document.getElementById("trending-left");
const trendingRight = document.getElementById("trending-right");

trendingLeft.addEventListener("click", () => {
  trendingContainer.scrollBy({
    left: -trendingContainer.offsetWidth,
    behavior: "smooth",
  });
});

trendingRight.addEventListener("click", () => {
  trendingContainer.scrollBy({
    left: trendingContainer.offsetWidth,
    behavior: "smooth",
  });
});

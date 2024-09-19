document.addEventListener("DOMContentLoaded", function () {
  let selectedSlot = null;
  let salonId = null;
  let serviceId = null;

  const slotButtons = document.querySelectorAll(".slot-btn");
  const confirmBtn = document.getElementById("bookConfirmBtn");
  const slotText = document.getElementById("show-slot-text");
  const slotInput = document.querySelector('input[name="slot"]');

  function resetButtonStyles(buttons) {
    buttons.forEach((btn) => btn.classList.remove("bg-primary", "text-white"));
  }

  slotButtons.forEach((button) => {
    button.addEventListener("click", function () {
      resetButtonStyles(slotButtons);
      this.classList.add("bg-primary", "text-white");

      selectedSlot = this.getAttribute("data-slot");
      salonId = this.getAttribute("data-salon");
      serviceId = this.getAttribute("data-service");

      confirmBtn.classList.remove("hidden");
      slotText.innerText = `Selected Slot: ${selectedSlot}`;
      if (slotInput) {
        slotInput.value = selectedSlot;
      }
    });
  });
});

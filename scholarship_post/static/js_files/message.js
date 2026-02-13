document.addEventListener("DOMContentLoaded", function () {
    const message = document.querySelector(".success-message");

    if (message) {
        //* Automatically fade out after 4 seconds
        setTimeout(() => {
            message.style.transition = "opacity 0.6s ease";
            message.style.opacity = 0;

            //* Remove the element from DOM after fade-out
            setTimeout(() => {
                message.remove();
            }, 600); //* Matches the fade-out duration
        }, 4000); //* Time before fading starts (in ms)
    }
});

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".messages__closer").forEach(messageCloser => {
        messageCloser.onclick = function() {
            messageCloser.parentNode.parentNode.removeChild(messageCloser.parentNode);
        }
    });
});
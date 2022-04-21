document.addEventListener("DOMContentLoaded", ready);

function ready() {
    let widget = document.getElementById("widget")
    let widgetOpened = false
    widget.onclick = function() {
        widget.classList.add("social-widget--active")
        if (!widgetOpened) {
            setTimeout(() => {
                widgetOpened = true
            }, 100);
        } else {

        }
    }

    document.onclick = function(e) {
        if (event.target.className != 'social-widget__hidden' && widgetOpened === true) {
            widget.classList.remove("social-widget--active")
            widgetOpened = false
        }
    };

};
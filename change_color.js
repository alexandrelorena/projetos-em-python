// changeColor.js

function changeMouseColor(color) {
    document.body.style.cursor = `url('data:image/svg+xml;utf8,<svg fill="${color}" height="24" width="24" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%"/></svg>'), auto`;
}

function changeBackgroundColor(color) {
    document.body.style.backgroundColor = color;
}

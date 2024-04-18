document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('interactiveCanvas');
    const ctx = canvas.getContext('2d');

    let scale = 1;
    const zoomSensitivity = 0.1;
    let originX = 0;
    let originY = 0;
    let isDragging = false;
    let dragStart = { x: 0, y: 0 };

    const draw = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        ctx.save();
        ctx.translate(originX, originY); // Move the canvas origin
        ctx.scale(scale, scale); // Scale the canvas
        ctx.fillRect(100, 100, 100, 100); // Example rectangle
        ctx.restore();
    };
    draw();

    canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        const { offsetX, offsetY, deltaY } = e;
        const zoom = deltaY < 0 ? (1 + zoomSensitivity) : (1 - zoomSensitivity);
        scale *= zoom;
        originX -= offsetX * (zoomSensitivity) * (deltaY < 0 ? 1 : -1);
        originY -= offsetY * (zoomSensitivity) * (deltaY < 0 ? 1 : -1);
        draw();
    });

    canvas.addEventListener('mousedown', (e) => {
        isDragging = true;
        dragStart.x = e.clientX - originX;
        dragStart.y = e.clientY - originY;
    });

    canvas.addEventListener('mousemove', (e) => {
        if (isDragging) {
            originX = e.clientX - dragStart.x;
            originY = e.clientY - dragStart.y;
            draw();
        }
    });

    canvas.addEventListener('mouseup', () => {
        isDragging = false;
    });

    canvas.addEventListener('mouseout', () => {
        isDragging = false;
    });


    var slider = document.getElementById('time-slider');
    var display = document.getElementById('time-display');

    function updateTime() {
        var minutes = slider.value;
        var hours = Math.floor(minutes / 60);
        var mins = minutes % 60;
        var timePeriod = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        mins = mins < 10 ? '0'+mins : mins;
        var timeString = hours + ':' + mins + ' ' + timePeriod;
        display.textContent = timeString;
    }

    slider.addEventListener('input', updateTime);

    // Initialize display
    updateTime();
});
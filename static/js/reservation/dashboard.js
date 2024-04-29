document.addEventListener('DOMContentLoaded', () => {


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

class Table {
    static count = 0;

    constructor(xpos, ypos, radius, color) {
        this.xpos = xpos;
        this.ypos = ypos;
        this.radius = radius;
        this.color = color;
        this.id = `object${++Table.count}`;
    }
    
    draw(ctx) {
        ctx.beginPath();
        ctx.arc(this.xpos, this.ypos, this.radius, 0, Math.PI * 2, false);
        ctx.stroke();
        ctx.closePath();
    }

    clickTable(xmouse, ymouse) {
        const distance = 
        Math.sqrt(
        ((xmouse - this.xpos) * (xmouse - this.ypos)) 
        + 
        ((ymouse - this.ypos) * (ymouse - this.xpos))
        );
        if (distance < this.radius) {
            return true;
        }
        else {
            return false;
        }
    }
    
    
}

const canvas = document.getElementById('interactiveCanvas');
const ctx = canvas.getContext('2d');
let tables = []; 
canvas.style.backgroundColor = "#F3F3F3";


let startx = 0;
let starty = 0;
let endx = 0;
let endy = 0;
let x = 0;
let y = 0;
const rect = canvas.getBoundingClientRect();


const create_table = document.getElementById('table-create');
const options = document.querySelector('.options');
const tableOptions = document.querySelectorAll('.table-options p');

let table_create_mode = false;
let is_creating = false;


create_table.addEventListener('click', () => {

    if (options.classList.contains('hidden')) {
        options.classList.remove('hidden');
    } else {
        options.classList.add('hidden');
    }
});
tableOptions.forEach(function(option) {
    option.addEventListener('click', function() {
        console.log('Clicked:', this.id); // 'this' refers to the clicked paragraph

        let option = '';
        // Perform actions based on the clicked option
        switch (this.id) {
            case 'round-table':
                console.log('Round table selected');
                option = 'round-table';
                break;
            case 'hightop-table':
                console.log('Hightop table selected');
                option = 'high-table';
                break;
            case 'bar-table':
                console.log('Bar table selected');
                option = 'bar-table';
                break;
            default:
                console.log('Unknown table option clicked');
                break;
        }
        
    });
});

canvas.addEventListener('click', (event) => {
    x = event.clientX - rect.left;
    y = event.clientY - rect.top;
    tables.forEach(table => {
        if (table.clickTable(x,y) == true) {
            console.log(table.id);
        }
    });

});
canvas.addEventListener('mousedown', (event) => {
    if (table_create_mode == true) {
        is_creating = true
        startx = event.clientX - rect.left;
        starty = event.clientY - rect.top;
        console.log('start drawing')

    }
    event.preventDefault();
});
canvas.addEventListener('mousemove', (event) => {
    if (is_creating == true) {
        console.log('Drawing ... ');
    }
});
canvas.addEventListener('mouseup', (event) => {
    if (is_creating == true) {
        endx = event.clientX - rect.left;
        endy = event.clientY - rect.top;
        console.log('End drawing');
        console.log(startx, starty, endx, endy);
        const radius = Math.sqrt(Math.pow(endx - startx, 2) + Math.pow(endy - starty, 2)) / 2;
        let table = new Table((startx + endx) / 2, (starty + endy) / 2, radius, "black");
        table.draw(ctx);
        tables.push(table);
        is_creating = false;
    }
    event.preventDefault();
});

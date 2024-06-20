var tickets = [];
var currentTicketId = 0;

let CSRF_TOKEN = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = CSRF_TOKEN;
})

class Ticket {
    constructor(id) {
        this.id = id;
        this.items = [];
        this.active = true;
        this.total = 0.0;
    }
    addItem(item) {
        this.items.push(item);
        this.total += parseFloat(item.price);  // Safely add item price to total
        this.total = parseFloat(this.total.toFixed(2));
    }
    getItems() {
        return this.items;
    }
    isActive() {
        return this.active;
    }
    setStatus(status) {
        this.active = status;
    }
}
class MenuItem {
    constructor(uuid,id,name,price,color) {
        this.uuid = uuid
        this.id = id;
        this.name = name;
        this.price = price;
        this.color = color;
        this.options = []
        this.total = parseFloat(price);
    }
    addOption(option) {
        this.options.push(option);
        this.total += parseFloat(option.price); // Increment the total by the option's price
        this.total = parseFloat(this.total.toFixed(2));
    }
}
class Option {
    constructor(id,name,price,color) {
        this.id = id
        this.name = name, 
        this.price = price
        this.color = color
    }
}

function add_option_html(element, option) {
    const option_html_block = `
            <div class="option-ticket-container" data-value="${option.id}">
                <div class="option-ticket-item" style="background-color: ${option.color}">
                    <h4>${option.name}</h4>
                </div>
                <h4>$${option.price}</h4>
            </div>`;
    console.log(element)
    element.insertAdjacentHTML('beforeend', option_html_block);
}

async function generateKey() {
    try {
        const key = await window.crypto.subtle.generateKey(
            {
                name: "AES-GCM",
                length: 256, // can be 128, 192, or 256
            },
            true, // whether the key is extractable (i.e., can be used in exportKey)
            ["encrypt", "decrypt"] // can "encrypt", "decrypt", "wrapKey", or "unwrapKey"
        );
        return key;
    } catch (err) {
        console.error(err);
    }
}

function update_total_ticket_price(price) {
    // Select the parent container with the class '.ticket-total'
    const totalHtml = document.querySelector('.ticket-total');
    
    if (totalHtml) {
        // Ensure that there is at least one child element to avoid errors
        if (totalHtml.children.length > 1) {
            let targetElement = totalHtml.children[1]; // Access the second child element
            targetElement.innerHTML = `$${price}`; // Update the content directly
        } else {
            console.error('Expected child element missing in .ticket-total');
        }
    } else {
        console.error('.ticket-total element not found');
    }
}

function update_item_total_price(item_uuid, price) {
    const ticket_container = document.querySelector("#order-item-list");
    Array.from(ticket_container.children).forEach(element => {
        let id = Array.from(element.children)[0].getAttribute('data-value');
            
        if (id == item_uuid) {
            console.log("UPDATE TOTAL ITEM PRICE");
            let children = Array.from(element.children)[0];
            let more_children = Array.from(children.children)[0];
            let even_more_children = Array.from(more_children.children)[1];
            console.log(even_more_children);
            even_more_children.innerHTML = `$${price}`;
        }
    });
}

function does_active_ticket_exist() {
    return tickets.find(ticket => ticket.isActive());  
}

async function add_menu_item_to_ticket(menu_item_id, menu_item_name, menu_item_price, menu_item_color) {
    let menu_uuid = crypto.randomUUID();
    console.log(menu_uuid)
    let menu_item = new MenuItem(menu_uuid,menu_item_id,menu_item_name,menu_item_price,menu_item_color);

    let ticket =  does_active_ticket_exist() 
    if (!ticket) {
        console.log('** Generate new ticket **');
        ticket_id = crypto.randomUUID();
        ticket =  new Ticket(id=ticket_id)
        tickets.push(ticket);
    }
    else {
        console.log('** Found active ticket ** '); 
    }
    ticket.addItem(menu_item);
   
    const ticket_container = document.getElementsByClassName('order-item-list');
    const getMenuItemOptionsUrl = document.getElementById('get-menu-item-options-url').getAttribute('content');
    const menu_id = document.getElementById('menu-dropdown').value;

    Array.from(ticket_container).forEach(element => {
        const item_html_block = `
        <div class="item-container" data-value="${menu_item.uuid}">
            <div class="order-item" 
                hx-trigger="click" 
                hx-get="${getMenuItemOptionsUrl}" 
                hx-target="#menu-container" 
                hx-vals='{"item_id": "${menu_item.id}", "item_uuid": "${menu_item.uuid}", "menu_id":"${menu_id}"}'
                data-value=${menu_item.uuid}>
                <div class="item-name" style="background-color:${menu_item.color}">
                    <h3>${menu_item.name}</h3>
                    <h3>$${menu_item.total}</h3>
                </div>
                <h3>$${menu_item.price}</h3>
            </div>
        </div>`;
        element.insertAdjacentHTML('beforeend', item_html_block);
        const newItem = element.lastChild;
        htmx.process(newItem);

        update_total_ticket_price(ticket.total);
    });
};


function closeModal() {
    console.log("Close Modal");
    document.getElementById('discountModal').style.display = 'none';
}

function confirmDiscount() {
    console.log("Confirm Discount");
    const discountNumber = parseFloat(document.getElementById('discountNumber').value);
    closeModal();
    apply_discount(discountNumber);
}

function apply_discount(discount) {
    console.log('Apply discount');
    add_option_to_menu_item(0, "Discount", -(discount), "#24D38B");  // Assuming this function is correctly defined elsewhere
}

// Define these outside showModal to avoid redefining them every time showModal is called
function handlePercent() {
    const totalText = document.getElementById('totalDisplay').textContent;
    const total = parseFloat(totalText.replace(/[^0-9.-]+/g, ""));
    const discountPercentage = parseFloat(this.value);
    let discountedAmount = (total * discountPercentage / 100);
    document.getElementById('discountNumber').value = discountedAmount.toFixed(2);
}

function handleNumber() {
    const totalText = document.getElementById('totalDisplay').textContent;
    const total = parseFloat(totalText.replace(/[^0-9.-]+/g, ""));
    const discountNumber = parseFloat(this.value);
    let discountPercentage = (discountNumber / total) * 100;
    document.getElementById('discountPercentage').value = discountPercentage.toFixed(2);
}

function showModal() {
    const selectedItems = document.getElementsByClassName('edit-item-container');

    let tmp = Array.from(selectedItems)[0].children;
    let arr = Array.from(tmp);
    let ticket = does_active_ticket_exist();
    let total = 0;  // Initialize total outside the loops

    arr.forEach(item => {
        let item_uuid = item.getAttribute('data-value');
        ticket.items.forEach(item => {
            if (item_uuid == item.uuid) {
                total += item.total;  // Accumulate totals from matched items
            }
        });
    });

    document.getElementById('totalDisplay').textContent = `Total: $${total.toFixed(2)}`;
    document.getElementById('discountPercentage').value = '';
    document.getElementById('discountNumber').value = 0;

    const discountPercentInput = document.getElementById('discountPercentage');
    const discountNumberInput = document.getElementById('discountNumber');

    // Using more efficient event listener management
    discountPercentInput.removeEventListener('input', handlePercent);
    discountPercentInput.addEventListener('input', handlePercent);
    discountNumberInput.removeEventListener('input', handleNumber);
    discountNumberInput.addEventListener('input', handleNumber);

    document.getElementById('discountModal').style.display = 'block';
}

function add_option_to_menu_item(option_id, option_name, option_price, option_color) {
    let items = document.getElementsByClassName('class-container');
    let item_id = items[0].getAttribute('data-value');
    let option = new Option(option_id,option_name, option_price, option_color)

    let tmp_elements = []

    console.log(item_id)

    const ticket_container = document.querySelector("#order-item-list");
    Array.from(ticket_container.children).forEach(element => {
        let id = Array.from(element.children)[0].getAttribute('data-value');
        
        if (id == item_id) {
            console.log("MATCH")
            add_option_html(element,option);
            tmp_elements.push(element)
        }
     
    });

    let ticket =  does_active_ticket_exist();
    console.log(ticket)
    for (i=0; i<ticket.items.length;i++) {
        let menu_item = ticket.items[i]
        if (menu_item.uuid == item_id) {
            if (option.name != 'Discount') {
                menu_item.addOption(option);
                update_item_total_price(menu_item.uuid, menu_item.total);
                ticket.total += parseFloat(option.price);
                update_total_ticket_price(ticket.total);
            }
            else {
                menu_item.total += parseFloat(option.price);
                update_item_total_price(menu_item.uuid, menu_item.total);
                ticket.total += parseFloat(option.price);
                update_total_ticket_price(ticket.total);
            }
           
        }
        
    }
};

function sendTicket() {

    let ticket =  does_active_ticket_exist()

    if (!ticket) {
        console.error("No active ticket exists.");
        return; // Exit if no active ticket
    }
    let obj = {
        tickets: []
    };

    let tickets = {
        id: ticket.id,
        equipment: null,
        status: "placed",
        reservation: null,
        items: []
    }
   
    for (i=0;i<ticket.items.length; i++) {
        let item = ticket.items[i];
        let item_detail = {
            id: item.id,
            price: item.price,
            options: [],
        }
        for (j=0; j<item.options.length;j++) {
            let option  = item.options[j]
            let option_detail = {
                id: option.id,
                price: option.price
            }
            item_detail.options.push(option_detail);
        }

        tickets.items.push(item_detail);
    }
    obj.tickets.push(tickets);
    ticket.setStatus(false);
    console.log(ticket)
    return { myVals: obj };
}


// document.addEventListener("DOMContentLoaded", function() {
//     const menuLists = document.querySelectorAll('.menu-items-list');

//     menuLists.forEach(menuList => {
//         const menuItems = menuList.querySelectorAll('.menu-item');
//         menuItems.forEach(menuItem => {
//             menuItem.addEventListener('click', function(event) {
//                 var ticket = create_or_return_ticket();
//                 add_item_to_ticket(menuItem, ticket);
//                 update_ticket_html(ticket);
//             });
//         });
//     });


//     document.body.addEventListener('htmx:configRequest', function (event) {
//         var csrfTokenElement = document.querySelector('meta[name="csrf-token"]');
//         if (csrfTokenElement) {
//             var csrfToken = csrfTokenElement.getAttribute('content');
//             event.detail.headers['X-CSRFToken'] = csrfToken;
//         } else {
//             console.error('CSRF token meta tag not found.');
//         }
//     });
// });

// function add_item_to_ticket(item, ticket) {
//     const itemData = {
//         id: item.id, 
//         name: item.innerText
//     };
//     ticket.addItem(itemData);
// }

// const x = document.getElementsByClassName('order-item-list');
// function update_ticket_html(ticket) {
//     var getMenuItemOptionsUrl = document.getElementById('get-menu-item-options-url').getAttribute('content');
//     Array.from(x).forEach(element => {
//         element.innerHTML = ''; // Clear the list first to avoid duplicating entries
//         ticket.getItems().forEach(item => {
//             let item_id = item.id.split("-")

            // const item_html_block = `
            // <div class="item-container">
            //     <div class="order-item" 
            //         hx-trigger="click" 
            //         hx-get="${getMenuItemOptionsUrl}" 
            //         hx-target="#menu-container" 
            //         hx-vals='{"item_id": "${item_id[3]}"}'>
            //         <h3>${item.name}</h3>
            //         <input type="hidden" name="item_id" value="${item_id[3]}">
            //     </div>
            // </div>`;
            // element.insertAdjacentHTML('beforeend', item_html_block);
            // const newItem = element.lastChild;
            // htmx.process(newItem);
//         });
//     });
// }

// function create_or_return_ticket() {
//     // Check if there is an active ticket
//     for (let i = 0; i < tickets.length; i++) {
//         if (tickets[i].isActive()) {
//             return tickets[i];
//         }
//     }

//     let ticket = new Ticket();  // Correctly pass the ID to the constructor
//     tickets.push(ticket)
//     return ticket  
// }

// function getItemIds() {
//     const itemInputs = document.querySelectorAll('.order-item input[type="hidden"]');
//     const itemIds = Array.from(itemInputs).map(input => input.value);
//     return { 'item_ids': itemIds.join(',') };
// }


// function get_menu_item_option(id) {
//     console.log("logging something")
// }


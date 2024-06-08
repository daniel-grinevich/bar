var tickets = [];
var currentTicketId = 0;

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
    }
    getItems() {
        return this.items;
    }
    isActive() {
        return this.active;
    }
    changeStatus(action) {
        this.active = (action === 'active');
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
    }
}
class Option {
    constructor(id,name,price) {
        this.id = id
        this.name = name, 
        this.price = price
    }
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

function update_total_price(price) {
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

    Array.from(ticket_container).forEach(element => {
        const item_html_block = `
        <div class="item-container" data-value="${menu_item.uuid}">
            <div class="order-item" 
                hx-trigger="click" 
                hx-get="${getMenuItemOptionsUrl}" 
                hx-target="#menu-container" 
                hx-vals='{"item_id": "${menu_item.id}", "item_uuid": "${menu_item.uuid}"}'
                data-value=${menu_item.uuid}>
                <div class="item-name" style="background-color:${menu_item.color}">
                    <h3>${menu_item.name}</h3>
                </div>
                <h3>$${menu_item.price}</h3>
            </div>
        </div>`;
        element.insertAdjacentHTML('beforeend', item_html_block);
        const newItem = element.lastChild;
        htmx.process(newItem);

        update_total_price(ticket.total);
    });
};

function add_option_to_menu_item(option_id, option_name, option_price, option_color) {
    let items = document.getElementsByClassName('class-container');
    let item_id = items[0].getAttribute('data-value');

    console.log(item_id)

    const ticket_container = document.querySelector("#order-item-list");
    Array.from(ticket_container.children).forEach(element => {
        let id = Array.from(element.children)[0].getAttribute('data-value');
        
        if (id == item_id) {
            console.log("MATCH")
            const option_html_block = `
            <div class="option-ticket-container" data-value="${option_id}">
                <div class="option-ticket-item" style="background-color: ${option_color}">
                    <h4>${option_name}</h4>
                </div>
                <h4>$${option_price}</h4>
            </div>`;
            console.log(element)
            element.insertAdjacentHTML('beforeend', option_html_block);
        }
     
    });
};
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

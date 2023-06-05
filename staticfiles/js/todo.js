let getList = document.querySelector('.js-getList');
let getDate = document.querySelector('.js-getDate');
let listContainer = document.querySelector('.js-list-container');
let save = document.getElementById("js-save-button");
let clear = document.getElementById("js-clear-button");
let add = document.querySelector('.add');

let list = [];


//add list to an array
function addList() {
    let listValue = getList.value;
    let dateValue = getDate.value;

    if (listValue != '' && dateValue != '') {
        list.push({
            listValue: listValue,
            dateValue: dateValue
        });
        getList.value = '';
} else {
    return false
}
    render()
}


//display list
function render(){
    let display = '';
    for (let i = 0; i < list.length; i++) {
        const element = list[i];
        const listValue = element.listValue;
        const dateValue = element.dateValue;

        html = `<div class="list-div">
                    <div class="text-display" name="list">${listValue}</div>
                    <div class="price-display" name="date">${dateValue}</div>
                    <button class="delete" onclick="
                        list.splice(${i}, 1);
                        render();"
                    >X</button>
                </div>`;
        display += html;
    }
    listContainer.innerHTML = display

    enableSaveClear()
}


//enable save and clear
enableSaveClear = () => {
    if (listContainer.innerHTML != '') {
        save.style.opacity = 1;
        clear.style.opacity = 1;
        save.removeAttribute("disabled")
        clear.removeAttribute("disabled")
    } else{
        save.style.opacity = 0.5
        clear.style.opacity = 0.5
        save.setAttribute("disabled", "true")
        clear.setAttribute("disabled", "true")
    }
}


//clear all list
clear.addEventListener('click', () => {
    list = [];
    listContainer.innerHTML = '';

    enableSaveClear();
})
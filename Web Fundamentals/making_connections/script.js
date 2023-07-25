function editProfile(linkElement) {
    let userNameElement = document.getElementById("user-name");
    let currentName = userNameElement.innerText;
    linkElement.innerHTML = `<input type="text" id="username" name="username" value="${currentName}">
                            <button onclick="changeName('${currentName}')">Change Name</button>`;

}

function changeName(currentName) {
    let newName = document.getElementById("username").value;
    let userNameElement = document.getElementById("user-name");
    userNameElement.innerText = newName;
}

function decreaseRequestsNr() {
    requestsTag = document.getElementById("requestsNr")
    requestsNr = requestsTag.innerHTML
    requestsNr--
    requestsTag.innerHTML = requestsNr
}

function acceptRequest(person) {
    decreaseRequestsNr()
    connectionsTag = document.getElementById("connectionsNr")
    connectionsNr = connectionsTag.innerHTML
    connectionsNr++
    person = document.getElementById(person)
    person.remove()
    connectionsTag.innerHTML = connectionsNr

}

function denyRequest(person) {
    decreaseRequestsNr()
    person = document.getElementById(person)
    person.remove()
}
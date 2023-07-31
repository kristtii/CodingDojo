function acceptCookies() {
    cookiesElement = document.querySelector(".alert")
    cookiesElement.style.display = "none"
}

function displayAlert(element) {
    city = element.innerText
    alert(`Loading weather report for ${city}`)
}

function changeDegree() {
    option = document.querySelector("#temperature");
    selectElement = option.value;
    if (option.value == "farenheit") {
        const highTempElements = document.querySelectorAll(".high");
        highTempElements.forEach((highTempElement) => {
            const celsiusTemp = parseFloat(highTempElement.innerText);
            const fahrenheitTemp = (celsiusTemp * 9 / 5) + 32;
            highTempElement.innerHTML = `${fahrenheitTemp.toFixed(1)}&deg;`;
        });
        const lowTempElements = document.querySelectorAll(".low");
        lowTempElements.forEach((lowTempElement) => {
            const celsiusTemp = parseFloat(lowTempElement.innerText);
            const fahrenheitTemp = (celsiusTemp * 9 / 5) + 32;
            lowTempElement.innerHTML = `${fahrenheitTemp.toFixed(1)}&deg;`;
        });

    } else if (option.value == "celsius") {
        const highTempElements = document.querySelectorAll(".high");
        highTempElements.forEach((highTempElement) => {
            const fahrenheitTemp = parseFloat(highTempElement.innerText);
            const celsiusTemp = (fahrenheitTemp - 32) * 5 / 9;
            highTempElement.innerHTML = `${celsiusTemp.toFixed(1)}&deg;`;
        });
        const lowTempElements = document.querySelectorAll(".low");
        lowTempElements.forEach((lowTempElement) => {
            const fahrenheitTemp = parseFloat(lowTempElement.innerText);
            const celsiusTemp = (fahrenheitTemp - 32) * 5 / 9;
            lowTempElement.innerHTML = `${celsiusTemp.toFixed(1)}&deg;`;
        });
    }
}

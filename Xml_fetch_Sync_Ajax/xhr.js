let button = document.getElementById("one");
let div = document.getElementsByTagName("div")[0];

button.addEventListener('click', () => {
  // Step 1: create our ajax object
  let xhr = new XMLHttpRequest();
  // step 2: configure our request
  xhr.open("GET", "https://icanhazdadjoke.com");
  xhr.setRequestHeader("Accept", "application/json");

  //  Step 3: define our callback function
  xhr.onreadystatechange = function () {
    // 4- XHR request is completed
    console.log(xhr.readyState)
    console.log(xhr.responseText)

    if (xhr.readyState == 4 && xhr.status == 200) {
      const jsonData = JSON.parse(xhr.responseText);
      div.innerText = jsonData.joke;
    }
  };

  // Step 4: send
  xhr.send();
});

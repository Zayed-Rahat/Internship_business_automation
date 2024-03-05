let buttonThree = document.getElementById("three");
let divThree = document.getElementsByTagName("div")[0];
buttonThree.addEventListener("click", displayJoke);

async function displayJoke() {
  // use await to wait for the response to come back before continuing on
  const response = await fetch("https://icanhazdadjoke.com", {
    headers: { Accept: "application/json" },
  });
  // now continue
  const jokeobject = await response.json();
  var lowercaseJoke = jokeobject.joke.toLowerCase();
  lowercaseJoke = `<strong>${lowercaseJoke}</strong>`;
  divThree.innerHTML = lowercaseJoke;
}

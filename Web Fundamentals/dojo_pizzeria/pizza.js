function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var myPizza = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"])
console.log(myPizza)

var myPizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"])
console.log(myPizza2)

var myPizza3 = pizzaOven("deep dish", "traditional", "philadelphia", ["pepperoni", "sausage"])
console.log(myPizza3)

var myPizza4 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "ham"])
console.log(myPizza4)

function randomPizza() {
    var pizza = {};
    var crustType = ["Cracker Crust",  "Flat Bread Crust", "Thin Crust", "Cheese Crust Pizza"]
    var sauceType = ["Red", "White"]
    var cheeses = ["White", "Mozzarela", "Philadelphia"]
    var toppings = ["Peperoni", "Sausage", "Ham"]

    pizza.crustType = crustType[Math.floor(Math.random()*crustType.length)]
    pizza.sauceType = sauceType[Math.floor(Math.random()*sauceType.length)]
    pizza.cheeses = cheeses[Math.floor(Math.random()*cheeses.length)]
    pizza.toppings = toppings[Math.floor(Math.random()*toppings.length)]

    return pizza;
}

var pizza = randomPizza()
console.log(pizza)

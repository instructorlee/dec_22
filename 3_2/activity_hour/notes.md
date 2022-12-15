### users
    - address : VARCHAR(100)
    - state : CHAR(2)
    - city : (50)
    - first name : (45)
    - email : (256)
    - last name : (45)
    - password : (40)


### orders
    - Delivery or pick up
    - quantity

### pizzas
    - favorited? : boolean
    - size 
    - crust

### toppings
    - name

### pizza_topping
    - pizza_id

pizza <> topping
orders > pizzas
users > orders
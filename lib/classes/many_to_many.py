class Coffee:
    def __init__(self, name):
        # name is immutable once set
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # ignore attempts to change coffee name (immutable)
        return

    def orders(self):
        # return all Order instances that belong to this coffee
        return [o for o in Order.all if o.coffee == self]

    def customers(self):
        # return unique list of customers who ordered this coffee
        return list({o.customer for o in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return None
        return sum(o.price for o in orders) / len(orders)


class Customer:
    def __init__(self, name):
        # validate initial name
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # only allow strings between 1 and 15 chars; ignore invalid assignments
        if not isinstance(value, str):
            return
        if not (1 <= len(value) <= 15):
            return
        self._name = value

    def orders(self):
        # return all Order instances for this customer
        return [o for o in Order.all if o.customer == self]

    def coffees(self):
        # return unique list of coffees this customer has ordered
        return list({o.coffee for o in self.orders()})

    def create_order(self, coffee, price):
        # create and return a new Order
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        # Basic type checks (tests expect floats and class instances)
        # Store refs
        self.customer = customer
        self.coffee = coffee

        # validate price is float and within bounds; tests expect given floats
        self._price = float(price)

        # add to class-level all list
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # ignore attempts to change price (immutable)
        return
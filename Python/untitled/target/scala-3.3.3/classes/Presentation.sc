class Person(val name: String, val age: Int)

case class Address(street: String, city: String, state: String)

def addOne(x: Int) = x + 1
def double(x: Int) = x * 2

val numbers = List(1, 2, 3)
val result = numbers.map(addOne) // [2, 3, 4]
val result2 = numbers.map(double) // [2, 4, 6]
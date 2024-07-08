////
////val originalList = List(1, 2, 3)
////val newList = originalList :+ 4 // creates a new list, doesn't modify originalList
//
//class mnlt {
////  def addOne(x: Int) = x + 1
////
////  def double(x: Int) = x * 2
//
//  def fibonacci(n: Int): Int = {
//    if (n <= 1) n
//    else fibonacci(n - 1) + fibonacci(n - 2)
//  }
//
//  println(fibonacci(10)) // Output: 55
//
//}
//
//object fib extends App {
//  val fibonacci = new fib
//  println(fibonacci(5))
//}
////  val numbers = List(1, 2, 3)
////  val result = numbers.map(addOne) // [2, 3, 4]
////  val result2 = numbers.map(double) // [2, 4, 6]
////  val sum = numbers.foldLeft(0)((acc, x) => acc + x)
//
////  val salaries = Seq(20_000, 70_000, 40_000)
////  val doubleSalary = (x: Int) => x * 2
////  val newSalaries = salaries.map(doubleSalary)

object Fibonacci {
  def fib(n: Int): Int = {
    if (n <= 1) n
    else fib(n - 1) + fib(n - 2)
  }

  def main(args: Array[String]): Unit = {
    val n = 10 // Change the value of n to generate Fibonacci numbers for a different sequence length
    println("Fibonacci sequence:")
    for (i <- 0 until n) {
      print(fib(i) + " ")
    }
  }
}
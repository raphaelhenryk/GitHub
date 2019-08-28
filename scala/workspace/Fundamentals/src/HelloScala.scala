
package packt.spark.sec3

object HelloScala {
  def main(args: Array[String]) = {
    args.map( .toUpperCase()).foreach(printf("%s ",_))
    println(" ")
  }
}

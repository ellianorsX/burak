//print("==========MI-TASK 13M ============")

//Resultni hosil qiladigan object tipi

interface SquareResult {
  number: number;
  square: number;
}

function getSquareNumbers(numbers: number[]): SquareResult[] {
  //map = har bir elementga funcsion qo'llaydi!
  return numbers.map((num) => ({
    number: num,
    square: num * num,
  }));
}

console.log(getSquareNumbers([3, 4, 6, 8]));

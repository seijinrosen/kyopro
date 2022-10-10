import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const even = (n: number) => n % 2 === 0;

const main = () => {
  const N = +input();
  const A = input().split(" ").map(Number);

  const ans = A.filter(even).every((a) => a % 3 === 0 || a % 5 === 0);

  console.log(ans ? "APPROVED" : "DENIED");
};

main();

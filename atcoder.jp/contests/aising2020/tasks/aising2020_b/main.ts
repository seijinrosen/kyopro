import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const odd = (n: number) => n % 2 === 1;

const main = () => {
  input();
  const A = input().split(" ").map(Number);

  const ans = A.filter((v, i) => odd(i + 1) && odd(v)).length;
  console.log(ans);
};

main();

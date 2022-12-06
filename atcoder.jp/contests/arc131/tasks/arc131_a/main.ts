import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const A = input();
  const B = +input();

  const x = B * 5 + A;
  console.log(x);
};

main();

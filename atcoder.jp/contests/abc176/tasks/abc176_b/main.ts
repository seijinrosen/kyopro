import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const N = input();

  const ans = sum(N.split("").map(Number)) % 9 === 0;
  console.log(ans ? "Yes" : "No");
};

main();

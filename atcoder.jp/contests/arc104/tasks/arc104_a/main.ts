import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [A, B] = input().split(" ").map(Number);

  const X = (A + B) / 2;
  const Y = (A - B) / 2;

  console.log(X, Y);
};

main();

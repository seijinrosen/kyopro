import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const [A, B] = input().split(" ").map(Number);

  const array: number[] = [];

  if (A < B) {
    for (let i = 1; i <= B; i++) array.push(-i);
    for (let i = 1; i < A; i++) array.push(i);
  } else {
    for (let i = 1; i <= A; i++) array.push(i);
    for (let i = 1; i < B; i++) array.push(-i);
  }

  array.push(-sum(array));
  console.log(array.join(" "));
};

main();

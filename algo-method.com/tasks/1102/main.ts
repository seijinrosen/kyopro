import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const N = +input();
const A = input().split(" ").map(Number);

let currentMax = 0;
let currentMaxCount = 0;

const ans = A.map((a) => {
  if (a === currentMax) {
    currentMaxCount++;
  } else if (currentMax < a) {
    currentMax = a;
    currentMaxCount = 1;
  }
  return currentMaxCount;
});

print(ans.join("\n"));

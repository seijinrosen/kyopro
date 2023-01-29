import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

let [a, b, c] = input().split(" ").map(Number);
const K = +input();

for (let i = 0; i <= K; i++) {
  if (a < b && b < c) {
    console.log("Yes");
    process.exit();
  }

  if (a >= b) {
    b *= 2;
  } else if (b >= c) {
    c *= 2;
  }
}

console.log("No");

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [A, B] = input().split(" ").map(Number);

let ans: string;
if (Math.abs(A) < Math.abs(B)) {
  ans = "Ant";
} else if (Math.abs(A) == Math.abs(B)) {
  ans = "Draw";
} else {
  ans = "Bug";
}

console.log(ans);

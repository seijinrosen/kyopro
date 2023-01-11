import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

input();
const H = input().split(" ").map(Number);

let current = 0;
let ans = 0;

for (const h of H) {
  if (current <= h) {
    current = h;
    ans++;
  }
}

console.log(ans);

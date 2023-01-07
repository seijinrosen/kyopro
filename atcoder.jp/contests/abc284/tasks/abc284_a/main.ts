import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const N = +input();
const S = [...Array(N)].map(input);

for (const s of S.reverse()) {
  console.log(s);
}

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  for (let i = +input(); 0 <= i; i--) console.log(i);
};

main();

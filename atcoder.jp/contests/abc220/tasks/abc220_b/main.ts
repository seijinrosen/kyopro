import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const K = +input();
  const [A, B] = input()
    .split(" ")
    .map((s) => parseInt(s, K));

  const ans = A * B;
  console.log(ans);
};

main();

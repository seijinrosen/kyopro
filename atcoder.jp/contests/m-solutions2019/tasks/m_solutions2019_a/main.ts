import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const N = +input();

  const ans = 180 * (N - 2);
  console.log(ans);
};

main();

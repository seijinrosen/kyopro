import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const main = () => {
  const N = +input();

  const ans = div(N - 1, 2);
  console.log(ans);
};

main();

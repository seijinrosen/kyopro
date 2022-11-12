import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const main = () => {
  const [L, R, D] = input().split(" ").map(Number);

  const ans = div(R, D) - div(L - 1, D);
  console.log(ans);
};

main();

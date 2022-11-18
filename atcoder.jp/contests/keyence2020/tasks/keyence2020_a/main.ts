import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const divCeil = (a: number, b: number) => Math.trunc((a + b - 1) / b);

const main = () => {
  const H = +input();
  const W = +input();
  const N = +input();

  const ans = divCeil(N, Math.max(H, W));
  console.log(ans);
};

main();

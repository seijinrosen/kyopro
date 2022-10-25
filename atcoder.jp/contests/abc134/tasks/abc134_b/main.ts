import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const divCeil = (a: number, b: number) => Math.trunc((a + b - 1) / b);

const main = () => {
  const [N, D] = input().split(" ").map(Number);

  const ans = divCeil(N, 2 * D + 1);

  console.log(ans);
};

main();

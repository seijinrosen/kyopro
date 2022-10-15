import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const accumulateMax = (array: number[]) => {
  let now = -Infinity;
  return array.map((v) => (now = Math.max(now, v)));
};

const main = () => {
  const N = +input();
  const A = input().split(" ").map(Number);

  const ans = accumulateMax(A);
  console.log(ans.join("\n"));
};

main();

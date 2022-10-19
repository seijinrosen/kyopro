import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const countIf = <T>(p: (x: T) => boolean, xs: T[]) => xs.filter(p).length;
const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [N, K] = inputNumberArray();
  const H = inputNumberArray();

  const ans = countIf((h) => K <= h, H);
  console.log(ans);
};

main();

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [SA, TA] = inputNumberArray();
  const [SB, TB] = inputNumberArray();

  const ans = Math.max(0, Math.min(TA, TB) - Math.max(SA, SB));

  print(ans);
};

main();

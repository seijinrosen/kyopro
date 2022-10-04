import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const inputNumberArray = (): number[] => input().split(" ").map(Number);

const main = () => {
  const A = +input();
  const [B, C] = inputNumberArray();
  const S = input();

  const ans = A + B + C;
  print(ans, S);
};

main();

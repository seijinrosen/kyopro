import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const even = (n: number) => n % 2 === 0;

const main = () => {
  const [H, W, P, Q] = input().split(" ").map(Number);

  const ans = even(P + Q) ? "Black" : "White";

  console.log(ans);
};

main();

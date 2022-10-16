import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const [K, X] = input().split(" ").map(Number);

  const ans = range(X - K + 1, X + K);
  console.log(ans.join(" "));
};

main();

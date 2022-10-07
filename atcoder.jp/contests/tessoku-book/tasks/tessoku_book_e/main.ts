import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [N, K] = inputNumberArray();

  const ans = range(1, N + 1).flatMap((i) =>
    range(1, N + 1).filter((j) => {
      const k = K - i - j;
      return 1 <= k && k <= N;
    })
  ).length;

  print(ans);
};

main();

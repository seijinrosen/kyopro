import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

// input functions -------------------------------------------------------------
const inputNumberArray = () => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, Y] = inputNumberArray();

  const solve = (): [number, number, number] => {
    for (const i of range(N + 1))
      for (const j of range(N - i + 1)) {
        const k = N - i - j;
        if (10000 * i + 5000 * j + 1000 * k === Y) return [i, j, k];
      }
    return [-1, -1, -1];
  };

  const ans = solve();
  print(...ans);
};

main();

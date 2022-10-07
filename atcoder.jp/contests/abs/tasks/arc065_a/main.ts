import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const reverse = (s: string) => s.split("").reverse().join("");
const yesNo = (b: boolean | number) => (b ? "YES" : "NO");

const CANDIDATES = ["dream", "dreamer", "erase", "eraser"];
const REVERSED_CANDIDATES = CANDIDATES.map(reverse);

const solve = (s: string): boolean => {
  while (s) {
    const prefix = REVERSED_CANDIDATES.find((p) => s.startsWith(p));
    if (!prefix) return false;
    s = s.slice(prefix.length);
  }
  return true;
};

const main = () => {
  const S = input();

  const ans = solve(reverse(S));

  print(yesNo(ans));
};

main();

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const reverse = (s: string) => s.split("").reverse().join("");
const translate = (mp: Map<string, string>, s: string) =>
  s
    .split("")
    .map((c) => mp.get(c) || c)
    .join("");

const main = () => {
  const S = input();

  const d = new Map([
    ["6", "9"],
    ["9", "6"],
  ]);

  const ans = translate(d, reverse(S));
  console.log(ans);
};

main();

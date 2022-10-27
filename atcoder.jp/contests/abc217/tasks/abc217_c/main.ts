import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const enumerate = <T>(array: T[], start: number = 0): [number, T][] =>
  array.map((v, i) => [start + i, v]);

const main = () => {
  const N = +input();
  const P = input().split(" ").map(Number);

  const ans: number[] = Array(N);
  for (const [i, p] of enumerate(P, 1)) ans[p - 1] = i;

  console.log(ans.join(" "));
};

main();

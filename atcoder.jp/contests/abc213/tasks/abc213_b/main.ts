import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const enumerate = <T>(array: T[], start: number = 0): [number, T][] =>
  array.map((v, i) => [start + i, v]);
const fst = <T>(x: [T, any]) => x[0];

const main = () => {
  const N = +input();
  const A = input().split(" ").map(Number);

  const ans = fst(enumerate(A, 1).sort(([, a], [, b]) => a - b)[N - 2]);
  console.log(ans);
};

main();

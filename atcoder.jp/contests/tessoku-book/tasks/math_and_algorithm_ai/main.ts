import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const accumulate = (array: number[]) => {
  let now = 0;
  return array.map((v) => (now += v));
};

// input functions -------------------------------------------------------------
type Pair = [number, number];
const inputNumberArray = () => input().split(" ").map(Number);
const inputPairArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as Pair);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, Q] = inputNumberArray();
  const A = inputNumberArray();
  const LR = inputPairArray(Q);

  const acc = [0, ...accumulate(A)];
  const ans = LR.map(([l, r]) => acc[r] - acc[l - 1]);

  print(ans.join("\n"));
};

main();

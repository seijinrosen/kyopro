import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const [N, M] = input().split(" ").map(Number);
  const FC = [...Array(N)].map(() => input().split(" "));
  const X = input().split(" ");

  const map = new Map(FC.map(([f, c]) => [f, +c]));
  const ans = sum(X.map((x) => map.get(x) || 0));

  console.log(ans);
};

main();

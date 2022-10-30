import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const divCeil = (a: number, b: number) => Math.trunc((a + b - 1) / b);
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const N = +input();
  const [D, X] = input().split(" ").map(Number);
  const A = [...Array(N)].map(() => +input());

  const ans = X + sum(A.map(divCeil.bind(null, D)));
  console.log(ans);
};

main();

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const func = (x: number, y: number): [number, number] => {
  if (x % 2 === 1) x--;

  const tmp = div(x, 2);
  x -= tmp;
  y += tmp;

  return [x, y];
};

let [a, b, K] = input().split(" ").map(Number);

for (let i = 0; i < K; i++) {
  if (i % 2 === 0) {
    [a, b] = func(a, b);
  } else {
    [b, a] = func(b, a);
  }
}

console.log(a, b);

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const isProductDay = (m: number, d: number) => {
  const d10 = div(d, 10);
  const d1 = d % 10;
  return d1 >= 2 && d10 >= 2 && d1 * d10 === m;
};

const solve = (m: number, d: number) => {
  let ans = 0;
  for (let mm = 1; mm <= m; mm++)
    for (let dd = 1; dd <= d; dd++) if (isProductDay(mm, dd)) ans++;
  return ans;
};

const [M, D] = input().split(" ").map(Number);
console.log(solve(M, D));

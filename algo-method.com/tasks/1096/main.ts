import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const gcd = (x: number, y: number): number => (y === 0 ? x : gcd(y, x % y));

const main = () => {
  const [N, D] = input().split("/").map(Number);

  const g = gcd(N, D);
  const ans = [N / g, D / g].join("/");

  console.log(ans);
};

main();

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const [R, D, X2000] = input().split(" ").map(Number);

  let x = X2000;
  const ans = range(10).map(() => (x = R * x - D));

  console.log(ans.join("\n"));
};

main();

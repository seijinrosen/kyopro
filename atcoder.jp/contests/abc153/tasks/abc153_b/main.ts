import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [H, N] = inputNumberArray();
  const A = inputNumberArray();

  const ans = H <= sum(A);
  console.log(yesNo(ans));
};

main();

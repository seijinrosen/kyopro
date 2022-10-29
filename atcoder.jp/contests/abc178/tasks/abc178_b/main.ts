import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const max = <T extends number | bigint>(array: T[]) =>
  array.reduce((a, b) => (a < b ? b : a));

const main = () => {
  const [A, B, C, D] = input().split(" ").map(BigInt);

  const ans = max([A, B].flatMap((x) => [C, D].map((y) => x * y)));
  console.log(ans.toString());
};

main();

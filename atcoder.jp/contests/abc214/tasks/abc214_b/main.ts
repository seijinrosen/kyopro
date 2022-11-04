import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [S, T] = input().split(" ").map(Number);

  let ans = 0;
  for (let a = 0; a <= S; a++)
    for (let b = 0; b <= S - a; b++)
      for (let c = 0; c <= S - a - b; c++) if (a * b * c <= T) ans++;

  console.log(ans);
};

main();

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const reverse = (s: string) => s.split("").reverse().join("");

const main = () => {
  const S = input();

  const ans = S.length === 2 ? S : reverse(S);
  console.log(ans);
};

main();

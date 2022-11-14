import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const countText = (countString: string, s: string) =>
  [...s.matchAll(RegExp(countString, "g"))].length;

const main = () => {
  const S = input();

  const ans = countText("ZONe", S);
  console.log(ans);
};

main();

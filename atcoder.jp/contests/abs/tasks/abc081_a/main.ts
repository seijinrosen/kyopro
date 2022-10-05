import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const count = (x: string, s: string) =>
  s.split("").filter((c) => c === x).length;

const main = () => {
  const S = input();

  const ans = count("1", S);
  print(ans);
};

main();

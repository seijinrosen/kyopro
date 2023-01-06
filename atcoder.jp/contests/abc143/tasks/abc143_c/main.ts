import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const runLengthEncoding = (str: string): [string, number][] => {
  const ret: [string, number][] = [[str[0], 1]];
  for (const c of str.slice(1)) {
    if (c === ret[ret.length - 1][0]) ret[ret.length - 1][1]++;
    else ret.push([c, 1]);
  }
  return ret;
};

const _N = +input();
const S = input();

const ans = runLengthEncoding(S).length;

console.log(ans);

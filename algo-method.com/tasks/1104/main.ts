import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const runLengthEncoding = (str: string): [string, number][] => {
  const ret: [string, number][] = [[str[0], 1]];
  for (const c of str.slice(1)) {
    if (c === ret[ret.length - 1][0]) ret[ret.length - 1][1]++;
    else ret.push([c, 1]);
  }
  return ret;
};

const N = +input();
const S = input();

const runLength = runLengthEncoding(S);
let ans = 0;

while (2 <= runLength.length) {
  const [k1, v1] = runLength.pop()!;
  const [k2, v2] = runLength.pop()!;
  runLength.push([k2, v1 + v2 + 1]);
  ans += v1;
}

print(ans);

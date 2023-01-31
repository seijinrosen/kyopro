import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [N, M] = input().split(" ").map(Number);
const S = [...Array(N)].map(() => input());
const T = [...Array(M)].map(() => input());

const st = new Set(T);
const ans = S.filter((s) => st.has(s.slice(3))).length;

console.log(ans);

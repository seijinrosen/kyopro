import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const reverse = (s: string) => s.split("").reverse().join("");

const S = input();

const isPalindrome = (s: string) => s === reverse(s);
const former = (s: string) => s.slice(0, (s.length - 1) / 2);
const latter = (s: string) => s.slice((s.length + 3) / 2 - 1);

const ok = [S, former(S), latter(S)].every(isPalindrome);
const ans = ok ? "Yes" : "No";

print(ans);

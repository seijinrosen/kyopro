import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const isPalindrome = (s: string) => s.split("").reverse().join("") === s;
const rstrip = (s: string, c: string) => {
  let n = s.length;
  for (let i = n - 1; i >= 0; i--) {
    if (s[i] !== c) break;
    n--;
  }
  return s.slice(0, n);
};

const N = input();

const ans = isPalindrome(rstrip(N, "0"));
console.log(ans ? "Yes" : "No");

import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [N, M] = inputNumberArray();
  const AB = [...Array(M)].map(() => inputNumberArray() as [number, number]);

  const G = [...Array(N)].map(() => [] as number[]);
  for (const [a, b] of AB) {
    G[a - 1].push(b);
    G[b - 1].push(a);
  }

  for (const g of G)
    console.log(g.length ? g.length + " " + sort(g).join(" ") : g.length);
};

main();

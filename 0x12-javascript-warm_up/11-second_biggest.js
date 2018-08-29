#!/usr/bin/node
if (!process.argv[2]) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv.splice(2, process.argv.length - 1).sort().reverse();
  console.log(args[1]);
}

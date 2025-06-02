const fs = require('fs');
const secret = fs.readFileSync('/run/secrets/mysecret', 'utf8');
console.log("Runtime secret:", secret);
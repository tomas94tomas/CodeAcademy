const express = require('express');
const app = express();
const PORT = 3000;

const quotes = [
  "Keep it simple.",
  "Stay focused and never give up.",
  "Code is like humor. When you have to explain it, it’s bad.",
  "Before software can be reusable it first has to be usable.",
  "Fix the cause, not the symptom."
];

app.get('/quote', (req, res) => {
  const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
  res.send(randomQuote);
});

app.listen(PORT, () => {
  console.log(`Quote service running on port ${PORT}`);
});
const mongoose = require("mongoose");

const DHT11Schema = new mongoose.Schema({
  timestamp: { type: Date, default: Date.now },
  temperature: { type: Number, required: true },
  humidity: { type: Number, required: true },
});

module.exports = new mongoose.model("DHT11", DHT11Schema);

const mongoose = require("mongoose");

const MAX30100Schema = new mongoose.Schema({
  timestamp: { type: Date, default: Date.now },
  pulse_bpm: { type: Number, required: true },
  spo2_percent: { type: Number, required: true },
});

module.exports = mongoose.model("MAX30100", MAX30100Schema);

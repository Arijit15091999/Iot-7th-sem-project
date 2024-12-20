const express = require("express");
const DHT11 = require("../models/DHT11");
const MAX30100 = require("../models/MAX30100");

const router = express.Router();

// API to get all DHT11 sensor data
router.get("/dht11", async (req, res) => {
  try {
    const data = await DHT11.find().sort({ timestamp: -1 });
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: "Error fetching DHT11 data" });
  }
});

// API to add DHT11 sensor data
router.post("/dht11", async (req, res) => {
  try {
    const { temperature, humidity } = req.body;
    const newEntry = new DHT11({ temperature, humidity });
    await newEntry.save();
    res.status(201).json(newEntry);
  } catch (err) {
    res.status(400).json({ error: "Error saving DHT11 data" });
  }
});

// API to get all MAX30100 sensor data
router.get("/max30100", async (req, res) => {
  try {
    const data = await MAX30100.find().sort({ timestamp: -1 });
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: "Error fetching MAX30100 data" });
  }
});

// API to add MAX30100 sensor data
router.post("/max30100", async (req, res) => {
  try {
    const { pulse_bpm, spo2_percent } = req.body;
    const newEntry = new MAX30100({ pulse_bpm, spo2_percent });
    await newEntry.save();
    res.status(201).json(newEntry);
  } catch (err) {
    res.status(400).json({ error: "Error saving MAX30100 data" });
  }
});

module.exports = router;

const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const bodyParser = require("body-parser");
const sensorRoutes = require("./routes/sensorRoutes");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// MongoDB Connection
const mongoUri = process.env.MONGO_URI_TEMPLATE
  .replace("{MONGO_USER}", encodeURIComponent(process.env.MONGO_USER))
  .replace("{MONGO_PASSWORD}", encodeURIComponent(process.env.MONGO_PASSWORD))
  .replace("{MONGO_DATABASE}", encodeURIComponent(process.env.MONGO_DATABASE));

mongoose
  .connect(mongoUri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Routes
app.use("/api/sensors", sensorRoutes);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

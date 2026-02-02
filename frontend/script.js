async function predict() {
  const data = {
    area_sqft: parseFloat(document.getElementById("area").value),
    bedrooms: parseInt(document.getElementById("bedrooms").value),
    bathrooms: parseInt(document.getElementById("bathrooms").value),
    location_score: parseInt(document.getElementById("location").value)
  };

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById("result").innerText =
    "Predicted Price : " + result.predicted_price;
}


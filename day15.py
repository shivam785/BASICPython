import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Generate dataset
np.random.seed(42)
car_names = [f"Car_{i}" for i in range(100)]
brands = ['Toyota', 'BMW', 'Ford', 'Honda']
data = {
    'car_name': car_names,
    'year': np.random.randint(2005, 2022, 100),
    'mileage': np.random.randint(5000, 150000, 100),
    'engine_size': np.random.choice([1.2, 1.6, 2.0, 2.5, 3.0], 100),
    'brand': np.random.choice(brands, 100)
}
df = pd.DataFrame(data)

# Step 2: Create pricing logic
base_price = 30000
brand_multiplier = {'Toyota': 1.0, 'BMW': 1.5, 'Ford': 0.9, 'Honda': 1.0}
df['price'] = (
    base_price
    - (2025 - df['year']) * 1000
    - df['mileage'] * 0.05
    + df['engine_size'] * 2000 * df['brand'].map(brand_multiplier)
    + np.random.normal(0, 2000, 100)
)

# Step 3: Train model
df_encoded = pd.get_dummies(df.drop(columns=['car_name']), columns=['brand'], drop_first=True)
X = df_encoded.drop(columns=['price'])
y = df_encoded['price']
model = LinearRegression()
model.fit(X, y)

# Step 4: GUI application
def get_prediction():
    car_name = entry.get().strip()
    car = df[df['car_name'].str.lower() == car_name.lower()]
    
    if car.empty:
        messagebox.showerror("Not Found", "Car not found. Try names like Car_0 to Car_99.")
        return

    car_info = car.iloc[0]
    display_info = f"Car: {car_info['car_name']}\nBrand: {car_info['brand']}\nYear: {car_info['year']}\nMileage: {car_info['mileage']} km\nEngine Size: {car_info['engine_size']}L"
    
    # Prepare for prediction
    input_data = car.drop(columns=['car_name', 'price'])
    input_encoded = pd.get_dummies(input_data, columns=['brand'], drop_first=True)
    for col in X.columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[X.columns]
    predicted_price = model.predict(input_encoded)[0]

    result_text.set(f"{display_info}\n\nPredicted Price: ${predicted_price:,.2f}")

# Build the GUI
app = tk.Tk()
app.title("Used Car Price Predictor")
app.geometry("450x300")

tk.Label(app, text="Enter Car Name (e.g. Car_42):", font=("Helvetica", 12)).pack(pady=10)
entry = tk.Entry(app, font=("Helvetica", 12), width=30)
entry.pack()

tk.Button(app, text="Get Car Details & Predict Price", font=("Helvetica", 12), command=get_prediction).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, font=("Helvetica", 11), justify="left", wraplength=400)
result_label.pack(padx=10, pady=10)

app.mainloop()
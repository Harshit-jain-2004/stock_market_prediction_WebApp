from keras.models import load_model
from keras.models import Model, Sequential
from keras.layers import LSTM, Dense, Input

# Load the model
model = load_model('/mnt/data/LSTM_model.h5')

# Review the model architecture
model.summary()

# Rebuild if needed:
new_model = Sequential()
for layer in model.layers:
    if isinstance(layer, LSTM):
        # Ensure we remove unsupported arguments
        new_layer = LSTM(layer.units, return_sequences=layer.return_sequences)
    else:
        new_layer = layer
    
    new_model.add(new_layer)

# Save the modified model if necessary
new_model.save('/mnt/data/Updated_LSTM_model.h5')

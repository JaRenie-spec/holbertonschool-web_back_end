function createInt8TypedArray(length, position, value) {
  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView to interact with the ArrayBuffer
  const dataView = new DataView(buffer);

  // Check if the position is within bounds
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Set the value at the specified position
  dataView.setInt8(position, value);

  return dataView;
}

export default createInt8TypedArray;
